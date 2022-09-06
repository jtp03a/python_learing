import pygame
from os import walk
import random

class Car(pygame.sprite.Sprite):
  def __init__(self, groups, pos):
    super().__init__(groups)
    self.image = self.import_assets()
    self.rect = self.image.get_rect(center = pos)
    self.pos = pygame.math.Vector2(self.rect.center)

    if pos[0] < 200:
      self.direction = pygame.math.Vector2((1, 0))
    else:
      self.image = pygame.transform.flip(self.image, True, False)
      self.direction = pygame.math.Vector2((-1, 0))
    self.speed = 300
    self.name = 'car'
    self.hitbox = self.rect.inflate(0, -self.rect.height /3)


  def import_assets(self):
    for _, _, file_name in walk('./graphics/cars'):
        random_car = random.choice(file_name)
    return pygame.image.load(f'./graphics/cars/{random_car}').convert_alpha()

  def update(self, dt):
    self.pos += self.direction * self.speed * dt
    self.hitbox.center = (round(self.pos.x), round(self.pos.y))
    self.rect.center = self.hitbox.center

    if not -200 < self.rect.x < 3400:
      self.kill()