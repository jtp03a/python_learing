import pygame, sys
import random

class Player(pygame.sprite.Sprite):
  def __init__(self, pos_x, pos_y):
    super().__init__()
    self.sprites = []
    self.is_animating = False
    self.sprites.append(pygame.image.load('./animation/attack_1.png'))
    self.sprites.append(pygame.image.load('./animation/attack_2.png'))
    self.sprites.append(pygame.image.load('./animation/attack_3.png'))
    self.sprites.append(pygame.image.load('./animation/attack_4.png'))
    self.sprites.append(pygame.image.load('./animation/attack_5.png'))
    self.sprites.append(pygame.image.load('./animation/attack_6.png'))
    self.sprites.append(pygame.image.load('./animation/attack_7.png'))
    self.sprites.append(pygame.image.load('./animation/attack_8.png'))
    self.sprites.append(pygame.image.load('./animation/attack_9.png'))
    self.sprites.append(pygame.image.load('./animation/attack_10.png'))
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]
    self.rect = self.image.get_rect()
    self.rect.topleft = [pos_x, pos_y]
  
  def update(self):
    if self.is_animating == True:
      self.current_sprite += 0.2

      if self.current_sprite >= len(self.sprites):
        self.current_sprite = 0
        self.is_animating = False

      self.image = self.sprites[int(self.current_sprite)]

  def animate(self):
    self.is_animating = True





# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

moving_sprites = pygame.sprite.Group()
player = Player(10, 10)
moving_sprites.add(player)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      player.animate()

  # Drawing
  screen.fill((0, 0, 0))
  moving_sprites.draw(screen)
  moving_sprites.update()
  pygame.display.flip()
  clock.tick(60)