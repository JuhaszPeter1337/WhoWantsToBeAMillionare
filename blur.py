import pygame
from constants import BACKGROUND

def blur(screen):
    sf_blur = pygame.transform.gaussian_blur(BACKGROUND,10)
    screen.blit(sf_blur,(0,0,1,1))
    pygame.display.update()