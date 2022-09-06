from dis import dis
import pygame, sys 
from settings import *
from player import Player
from car import Car
import random
from sprite import SimpleSprite, LongSprite

# used for camera implementation. provide an offset to move everything around the display surface, cant move display surface
class AllSprites(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.offset = pygame.math.Vector2(0, 0)
		self.bg = pygame.image.load('./graphics/main/map.png').convert()
		self.fg = pygame.image.load('./graphics/main/overlay.png').convert_alpha()

	def custom_draw(self):
		# change the offset vector
		self.offset.x = player.rect.centerx - WINDOW_WIDTH /2
		self.offset.y = player.rect.centery - WINDOW_HEIGHT /2

		# blit background, should always come first
		display_surface.blit(self.bg, -self.offset)

		# lamda function here is used to short all the sprite based on y position so that 3d is simulated
		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			display_surface.blit(sprite.image, offset_pos)

		# blit forground, should always come last
		display_surface.blit(self.fg, -self.offset)

# basic setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

# sprite groups
all_sprites = AllSprites()
obstacle_sprites = pygame.sprite.Group()

# sprite creation
player = Player(all_sprites, (2062, 3274), obstacle_sprites)

# simple sprites
for file_name, pos_list in SIMPLE_OBJECTS.items():
	path = f'./graphics/objects/simple/{file_name}.png'
	surf = pygame.image.load(path).convert_alpha()
	for pos in pos_list:
		SimpleSprite([all_sprites, obstacle_sprites], surf, pos)

# long sprites
for file_name, pos_list in LONG_OBJECTS.items():
	path = f'./graphics/objects/long/{file_name}.png'
	surf = pygame.image.load(path).convert_alpha()
	for pos in pos_list:
		LongSprite([all_sprites, obstacle_sprites], surf, pos)

# car timer
car_timer = pygame.event.custom_type()
pygame.time.set_timer(car_timer, 50)
pos_list = []

# Text
font = pygame.font.Font(None, 50)
text_surf = font.render('YOU WON', True, 'White')
text_rect = text_surf.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

# music
bg_music = pygame.mixer.Sound('./audio/music.mp3')
bg_music.play(-1)

# game loop
while True:
	
	# event loop 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == car_timer:
			# random car side and position
			rand_pos = random.choice(CAR_START_POSITIONS)
			if rand_pos not in pos_list:
				pos_list.append(rand_pos)
				pos = (rand_pos[0], rand_pos[1] + random.randint(-8, 8))
				new_car = Car([all_sprites, obstacle_sprites], pos)
			if len(pos_list) > 5:
				del pos_list[0]

	# delta time 
	dt = clock.tick() / 1000

	# Display surface fill
	display_surface.fill('black')
	
	if player.pos.y >= 1180:
		# Updates
		all_sprites.update(dt)
		# graphics
		all_sprites.custom_draw()
	else:
		display_surface.fill('teal')
		display_surface.blit(text_surf, text_rect)

	# update the display surface -> drawing the frame 
	pygame.display.update()

	# Keyboard input
	# in event loop
	# if event.type == pygame.KEYDOWN:
	# 	if event.key == pygame.K_a:
	#  method
	# keys = pygame.key.get_pressed([K_a])

	# Animation
	# In a sprite
	# self.image determines how the sprite looks - going to change self.image quickly
	# self.rect deterines the position
	# both can be changed 

	# Cameras
	# cannot move display surface
	# we have to move everything else
	# 
