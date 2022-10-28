import pygame


class BaseComponent:
    def __init__(self, window, x, y, w, h):
        self.window = window
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.surface = pygame.Surface(self.getsize(), pygame.SRCALPHA)

    def getsize(self):
        return self.w, self.h

    def getpos(self):
        return self.x, self.y