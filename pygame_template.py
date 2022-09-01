import pygame, sys

# game init and setup
pygame.init()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid w/ Classes')
clock = pygame.time.Clock()








# game loop
while True:
  # event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  # framerate limit - delta time
  dt = clock.tick(120) / 1000





  # draw display surface
  display_surface.fill((0, 0, 0))



  

  # final frame
  pygame.display.update()