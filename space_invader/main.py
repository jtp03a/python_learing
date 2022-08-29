import pygame
import random
from enemy import Enemy_Manager
from pygame import mixer
import math

# constants
screen_width = 800
screen_height = 600
bg_fill = (0, 0, 0)

# Initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Background
background = pygame.image.load('background.png')

# Background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and icon
pygame.display.set_caption("Jake's Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load("spaceship.png")
player_loc = player_img.get_rect()
player_x = 370
player_y = 480
player_x_move_spd = 0
player_move_vel = 3

# Enemy
enemy_manager = Enemy_Manager()
num_of_enemies = 6

for i in range(num_of_enemies):
  enemy_manager.create_enemy(pygame.image.load("aircraft.png"))

# Missile
missile_img = pygame.image.load("missile.png")
missile_loc = missile_img.get_rect()
missile_x = 370
missile_y = 480
missile_x_move_spd = 5
missile_state = "ready"

# Explosion
explosion_img = pygame.image.load("explode.png")

# Score
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10

# Game over text
gamer_over_font = pygame.font.Font("freesansbold.ttf", 64)

def game_over():
  mixer.music.stop()
  game_over_ren = gamer_over_font.render("GAME OVER", True, (255, 255, 255))
  game_over_rect = game_over_ren.get_rect(center=(screen_width/2, screen_height/2))
  screen.blit(game_over_ren, game_over_rect)

def show_score(x, y):
  score_ren = font.render(f"Score: {score}", True, (255, 255, 255))
  screen.blit(score_ren, (x, y))

def player(x, y):
  screen.blit(player_img, (x, y))

def draw_enemy(img, x, y):
  screen.blit(img, (x, y))

def fire_missile(x, y):
  global missile_state
  missile_state = "fire"
  screen.blit(missile_img, (x + 16, y-15))

def explode(x, y):
  bullet_explosion = mixer.Sound("explosion.wav")
  bullet_explosion.play()
  screen.blit(explosion_img, (x, y))

# Game loop
running = True
game_over_state = False
while running:
  screen.fill(bg_fill)
  screen.blit(background, (0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        if missile_state is "ready":
          missile_x = player_x
          missile_y = player_y
          fire_missile(missile_x, missile_y)
          bullet_sound = mixer.Sound("laser.wav")
          bullet_sound.play()

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    player_x_move_spd = -(player_move_vel)
  elif keys[pygame.K_RIGHT]:
    player_x_move_spd = player_move_vel
  else:
    player_x_move_spd = 0

  player_x += player_x_move_spd
  enemy_manager.move_enemy()

  # Bullet movement
  if missile_y <=-32:
    missile_y = 480
    missile_state = "ready"
  if missile_state is "fire":
    fire_missile(missile_x, missile_y)
    missile_y -= missile_x_move_spd

  # Bullet collision
  for enemy in enemy_manager.enemies:
    if math.dist((enemy.x_pos, enemy.y_pos), (missile_x, missile_y)) < 32:
    # if enemy.img.get_rect(x = enemy.x_pos, y = enemy.y_pos).colliderect(missile_img.get_rect(x = missile_x, y = missile_y)):
      explode(enemy.x_pos, enemy.y_pos)
      missile_y = 480
      missile_state = "ready"
      score += 1
      hit_index = enemy_manager.enemies.index(enemy)
      enemy_manager.travel_mult += 0.1
      enemy.travel *= -1
      enemy.x_pos = random.randint(1, 735)
      enemy.y_pos = random.randint(1, 100)

  # collision with player
  for enemy in enemy_manager.enemies:
    if math.dist((enemy.x_pos, enemy.y_pos), (player_x, player_y)) < 64:
    # if enemy.img.get_rect(x = enemy.x_pos, y = enemy.y_pos).colliderect(player_img.get_rect(x = player_x, y = player_y)):
      explode(player_x, player_y)
      enemy_manager.game_over()
      game_over_state = True

  # boundary detection
  if player_x <= 0:
    player_x = 0
  elif player_x >= 736:
    player_x = 736

  if game_over_state:
    game_over()
  player(player_x, player_y)
  for enemy in enemy_manager.enemies:
    draw_enemy(enemy.img, enemy.x_pos, enemy.y_pos)
  show_score(text_x, text_y)
  pygame.display.update()
