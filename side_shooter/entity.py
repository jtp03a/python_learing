import pygame
from settings import *
from pygame.math import Vector2 as vector
from os import walk
from math import sin

class Entity(pygame.sprite.Sprite):
  def __init__(self, pos, path, groups, shoot):
    super().__init__(groups)
    
    # setup
    self.import_assets(path)
    self.frame_index = 0
    self.status = 'right'

    # image setup
    self.image = self.animations[self.status][self.frame_index]
    self.rect = self.image.get_rect(topleft = pos)
    self.z = LAYERS['Level']
    self.mask = pygame.mask.from_surface(self.image)

    # float based movement
    self.pos = vector(self.rect.center)
    self.direction = vector(0, 0)
    self.speed = 400
    # collisions
    self.prev_rect = self.rect.copy()

    # shooting setup
    self.shoot = shoot

    # shot timer
    self.can_shoot = True
    self.shot_time = pygame.time.get_ticks()
    self.cooldown = 200

    # ducking
    self.ducking = False

    # health
    self.health = 3
    self.is_vulnerable = True
    self.hit_time = None
    self.iframe_dur = 500

  def import_assets(self, path):
    self.animations = {}
    for index, folder in enumerate(walk(path)):
      if index == 0:
        for name in folder[1]:
          self.animations[name] = []
      else: 
        for file_name in sorted(folder[2], key = lambda string: int(string.split('.')[0])):
          fixed_path = folder[0].replace('\\', '/')
          path = f'{fixed_path}/{file_name}'
          surf = pygame.image.load(path).convert_alpha()
          key = folder[0].split('\\')[1]
          self.animations[key].append(surf)

  def shoot_timer(self):
    if not self.can_shoot:
      current_time = pygame.time.get_ticks()
      if current_time - self.shot_time > self.cooldown:
        self.can_shoot = True

  def animate(self, dt):
    current_animation = self.animations[self.status]

    self.frame_index += 10 * dt
    
    if self.frame_index >= len(current_animation):
      self.frame_index = 0

    self.image = current_animation[int(self.frame_index)]
    self.mask = pygame.mask.from_surface(self.image)

  def damage(self):
    if self.is_vulnerable:
      self.is_vulnerable = False
      self.hit_time = pygame.time.get_ticks()
      self.health -= 1

  def check_death(self):
    if self.health <= 0:
      self.kill()

  def iframes(self):
    if not self.is_vulnerable:
      current_time = pygame.time.get_ticks()
      if current_time - self.hit_time > self.iframe_dur:
        self.is_vulnerable = True

  def blink(self):
    if not self.is_vulnerable:
      if self.wave_value():
        mask = pygame.mask.from_surface(self.image)
        white_surf = mask.to_surface()
        white_surf.set_colorkey((0, 0, 0))
        self.image = white_surf

  def wave_value(self):
    value = sin(pygame.time.get_ticks())
    if value >= 0:
      return True
    else:
      return False