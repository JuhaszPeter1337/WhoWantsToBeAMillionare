import pygame

WIDTH, HEIGHT = 1200, 1000

BACKGROUND = pygame.image.load("images/bg.jpg")
MAN = pygame.image.load("images/person.png")
AUDIENCE = pygame.transform.scale(pygame.image.load("images/audience.png"), (WIDTH, HEIGHT))

FIFTYFIFTY =  pygame.transform.scale(pygame.image.load("images/Classic5050.webp"), (97,72))
PAF = pygame.transform.scale(pygame.image.load("images/ClassicPAF.webp"), (97,72))
ATA = pygame.transform.scale(pygame.image.load("images/ClassicATA.webp"), (97,72))

STOP = pygame.transform.scale(pygame.image.load("images/stop.png"), (150,70))

QUIT = pygame.image.load("images/quit.JPG")

STOP_GAME = pygame.image.load("images/stop_game.JPG")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,128,255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)