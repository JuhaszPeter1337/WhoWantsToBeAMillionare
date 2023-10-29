import pygame
from constants import *
from shape import *

class Rectangular(Shape):
    def __init__(self, x, y, width, height, outline, text = "") -> None:
        super().__init__(x, y, width, height)
        self.outline = outline
        self.text = text

    def draw(self, screen) -> None:

        if self.outline:
            pygame.draw.rect(screen, self.outline, (self.x - 4, self.y - 4, self.width + 8, self.height + 8), 0)

        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 0)

        if self.text != "":
            font = pygame.font.SysFont('segoeuisemibold', 30)
            text = font.render(self.text, 1, WHITE)
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))