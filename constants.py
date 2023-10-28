import pygame

WIDTH, HEIGHT = 1200, 1000

BACKGROUND = pygame.image.load("images/bg.jpg")

FIFTYFIFTY =  pygame.transform.scale(pygame.image.load("images/Classic5050.webp"), (97,72))
PAF = pygame.transform.scale(pygame.image.load("images/ClassicPAF.webp"), (97,72))
ATA = pygame.transform.scale(pygame.image.load("images/ClassicATA.webp"), (97,72))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,128,255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)