from ssl import enum_certificates
import pygame
import random

class Enemy:
  def __init__(self, img):
    self.img = img
    self.x_pos = 0
    self.y_pos = 0
    self.travel = 0

class Enemy_Manager():
  def __init__(self):
    self.enemies = []
    self.travel_mult = 1
  
  def create_enemy(self, img):
    new_enemy = Enemy(img)
    rand_dir = random.randint(0,1)
    if rand_dir == 0:
      new_enemy.travel = 1
    elif rand_dir == 1:
      new_enemy.travel = -1
    # old functionality to spawn enemies all in a row
    # if len(self.enemies) == 0:
    #   new_enemy.x_pos = random.randint(1, 300)
    # else:
    #   new_enemy.x_pos = self.enemies[len(self.enemies) - 1].x_pos + 70
    new_enemy.x_pos = random.randint(1, 735)
    new_enemy.y_pos = random.randint(1, 100)
    self.enemies.append(new_enemy)

  def move_enemy(self):
    for enemy in self.enemies:
      enemy.x_pos += enemy.travel * self.travel_mult
      if enemy.x_pos >= 736:
        enemy.travel = -1
        enemy.y_pos += 32
      elif enemy.x_pos <= 0:
        enemy.travel = 1
        enemy.y_pos += 32

  def game_over(self):
    for enemy in self.enemies:
      enemy.y_pos = 800
      # enemy.travel = 0

