import pygame

class player(object):
    def moveLeft(self):
        ev = pygame.event.Event(pygame.KEYDOWN)
        ev.key = pygame.K_LEFT
        pygame.event.post(ev)
    def rotate(self):
        ev = pygame.event.Event(pygame.KEYDOWN)
        ev.key = pygame.K_SPACE
        pygame.event.post(ev)
