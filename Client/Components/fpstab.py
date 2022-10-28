import math
import pygame
from Client.Components.basecomponent import BaseComponent

class FpsTab(BaseComponent):
    def __init__(self, window, x, y, w, h):
        BaseComponent.__init__(self, window, x, y, w, h)
        self.image = pygame.image.load("Client/Assets/Image/fps.png")
        self.image = pygame.transform.scale(self.image, self.getsize())
        self.arr = [-3.6, 0.4]

    def render(self, fps):
        normalise = (fps - 0) / (60 - 0)
        denormalize = normalise * (self.arr[1] - self.arr[0]) + self.arr[0]

        x = math.cos(denormalize) * (self.w/3) + (self.w/2)
        y = math.sin(denormalize) * (self.h/3) + (self.h/2)

        self.surface.fill((120, 120, 120))
        self.surface.blit(self.image, (0, 0))
        pygame.draw.line(self.surface, self.getcolour(fps), (self.w/2, (self.h/2)), (x, y), width=2)

        self.window.blit(self.surface, self.getpos())

    def getcolour(self, fps):
        if fps < 20:
            return 255, 0, 0
        if fps < 40:
            return 255, 255, 0
        else:
            return 0, 255, 0
