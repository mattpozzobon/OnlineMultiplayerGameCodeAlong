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

screen.fill((60, 63, 65))

topbar = pygame.Surface((resolution[0]-2, 40))
window = pygame.Surface((resolution[0]-2, resolution[1]-41))

topbar.fill((46, 47, 45))
window.fill((100, 100, 100))


angle = 0