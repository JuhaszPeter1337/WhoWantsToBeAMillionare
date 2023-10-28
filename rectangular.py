import pygame
from constants import *

class Rectangular():
    def __init__(self, x, y, width, height, outline, text = "") -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.outline = outline

    def draw(self, screen):

        if self.outline:
            pygame.draw.rect(screen, self.outline, (self.x - 4, self.y - 4, self.width + 8, self.height + 8), 0)

        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 0)

        if self.text != "":
            font = pygame.font.SysFont('segoeuisemibold', 30)
            text = font.render(self.text, 1, WHITE)
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))