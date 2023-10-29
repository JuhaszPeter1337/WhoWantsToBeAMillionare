import pygame
from constants import *
from main import gameover
from shape import *

class Button(Shape):
    def __init__(self, x, y, width, height, outline, type, text = "", pushed = False) -> None:
        super().__init__(x, y, width, height)
        self.outline = outline
        self.type = type
        self.text = text
        self.pushed = pushed

    def draw(self, screen, outline = None, answered = False, correct = False, incorrect = False) -> None:

        if self.outline:
            pygame.draw.rect(screen, self.outline, (self.x - 4, self.y - 4, self.width + 8, self.height + 8), 0)

        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 0)

        if self.text != "": 
            font = pygame.font.SysFont('segoeuisemibold', 26)
            if (answered and not self.pushed and not correct and not incorrect) or (answered and self.pushed and not correct and not incorrect):
                text = font.render(self.text, 1, ORANGE)
            elif answered and self.pushed and correct:
                text = font.render(self.text, 1, GREEN)
            elif answered and self.pushed and incorrect:
                text = font.render(self.text, 1, RED)
            else:
                text = font.render(self.text, 1, WHITE)
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos) -> bool:
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def answer(self) -> None:
        self.outline = ORANGE

    def correct(self) -> None:
        self.outline = GREEN

    def incorrect(self) -> None:
        self.outline = RED

    def update(self, screen, money = None) -> None:
        if self.isOver(pygame.mouse.get_pos()):
            if self.type != "stop":
                if self.outline == WHITE:
                    self.answer()
                    self.pushed = True
            else:
                gameover(screen, money)