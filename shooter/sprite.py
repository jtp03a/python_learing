import pygame
from pygame.math import Vector2 as vector

class Sprite(pygame.sprite.Sprite):
  def __init__(self, groups, pos, surf):
    super().__init__(groups)
    self.image = surf
    self.mask = pygame.mask.from_surface(self.image)
    self.rect = self.image.get_rect(topleft = pos)
    self.hitbox = self.rect.inflate(0, -self.rect.height /3)

class Bullet(pygame.sprite.Sprite):
  def __init__(self, groups, pos, direction, surf):
    super().__init__(groups)
    self.image = surf
    self.rect = self.image.get_rect(center = pos)
    self.shoot_sound = pygame.mixer.Sound('./sound/bullet.wav')
    self.shoot_sound.play()

    # float based movement
    self.pos = vector(self.rect.center)
    self.direction = direction
    self.speed = 400

  def update(self, dt):
    self.pos += self.direction * self.speed * dt
    self.rect.center = (round(self.pos.x), round(self.pos.y))

