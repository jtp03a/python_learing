import pygame, sys
from settings import *
from pygame.math import Vector2 as vector
from os import walk
from entity import Entity

class Player(Entity):
  def __init__(self, pos, groups, path, collision_sprites, shoot):
    super().__init__(pos, path, groups, shoot)

    # self.hitbox = self.rect.inflate(-self.rect.width * 0.5, -self.rect.height /2)
    self.collision_sprites = collision_sprites
    # self.mask = pygame.mask.from_surface(self.image)

    # jumping
    self.gravity = 15
    self.jump_speed = 1500
    self.on_floor = True
    self.moving_floor = None

    # overide health for player
    self.health = 10
    
  def get_status(self):
    # idle
    if self.direction.magnitude() == 0 and self.on_floor:
      self.status = self.status.split('_')[0] + '_idle'

    # attacking
    # if self.attacking:
    #   self.status = self.status.split('_')[0] + '_attack'

    # jumping
    if self.direction.y != 0 and not self.on_floor:
      self.status = self.status.split('_')[0] + '_jump'

    # ducking
    if self.ducking and self.on_floor:
      self.status = self.status.split('_')[0] + '_duck'

  def check_floor_contact(self):
    bottom_rect = pygame.Rect(0,0,self.rect.width,5)
    bottom_rect.midtop = self.rect.midbottom
    for sprite in self.collision_sprites.sprites():
      if sprite.rect.colliderect(bottom_rect):
        if self.direction.y > 0:
          self.on_floor = True
        if hasattr(sprite, 'direction'):
          self.moving_floor = sprite

  def input(self):
    keys =  pygame.key.get_pressed()
    # movement keys
    if keys[pygame.K_LEFT]:
        self.direction.x = -1
        self.status = 'left'
    elif keys[pygame.K_RIGHT]:
        self.direction.x = 1
        self.status = 'right'
    else:
        self.direction.x = 0

    if keys[pygame.K_UP] and self.on_floor:
      self.direction.y = -self.jump_speed

    if keys[pygame.K_DOWN]:
      self.ducking = True
    else:
      self.ducking = False

    if keys[pygame.K_SPACE] and self.can_shoot:

      bullet_direction = vector(1,0) if self.status.split('_')[0] == 'right' else vector(-1,0)
      pos = self.rect.center + bullet_direction * 60
      y_offset = vector(0, -16) if not self.ducking else vector(0, 10)
      self.shoot(pos + y_offset, bullet_direction, self)

      self.can_shoot = False
      self.shot_time = pygame.time.get_ticks()

  def collision(self, direction):
      for sprite in self.collision_sprites.sprites():
        if sprite.rect.colliderect(self.rect):
          if direction == 'horizontal':
            # left collision
            if self.rect.left <= sprite.rect.right and self.prev_rect.left >= sprite.prev_rect.right:
              self.rect.left = sprite.rect.right
            # right collision
            if self.rect.right >= sprite.rect.left and self.prev_rect.right <= sprite.prev_rect.left:
              self.rect.right = sprite.rect.left
            self.pos.x = self.rect.x
          elif direction == 'vertical': 
            # top collision
            if self.rect.top <= sprite.rect.bottom and self.prev_rect.top >= sprite.prev_rect.bottom:
              self.rect.top = sprite.rect.bottom
            # bottom collision
            if self.rect.bottom >= sprite.rect.top and self.prev_rect.bottom <= sprite.prev_rect.top:
              self.rect.bottom = sprite.rect.top
              self.on_floor = True
            self.pos.y = self.rect.y
            self.direction.y = 0

      # check if the player is falling
      if self.on_floor and self.direction.y != 0:
        self.on_floor = False

  def move(self, dt):  
    if self.ducking and self.on_floor:
      self.direction.x = 0

    # Horizontal movement + collision
    self.pos.x += self.direction.x * self.speed * dt
    # self.hitbox.centerx = round(self.pos.x)
    self.rect.x = round(self.pos.x)

    # get horizontal collisions
    self.collision('horizontal')

    # Vertical movement + collision
    # gravity
    self.direction.y += self.gravity
    self.pos.y += self.direction.y * dt
    # self.hitbox.centery = round(self.pos.y)
    
    # glue the player to the moving platform
    if self.moving_floor and self.moving_floor.direction.y > 0 and self.direction.y > 0:
      self.direction.y = 0
      self.rect.bottom = self.moving_floor.rect.top
      self.pos.y = self.rect.y
      self.on_floor = True
    
    self.rect.y = round(self.pos.y)

    # get vertical collisions
    self.collision('vertical')
    self.moving_floor = None

  def check_death(self):
    if self.health <= 0:
      pygame.quit()
      sys.exit()
  
  def update(self, dt):
    self.prev_rect = self.rect.copy()
    self.input()
    self.get_status()
    self.move(dt)
    self.check_floor_contact()
    self.animate(dt)
    self.blink()
    self.shoot_timer()
    self.check_death()
    self.iframes()
