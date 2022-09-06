import pygame, sys
from settings import * 
from pytmx.util_pygame import load_pygame
from pygame.math import Vector2 as vector
from tile import Tile, CollisionTile, MovingPlatform
from player import Player
from bullet import Bullet, FireAnimation
from enemy import Enemy
from overlay import Overlay

class AllSprites(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.offset = vector()
		self.display_surface = pygame.display.get_surface()

		# Sky
		# imports
		self.fg_sky = pygame.image.load('./graphics/sky/fg_sky.png').convert_alpha()
		self.bg_sky = pygame.image.load('./graphics/sky/bg_sky.png').convert_alpha()
		tmx_map = load_pygame('./data/map.tmx')

		# get dimensions
		self.padding = WINDOW_WIDTH /2
		map_width = tmx_map.tilewidth * tmx_map.width + (2 * self.padding)
		self.sky_width = self.bg_sky.get_width()

		self.sky_num = int(map_width // self.sky_width)

	def custom_draw(self, player):
		# change the offset vector - move anything in the game in the oposite direction as the player to simulate camera
		self.offset.x = player.rect.centerx - WINDOW_WIDTH /2
		self.offset.y = player.rect.centery - WINDOW_HEIGHT /2

		for x in range(self.sky_num):
			x_pos = -self.padding + (x * self.sky_width)
			self.display_surface.blit(self.bg_sky, (x_pos - self.offset.x / 2.5, 600 - self.offset.y /2.5))
			self.display_surface.blit(self.fg_sky, (x_pos - self.offset.x / 2, 800 - self.offset.y /2))

		# blit the surfaces
		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.z):
			offset_rect = sprite.image.get_rect(center = sprite.rect.center)
			offset_rect.center -= self.offset
			self.display_surface.blit(sprite.image, offset_rect)


class Main:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption('Side Shooter')
		self.clock = pygame.time.Clock()

		# groups
		self.all_sprites = AllSprites()
		self.collision_sprites = pygame.sprite.Group()
		self.platform_sprites = pygame.sprite.Group()
		self.bullet_sprites = pygame.sprite.Group()
		self.vulnerable_sprites = pygame.sprite.Group()

		self.setup()
		self.overlay = Overlay(self.player)

		# bullet images
		self.bullet_surf = pygame.image.load('./graphics/bullet.png').convert_alpha()
		self.fire_surfs = [pygame.image.load('./graphics/fire/0.png').convert_alpha(), 
											 pygame.image.load('./graphics/fire/1.png').convert_alpha()]

		# music
		self.bg_music = pygame.mixer.Sound('./audio/music.wav')
		self.bg_music.play(loops = -1)

		self.hit_sound = pygame.mixer.Sound('./audio/hit.wav')

	def setup(self):
		tmx_map = load_pygame('./data/map.tmx')
		
		# collision tiles
		for x, y, surf in tmx_map.get_layer_by_name('Level').tiles():
			CollisionTile((x * 64, y * 64), surf, [self.all_sprites, self.collision_sprites])

		# tiles
		for layer in ['BG', 'BG Detail', 'FG Detail Top', 'FG Detail Bottom']:
			for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
				Tile((x * 64, y * 64), surf, self.all_sprites, LAYERS[layer])

		# entities
		for obj in tmx_map.get_layer_by_name('Entities'):
			if obj.name == 'Player':
				self.player = Player(
					groups = [self.all_sprites, self.vulnerable_sprites], 
					pos = (obj.x, obj.y),
					path = './graphics/player',
					collision_sprites = self.collision_sprites,
					shoot = self.shoot
					)
			if obj.name == 'Enemy':
				Enemy(
					groups = [self.all_sprites, self.vulnerable_sprites], 
					pos = (obj.x, obj.y),
					path = './graphics/enemies/standard',
					collision_sprites = self.collision_sprites,
					shoot = self.shoot,
					player = self.player
					)			

		self.platform_border_rects = []
		for obj in tmx_map.get_layer_by_name('Platforms'):
			if obj.name == 'Platform':
				MovingPlatform(
					pos = (obj.x, obj.y),
					surf = obj.image,
					groups = [self.all_sprites, self.collision_sprites, self.platform_sprites])
			else:
				border_rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
				self.platform_border_rects.append(border_rect)

	def platform_collisions(self):
		for platform in self.platform_sprites.sprites():
			for border in self.platform_border_rects:
				if platform.rect.colliderect(border):
					if platform.direction.y < 0:
						platform.rect.top = border.bottom
						platform.pos.y = platform.rect.y
						platform.direction.y = 1
					else:
						platform.rect.bottom = border.top
						platform.pos.y = platform.rect.y
						platform.direction.y = -1
			if platform.rect.colliderect(self.player.rect) and self.player.rect.centery > platform.rect.centery:
				platform.rect.bottom = self.player.rect.top
				platform.pos.y = platform.rect.y
				platform.direction.y = -1

	def shoot(self, pos, direction, entity):
		Bullet(pos, self.bullet_surf, direction, [self.all_sprites, self.bullet_sprites])
		FireAnimation(entity, self.fire_surfs, direction, self.all_sprites)

	def bullet_collisions(self):
		# with obstacles
		for obstacle in self.collision_sprites.sprites():
			pygame.sprite.spritecollide(obstacle, self.bullet_sprites, True)

		# with entities
		for sprite in self.vulnerable_sprites.sprites():
			if pygame.sprite.spritecollide(sprite, self.bullet_sprites, True, pygame.sprite.collide_mask):
				sprite.damage()
				self.hit_sound.play()
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			dt = self.clock.tick() / 1000
			self.display_surface.fill((249,131,103))
			self.platform_collisions()
			self.all_sprites.update(dt)
			self.bullet_collisions()
			self.all_sprites.custom_draw(self.player)
			self.overlay.display()

			pygame.display.update()

if __name__ == '__main__':
	main = Main()
	main.run()
