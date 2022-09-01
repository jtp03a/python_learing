from xml.dom import minidom
import pygame, sys
import random

class Ship(pygame.sprite.Sprite):
  def __init__(self, groups):
    super().__init__(groups)
    # Sprite surface/image
    self.image = pygame.image.load('ship.png').convert_alpha()
    # Sprite rect
    self.rect = self.image.get_rect(center = (WINDOW_WIDTH*.5, WINDOW_HEIGHT*.75))
    # collision mask
    self.mask = pygame.mask.from_surface(self.image)
    # Shoot timer
    self.can_shoot = True
    self.shoot_time = 0
    self.laser_sound = pygame.mixer.Sound('laser.ogg')

  def input_position(self):
    m_pos = pygame.mouse.get_pos()
    self.rect.center = m_pos

  def laser_shoot(self):
    if pygame.mouse.get_pressed()[0]:
      if self.can_shoot:
        self.laser_sound.play()
        Laser(laser_group, self.rect.midtop)
        self.can_shoot = False
        self.shoot_time = pygame.time.get_ticks()
      else:
        current_time = pygame.time.get_ticks()
        duration = 500
        if current_time - self.shoot_time > duration:
          self.can_shoot = True

  def update(self):
    self.input_position()
    self.laser_shoot()

class Laser(pygame.sprite.Sprite):
  def __init__(self, groups, rect_pos):
    super().__init__(groups)
    # Sprite surface/image
    self.image = pygame.image.load('laser.png').convert_alpha()
    # Sprite rect
    self.rect = self.image.get_rect(midbottom = rect_pos)
    # mask
    self.mask = pygame.mask.from_surface(self.image)
    # float based position
    self.pos = pygame.math.Vector2(self.rect.topleft)
    self.direction = pygame.math.Vector2(0,-1)
    self.speed = 600

  def update(self):
    self.pos += self.direction * self.speed * dt
    self.rect.topleft = (round(self.pos.x), round(self.pos.y))
    if self.rect.bottom < 0:
      self.kill()

class Meteor(pygame.sprite.Sprite):
  def __init__(self, groups, pos):
    super().__init__(groups)
    # randomize the meteor size
    meteor_surf = pygame.image.load('meteor.png').convert_alpha()
    size_mult = random.uniform(0.5, 2)
    meteor_size = pygame.math.Vector2(meteor_surf.get_size()) * size_mult
    self.scaled_surf = pygame.transform.scale(meteor_surf, meteor_size)
    self.image = self.scaled_surf
    self.rect = self.image.get_rect(center = pos)
    self.mask = pygame.mask.from_surface(self.image)
    self.pos = pygame.math.Vector2(self.rect.topleft)
    self.direction = pygame.math.Vector2(random.uniform(-0.5, 0.5),1)
    self.speed = random.randint(400, 600)
    # rotation logic
    self.rotation = 0
    self.rotation_speed = random.randint(20, 50)
    self.explode_sound = pygame.mixer.Sound('explosion.wav')

  def laser_collision(self):
    if pygame.sprite.spritecollide(self, laser_group, True, pygame.sprite.collide_mask):
      self.explode_sound.play()
      self.kill()

  def ship_collision(self):
    if pygame.sprite.spritecollide(self, ship_group, False, pygame.sprite.collide_mask):
      self.explode_sound.play()
      # pygame.quit()
      # sys.exit()

  def rotate(self):
    self.rotation += self.rotation_speed * dt
    rotated_surf = pygame.transform.rotozoom(self.scaled_surf, self.rotation, 1)
    self.image = rotated_surf
    self.rect = self.image.get_rect(center = self.rect.center)
    self.mask = pygame.mask.from_surface(self.image)

  def update(self):
    self.pos += self.direction * self.speed * dt
    self.rect.topleft = (round(self.pos.x), round(self.pos.y))
    if self.rect.top > WINDOW_HEIGHT:
      self.kill()
    self.rotate()
    self.laser_collision()
    self.ship_collision()

class Score:
  def __init__(self):
    self.font = pygame.font.Font('subatomic.ttf', 50)

  def display(self):
    score_text = f'Score: {pygame.time.get_ticks() // 1000}'
    text_surf = self.font.render(score_text, True, 'White')
    text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH*.5, WINDOW_HEIGHT - 80))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(
      display_surface, 
      'white', 
      text_rect.inflate(30, 30), 
      width = 5, 
      border_radius = 5)

# game init and setup
pygame.init()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid w/ Classes')
clock = pygame.time.Clock()

# importing background
background = pygame.image.load('background.png').convert()

# sprite groups
ship_group = pygame.sprite.GroupSingle()
laser_group = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()

# sprite creation
ship = Ship(ship_group)
score = Score()

# Meteor timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)

# import sound
background_music = pygame.mixer.Sound('music.wav')
background_music.play(loops = -1)

# game loop
while True:
  # event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == meteor_timer:  
      meteor_y_pos = random.randint(-150, -50)
      meteor_x_pos = random.randint(-100, WINDOW_WIDTH + 100)
      Meteor(meteor_group, (meteor_x_pos, meteor_y_pos))

  # framerate limit - delta time
  dt = clock.tick() / 1000

  # draw display surface
  display_surface.fill((0, 0, 0))
  # draw background
  display_surface.blit(background, (0, 0))

  # Updates
  ship_group.update()
  laser_group.update()
  meteor_group.update()

  # Graphics
  score.display()
  ship_group.draw(display_surface)
  laser_group.draw(display_surface)
  meteor_group.draw(display_surface)

  # final frame
  pygame.display.update()

  # Sprites
  # A sprite is a class that must have a rect and a surface
  # Allows you to control the graphics, positions, input, and update mechanics for each object

  # Sprite Groups
  # To display a sprite it needs to be put inside a group
  # The group draws the sprite on a surface (usually the display surface but could be another surface)
  # The group can also update the sprite
  # There is also a pygame group type of GroupSingle that can be used for sprite groups that only contain one sprite
  # if you try and add another sprite to a GroupSingle it will overwrite the sprite in there

  # Sprint Collision
  # pygame.sprite.spritecollide(sprite, group, DoKill)
  # check if a sprite collides with any sprite in a group and get a list of the collided sprites in the group
  # dokill will delete sprite in the group
  # use rects of each sprite object for the collision

  # improve collision with masking
  # a mask is a seperate object that checks which pixels are occupied in a surface - pixel perfect collisions




