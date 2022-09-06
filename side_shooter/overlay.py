import pygame

class Overlay:
  def __init__(self, player):
    self.player = player
    self.display_surface = pygame.display.get_surface()
    self.health_surf = pygame.image.load('./graphics/health.png').convert_alpha()

  def display(self):
    for hp in range(self.player.health):
      x_pos = hp * self.health_surf.get_width()
      self.display_surface.blit(self.health_surf,(x_pos,10))

