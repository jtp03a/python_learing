import pygame, sys
from settings import * 
from player import Player
from pygame.math import Vector2 as vector
from pytmx.util_pygame import load_pygame
from sprite import Sprite, Bullet
from monster import Coffin, Cactus

class AllSprites(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.offset = vector()
		self.display_surface = pygame.display.get_surface()
		self.bg = pygame.image.load('./graphics/other/bg.png').convert()

	def custom_draw(self, player):
		# change the offset vector - move anything in the game in the oposite direction as the player to simulate camera
		self.offset.x = player.rect.centerx - WINDOW_WIDTH /2
		self.offset.y = player.rect.centery - WINDOW_HEIGHT /2

		# blit background, should always come first
		self.display_surface.blit(self.bg, -self.offset)

		# blit the surfaces
		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
			offset_rect = sprite.image.get_rect(center = sprite.rect.center)
			offset_rect.center -= self.offset
			self.display_surface.blit(sprite.image, offset_rect)


class Game:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption('Western shooter')
		self.clock = pygame.time.Clock()
		self.bullet_surf = pygame.image.load('./graphics/other/particle.png').convert_alpha()

		# groups
		self.all_sprites = AllSprites()
		self.obstacles = pygame.sprite.Group()
		self.bullets = pygame.sprite.Group()
		self.monsters = pygame.sprite.Group()
		
		self.setup()

		self.music = pygame.mixer.Sound('./sound/music.mp3')
		self.music.play(loops = -1)

	def create_bullet(self, pos, direction):
		Bullet([self.all_sprites, self.bullets], pos, direction, self.bullet_surf)

	def bullet_collision(self):
		# bullet obstacle collision
		for obstacle in self.obstacles.sprites():
			pygame.sprite.spritecollide(obstacle, self.bullets, True)

		# # bullet monster collision
		for bullet in self.bullets.sprites():
			sprites = pygame.sprite.spritecollide(bullet, self.monsters, False, pygame.sprite.collide_mask)
	
			if sprites:
				bullet.kill()
				for sprite in sprites:
					sprite.damage()

		# player bullet collision
		if pygame.sprite.spritecollide(self.player, self.bullets, True, pygame.sprite.collide_mask):
			self.player.damage()

	def setup(self):
		tmx_map = load_pygame('./data/map.tmx')
		
		# tiles
		for x, y, surf in tmx_map.get_layer_by_name('Fence').tiles():
			# the x, y from tiled are the grid positions. since the tile size was setup as 64, 64 we can just multiply by 64 to get the actual x, y for the pygame display surface
			Sprite([self.all_sprites, self.obstacles], (x * 64, y * 64), surf)

		# objects
		for obj in tmx_map.get_layer_by_name('Object'):
			Sprite([self.all_sprites, self.obstacles], (obj.x, obj.y), obj.image)
			
		# entities
		for obj in tmx_map.get_layer_by_name('Entities'):
			if obj.name == 'Player':
				self.player = Player(
					groups = self.all_sprites, 
					pos = (obj.x, obj.y), 
					path = PATHS['player'], 
					collision_sprites = self.obstacles, 
					create_bullet = self.create_bullet)

			if obj.name == 'Coffin':
				Coffin(
					groups = [self.all_sprites, self.monsters], 
					pos = (obj.x, obj.y), 
					path = PATHS['coffin'], 
					collision_sprites = self.obstacles,
					player = self.player)

			if obj.name == 'Cactus':
				Cactus(
					groups = [self.all_sprites, self.monsters], 
					pos = (obj.x, obj.y), 
					path = PATHS['cactus'], 
					collision_sprites = self.obstacles,
					player = self.player,
					create_bullet = self.create_bullet)
	
	def run(self):
		while True:
			# event loop 
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			dt = self.clock.tick() / 1000

			# fill display_surface
			self.display_surface.fill('black')

			# update groups
			self.all_sprites.update(dt)
			self.bullet_collision()

			# draw groups
			self.all_sprites.custom_draw(self.player)

			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()