import pygame
from pygame.locals import *


class Environment:
    def __init__(self):
        self.bg_surf = pygame.display.set_mode((854, 480), pygame.HWSURFACE)
