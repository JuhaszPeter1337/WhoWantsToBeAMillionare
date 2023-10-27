import sys
import pygame
import random
from file import *

pygame.init()

WIDTH, HEIGHT = 1200, 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Who wants to be a millionare?")

BACKGROUND = pygame.image.load("bg.jpg")

Fiftyfifty =  pygame.transform.scale(pygame.image.load("Classic5050.webp"), (97,72))
PAF = pygame.transform.scale(pygame.image.load("ClassicPAF.webp"), (97,72))
ATA = pygame.transform.scale(pygame.image.load("ClassicATA.webp"), (97,72))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)

money = [100, 200, 500, 700, 1000,
        2000, 4000, 8000, 16000, 32000,
        64000, 125000, 250000, 500000, 1000000]

font = pygame.font.Font('freesansbold.ttf', 26) 

class Rectangular():
    def __init__(self, x, y, width, height, outline, text = "") -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.outline = outline

    def draw(self, screen, outline = None):

        if self.outline:
            pygame.draw.rect(screen, self.outline, (self.x - 4, self.y - 4, self.width + 8, self.height + 8), 0)

        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 0)

        if self.text != "":
            font = pygame.font.SysFont('segoeuisemibold', 30)
            text = font.render(self.text, 1, WHITE)
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

class Button():
    def __init__(self, x, y, width, height, outline, type, text = "", pushed = False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.outline = outline
        self.type = type
        self.pushed = pushed

    def draw(self, screen, outline = None, answered = False, correct = False, incorrect = False):

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

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def answer(self):
        self.outline = ORANGE

    def correct(self):
        self.outline = GREEN

    def incorrect(self):
        self.outline = RED

    def update(self):
        if self.isOver(pygame.mouse.get_pos()):
            if self.outline == WHITE:
                self.answer()
                self.pushed = True

def find_correct_answer(answer):
    number = None
    if answer == "A":
        number = 2
    elif answer == "B":
        number = 3
    elif answer == "C":
        number = 4
    else:
        number = 5
    return number

def gameover():
    pygame.quit()
    sys.exit()

def main():
    running = True

    question_counter = 1
    correct_answers = 0
    my_money = 0

    screen.blit(BACKGROUND, (0, 0))

    while running:
        screen.blit(Fiftyfifty, (780, 530))
        screen.blit(PAF, (890, 530))
        screen.blit(ATA, (1000, 530))

        length = len(quiz)
        rnd = random.randint(0, length-1)

        objects = [
            Rectangular(425, 533, 340, 75, WHITE, f"Question {question_counter} for {money[correct_answers]}$"),
            Rectangular(100, 610, 1000, 130, WHITE, quiz[rnd].question),
            Button(100, 770, 450, 80, WHITE, "A","A, " + quiz[rnd].option_A),
            Button(650, 770, 450, 80, WHITE, "B","B, " + quiz[rnd].option_B),
            Button(100, 880, 450, 80, WHITE, "C","C, " + quiz[rnd].option_C),
            Button(650, 880, 450, 80, WHITE, "D","D, " + quiz[rnd].option_D)
        ]

        for obj in objects:
            obj.draw(screen)

        pygame.display.update()

        answered = False
        while(not answered):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in objects:
                        if type(button) == Button:
                            button.update()
                        if type(button) == Button and button.pushed:
                            button.draw(screen, answered=True)
                            pygame.display.update()
                            pygame.time.delay(3000)
                    
                    for button in objects:
                        if type(button) == Button:
                            if button.pushed:
                                if button.type == quiz[rnd].correct_answer:
                                    button.correct()
                                    button.draw(screen, answered=True, correct=True)
                                    pygame.display.update()
                                    pygame.time.delay(3000)
                                    question_counter = question_counter + 1 if question_counter < 15 else 1
                                    correct_answers = correct_answers + 1 if correct_answers < 14 else 0
                                    quiz.pop(rnd)
                                    answered = True
                                else:
                                    button.incorrect()
                                    button.draw(screen, answered=True, incorrect=True)
                                    number = find_correct_answer(quiz[rnd].correct_answer)
                                    objects[number].outline = ORANGE
                                    objects[number].draw(screen, answered=True, incorrect=False)
                                    pygame.display.update()
                                    pygame.time.delay(5000)
                                    gameover()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.event.pump()

if __name__ == "__main__":
    read_from_file()
    main()