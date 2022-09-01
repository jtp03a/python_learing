import pygame, sys 
from settings import *
from player import Player

# basic setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

# sprite groups
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()

# sprite creation
player = Player(all_sprites, (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

# game loop
while True:
	
	# event loop 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# delta time 
	dt = clock.tick() / 1000

	# Updates
	all_sprites.update()

	# Graphics
	all_sprites.draw(display_surface)

	# update the display surface -> drawing the frame 
	pygame.display.update()

	# Keyboard input
	# in event loop
	# if event.type == pygame.KEYDOWN:
	# 	if event.key == pygame.K_a:
	#  method
	# keys = pygame.key.get_pressed([K_a])
