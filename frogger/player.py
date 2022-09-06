import pygame, sys
from os import walk

class Player(pygame.sprite.Sprite):
  def __init__(self, groups, pos, collision_sprites):
    super().__init__(groups)
    self.import_assets()
    self.frame_index = 0
    self.status = 'down'
    # self.image = self.animation[self.frame_index]
    self.image = self.animations[self.status][self.frame_index]
    self.rect = self.image.get_rect(center = pos)
    self.pos = pygame.math.Vector2(self.rect.center)
    self.direction = pygame.math.Vector2(0, 0)
    self.speed = 200
    # collisions
    self.collision_sprites = collision_sprites
    self.hitbox = self.rect.inflate(0, -self.rect.height /2)

  def collision(self, direction):
    if direction == 'horizontal':
      for sprite in self.collision_sprites.sprites():
        if sprite.hitbox.colliderect(self.hitbox):
          # check if the object colliding with has a attribute of name is car, if so end the game, dont do collision logic
          if hasattr(sprite, 'name') and sprite.name == 'car':
            pygame.quit()
            sys.exit()
          if self.direction.x > 0:
            self.hitbox.right = sprite.hitbox.left
            self.rect.centerx = self.hitbox.centerx
            self.pos.x = self.hitbox.centerx
          elif self.direction.x < 0:
            self.hitbox.left = sprite.hitbox.right
            self.rect.centerx = self.hitbox.centerx
            self.pos.x = self.hitbox.centerx
    else: 
      for sprite in self.collision_sprites.sprites():
        if sprite.hitbox.colliderect(self.hitbox):
          # check if the object colliding with has a attribute of name is car, if so end the game, dont do collision logic
          if hasattr(sprite, 'name') and sprite.name == 'car':
            pygame.quit()
            sys.exit()
          if self.direction.y > 0:
            self.hitbox.bottom = sprite.hitbox.top
            self.rect.centery = self.hitbox.centery
            self.pos.y = self.hitbox.centery
          elif self.direction.y < 0:
            self.hitbox.top = sprite.hitbox.bottom
            self.rect.centery = self.hitbox.centery
            self.pos.y = self.hitbox.centery

  def import_assets(self):
    # list comprehension
    # self.animation = [pygame.image.load(f'./graphics/player/right/{i}.png').convert_alpha() for i in range(4)]

    # better import
    self.animations = {}
    for index, folder in enumerate(walk('./graphics/player')):
      if index == 0:
        for name in folder[1]:
          self.animations[name] = []
      else:
        for file_name in folder[2]:
          fixed_path = folder[0].replace('\\', '/')
          path = f'{fixed_path}/{file_name}'
          surf = pygame.image.load(path).convert_alpha()
          key = folder[0].split('\\')[1]
          self.animations[key].append(surf)

    # for loop way - complicated
    # for i in range(4):
    #   new_surf = pygame.image.load(f'./graphics/player/right/{i}.png').convert_alpha()
    #   self.animation.append(new_surf)

  def move(self, dt):
    # normalize the vector -> the length of a vector is going to be 1
    if self.direction.magnitude() != 0:
      self.direction = self.direction.normalize()

    # need to seperate the horizonatal and verticle movements for collision detection
    # horizontal movement + collision
    self.pos.x += self.direction.x * self.speed * dt
    # the hitbox and the image rect need to keep the same center pos
    self.hitbox.centerx = round(self.pos.x)
    self.rect.centerx = self.hitbox.centerx

    # get horizontal collisions
    self.collision('horizontal')

    # verticle movement + collision
    self.pos.y += self.direction.y * self.speed * dt
    self.hitbox.centery = round(self.pos.y)
    self.rect.centery = self.hitbox.centery

    #  get verticle collisions
    self.collision('verticle')

  def input(self):
    keys =  pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      self.direction.x = -1
      self.status = 'left'
    elif keys[pygame.K_RIGHT]:
      self.direction.x = 1
      self.status = 'right'
    else:
      self.direction.x = 0
    if keys[pygame.K_UP]:
      self.direction.y = -1
      self.status = 'up'
    elif keys[pygame.K_DOWN]:
      self.direction.y = 1
      self.status = 'down'
    else:
      self.direction.y = 0

  def animate(self, dt):
    current_animation = self.animations[self.status]
    if self.direction.magnitude() != 0:
      self.frame_index += 10 * dt
      if self.frame_index >= len(current_animation):
        self.frame_index = 0
    else:
      self.frame_index = 0
    self.image = current_animation[int(self.frame_index)]

  def boundary(self):
    if self.rect.left < 640:
      self.pos.x = 640 + self.rect.width /2
      self.hitbox.left = 640
      self.rect.left = 640

    if self.rect.right > 2560:
      self.pos.x = 2560 - self.rect.width/2
      self.hitbox.right = 2650
      self.rect.right = 2560

    if self.rect.bottom > 3500:
      self.pos.y = 3500 - self.rect.height/2
      self.rect.bottom = 3500
      self.hitbox.centery = self.rect.centery



       
  def update(self, dt):
    self.input()
    self.move(dt)
    self.animate(dt)
    self.boundary()
