import pygame
import random
import time
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

class Button():
    def __init__(self, x, y, width, height, outline, type, text = ""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.outline = outline
        self.type = type

    def draw(self, screen, outline = None, answered = None, correct = None, incorrect = None):

        if self.outline:
            pygame.draw.rect(screen, self.outline, (self.x - 4, self.y - 4, self.width + 8, self.height + 8), 0)

        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 0)

        if self.text != "":
            if self.type == "question":
                font = pygame.font.SysFont('segoeuisemibold', 30)
                text = font.render(self.text, 1, WHITE)
                screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
            else:    
                font = pygame.font.SysFont('segoeuisemibold', 26)
                if answered:
                    text = font.render(self.text, 1, ORANGE)
                elif correct:
                    text = font.render(self.text, 1, GREEN)
                elif incorrect:
                    text = font.render(self.text, 1, RED)
                else:
                    text = font.render(self.text, 1, WHITE)
                screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def answer(self):
        self.outline = ORANGE

    def correct(self):
        self.outline = GREEN

    def incorrect(self):
        self.outline = RED

def main():
    running = True

    question_counter = 1
    correct_answers = 0
    my_money = 0

    screen.blit(BACKGROUND, (0, 0))

    while running:
        mouse = pygame.mouse.get_pos() 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 200 <= mouse[0] <= 220 and 400 <= mouse[1] <= 500: 
                    print("Button A pushed")

            if event.type == pygame.QUIT:
                running = False

        screen.blit(Fiftyfifty, (780, 530))
        screen.blit(PAF, (890, 530))
        screen.blit(ATA, (1000, 530))

        length = len(quiz)
        rnd = random.randint(0, length-1)

        objects = [
            Button(435, 533, 330, 75, WHITE, "number", f"Question {question_counter} for {money[correct_answers]}$"),
            Button(100, 610, 1000, 130, WHITE, "question", quiz[rnd].question),
            Button(100, 770, 450, 80, WHITE, "option","A, " + quiz[rnd].option_A),
            Button(650, 770, 450, 80, WHITE, "option","B, " + quiz[rnd].option_B),
            Button(100, 880, 450, 80, WHITE, "option","C, " + quiz[rnd].option_C),
            Button(650, 880, 450, 80, WHITE, "option","D, " + quiz[rnd].option_D)
        ]

        for obj in objects:
            obj.draw(screen)

        pygame.display.update()

        answered = False
        while(not answered):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    question_counter = question_counter + 1 if question_counter < 15 else 1
                    correct_answers = correct_answers + 1 if correct_answers < 14 else 0
                    objects[2].answer()
                    objects[2].draw(screen, answered=True)
                    pygame.display.update()
                    time.sleep(3)
                    objects[2].correct()
                    objects[2].draw(screen, correct=True)
                    pygame.display.update()
                    time.sleep(3)
                    objects[2].incorrect()
                    objects[2].draw(screen, incorrect=True)
                    pygame.display.update()
                    time.sleep(3)
                    answered = True

                elif event.type == pygame.QUIT:
                    pygame.quit()

    pygame.quit()

if __name__ == "__main__":
    read_from_file()
    main()