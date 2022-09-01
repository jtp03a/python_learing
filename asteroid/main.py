import pygame, sys
import random

def laser_update(laser_list, speed = 300):
  for laser in laser_list:
    laser.y -= speed * dt
    # remove the lasers from the list when they go off the top of the screen
    if laser.bottom < 0:
      laser_list.remove(laser)

def display_score():
  score_text = f'Score: {pygame.time.get_ticks() // 1000}'
  text_surf = font.render(score_text, True, 'White')
  text_rect = text_surf.get_rect(center = (WINDOW_WIDTH*.5, WINDOW_HEIGHT*.90))
  display_surface.blit(text_surf, text_rect)
  pygame.draw.rect(display_surface, 'white', text_rect.inflate(30, 30), width = 5, border_radius = 5)

def laser_timer(can_shoot, duration = 500):
  if not can_shoot:
    current_time = pygame.time.get_ticks()
    if current_time - shoot_time > duration:
      can_shoot = True
  return can_shoot

def meteor_update(meteor_list, speed = 300):
  for meteor_tuple in meteor_list:
    # to move meteor in 2 directions
    meteor_tuple[0].center += meteor_tuple[1] * speed * dt
    # only moving meteor in 1 direction
    # meteor.y += speed * dt
    if meteor_tuple[0].top > WINDOW_HEIGHT:
      meteor_list.remove(meteor_tuple)

# Game init
pygame.init()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid')
clock = pygame.time.Clock()

# importing background
background = pygame.image.load('background.png').convert()

# ship import
ship_surf = pygame.image.load('ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH*.5, WINDOW_HEIGHT*.75))
# laser import
laser_surf = pygame.image.load('laser.png').convert_alpha()
laser_list = []
# laser timer
can_shoot = True
shoot_time = 0
# text import
font = pygame.font.Font('subatomic.ttf', 50)

# import meteor
meteor_surf = pygame.image.load('meteor.png').convert_alpha()
meteor_list = []

# Meteor timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)

# import sound
laser_sound = pygame.mixer.Sound('laser.ogg')
explosion_sound = pygame.mixer.Sound('explosion.wav')
background_music = pygame.mixer.Sound('music.wav')
background_music.play(loops = -1)

# game loop
while True:
  # event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
      laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)
      laser_list.append(laser_rect)
      # timer
      can_shoot = False
      shoot_time = pygame.time.get_ticks()
      # play laser sound
      laser_sound.play()
    if event.type == meteor_timer:  
      # create rect
      meteor_rect = meteor_surf.get_rect(center = (random.randint(1,WINDOW_WIDTH), -50))
      # create a random direction
      direction = pygame.math.Vector2(random.uniform(-0.5,0.5),1)
      # add the newly generated meteor to the meteor list
      meteor_list.append((meteor_rect, direction))

  # framerate limit - delta time
  dt = clock.tick(120) / 1000  

  # Mouse input
  ship_rect.center = pygame.mouse.get_pos()

  # updates
  laser_update(laser_list)
  can_shoot = laser_timer(can_shoot, 400)
  meteor_update(meteor_list)

  # meteor -> ship collisions
  for meteor_tuple in meteor_list:
   if ship_rect.colliderect(meteor_tuple[0]):
    pygame.quit()
    sys.exit()

  # laser -> meteor collision
  for meteor_tuple in meteor_list:
    for laser in laser_list:
      if laser.colliderect(meteor_tuple[0]):
        meteor_list.remove(meteor_tuple)
        laser_list.remove(laser)
        explosion_sound.play()

  # drawing background
  display_surface.fill((0, 0, 0))
  display_surface.blit(background, (0, 0))
  # display score
  display_score() 
  # for loop that draws the lasers in the laser list
  for laser in laser_list:
    display_surface.blit(laser_surf, laser)
  # for loop that draws the meteors
  for meteor_tuple in meteor_list:
    display_surface.blit(meteor_surf, meteor_tuple[0])
  # drawing ship
  display_surface.blit(ship_surf, ship_rect)

  #draw the final frame 
  pygame.display.update()


# Rects
# rects can be used to draw shapes
# pygame.draw.rect pygame.draw.ellipse
# surfaces can be tranformed - scale flip
# pygame.transform.scale
# if you print rect you get <rect(0, 0, 99, 75)> which corresponds to Left, Top, Width, Height
# use rects to make it more precise to place surfaces, points in a rect always move together to stay relative to each other, create a surface then use it to create a rect 
# The surface stores the image and the rect stores position and movement
# Move only the rect!

# Images
# importing images - always use convert, convert_alpha for images with transperency

# Surfaces
# to create a surface use
# test_surf = pygame.Surface((400, 100))
# you need to attach the surface to the display surface - done with blit method - block image transfer
# place surface - display_surface.blit(test_surf, (WINDOW_WIDTH - test_surf.get_width(), 100))

# Text 
# To create text you first need a font object

# Event Manager
# get input from the event manager - there are two ways to access input, either in the event loop or by separate methods outside
# you can get input like this from keyboard and mosue
    # if event.type == pygame.MOUSEMOTION:
    #   ship_rect.center = event.pos
    # if event.type == pygame.MOUSEBUTTONDOWN:
    #   print('shoot')
    #   print(event.pos)
# But it is most common to just use the event loop for actions that interact with the window like exit.
# Use outside methods and classes for mouse keyboard input

# a framerate limit can be used to achieve consistent behavior across systems with different performance

# Display Surface
# always fill the entire surface before drawing anything otherwise you will get ghosting
# surfaces are drawn in the order they appear in the code, make sure to pay attn to the layers 
# The display surface is the main canvas, there is only a single display surface, it will always be shown
# There can be unlimited surfaces, they will be visible only on the display surface.

# RECT DRAWING
  # test_rect = pygame.Rect(100, 200, 400, 500)
  # pygame.draw.rect(display_surface, 'purple', test_rect, width = 10, border_radius = 5)
  # pygame.draw.lines(display_surface, 'red', True, [(0, 0), (200, 0), (300, 100)], width =50)
  
# Time and movement
# game runs at diff speeds depending on what computer it runs on, we have fluctuations based on framerate. 
# Even if we cap framerate we have no guarantee framerate will not dip below the cap
# Delta time
# measures how long it took to create one frame
# ex. 1 second / 60 fps = 0.0167 = 17 ms
# Problem with Delta time and rects
# when moving rects always placing integers because we are placing them on pixels
# when using delta time we are using floating point numbers which leads to impicent conversion

# Time
# pygame can get the time since we started the game (pygame(init))
# can use this information to create repeated timers

# Vector2
# A vector2 is a list that always contains an x and a y value
# you can multiply a vector by an integer to change both values
# it can used to move the x,y tuples of a rect
# rect.center += direction*speed*dt
#  (200, 300) += [2 -1]   *200  *0.017

# Collisions
# Types:
# Check if two rects are colliding/overlaping
# Check if a point is in a rect
# Check how close objects are to each other
# Pixel Perfect Collision
