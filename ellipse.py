import pygame
import math
from constants import *
from shape import *
from help import *

audience, phone, fifty = True, True, True

class Ellipse(Shape):
    def __init__(self, x, y, width, height, type) -> None:
        super().__init__(x, y, width, height)
        self.type = type

    def draw(self, screen) -> None:
        pygame.draw.ellipse(screen, BLUE, (self.x, self.y, self.width, self.height))

    #(x - h)^2 / a^2 + (y - k)^2 / b^2 <= 1
    def isOver(self, pos) -> float:
        point_x, point_y = pos[0], pos[1]
        ellipse_center_x, ellipse_center_y = self.x + self.width / 2, self.y + self.height / 2
        half_width, half_height = self.width / 2, self.height / 2
        p = ((math.pow((point_x - ellipse_center_x), 2) / math.pow(half_width, 2)) + (math.pow((point_y - ellipse_center_y), 2) / math.pow(half_height, 2)))
        return p

    def update(self, screen, question) -> None:
        global fifty, phone, audience
        collision = self.isOver(pygame.mouse.get_pos())
        if collision <= 1:
            if self.type == "fifty" and fifty:
                fifty = False
                pygame.draw.line(screen, RED, (779, 535), (879, 595), width=6)
                pygame.draw.line(screen, RED, (879, 535), (779, 595), width=6)
                pygame.display.update()
            elif self.type == "phone" and phone:
                phone = False
                correct_answer = phone_call(question)
                popup(correct_answer)
                pygame.draw.line(screen, RED, (889, 535), (989, 595), width=6)
                pygame.draw.line(screen, RED, (989, 535), (889, 595), width=6)
                pygame.display.update()
            elif self.type == "audience" and audience:
                audience = False
                values = use_audience(question)
                evaulate = evaluate_audience(question, values)
                diagram(evaulate)
                pygame.draw.line(screen, RED, (999, 535), (1099, 595), width=6)
                pygame.draw.line(screen, RED, (1099, 535), (999, 595), width=6)
                pygame.display.update()