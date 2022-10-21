import pygame
from pygame.locals import *

running = True
fps = 60
resolution = (1200, 800)
flags = HWSURFACE | DOUBLEBUF | NOFRAME

pygame.init()
screen_size = pygame.display.Info()
screen = pygame.display.set_mode(resolution, flags)
clock = pygame.time.Clock()

screen.fill((120, 120, 120))