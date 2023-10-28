import sys
import pygame
import random
from file import *
from constants import *
from rectangular import *
from ellipse import *
from button import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Who wants to be a millionare?")

money = [100, 200, 500, 700, 1000,
        2000, 4000, 8000, 16000, 32000,
        64000, 125000, 250000, 500000, 1000000]

font = pygame.font.Font('freesansbold.ttf', 26)

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
        length = len(quiz)
        rnd = random.randint(0, length-1)

        objects = [
            Rectangular(425, 533, 340, 75, WHITE, f"Question {question_counter} for {money[correct_answers]}$"),
            Rectangular(100, 610, 1000, 130, WHITE, quiz[rnd].question),
            Button(100, 770, 450, 80, WHITE, "A","A, " + quiz[rnd].option_A),
            Button(650, 770, 450, 80, WHITE, "B","B, " + quiz[rnd].option_B),
            Button(100, 880, 450, 80, WHITE, "C","C, " + quiz[rnd].option_C),
            Button(650, 880, 450, 80, WHITE, "D","D, " + quiz[rnd].option_D),
            Ellipse(779, 535, 100, 65, "fifty"),
            Ellipse(889, 535, 100, 65, "phone"),
            Ellipse(999, 535, 100, 65, "audience")
        ]

        for obj in objects:
            obj.draw(screen)

        screen.blit(FIFTYFIFTY, (780, 530))
        if not fifty:
            pygame.draw.line(screen, RED, (779, 535), (877, 600), width=6)
            pygame.draw.line(screen, RED, (879, 535), (779, 595), width=6)
        screen.blit(PAF, (890, 530))
        if not phone:
            pygame.draw.line(screen, RED, (889, 535), (989, 595), width=6)
            pygame.draw.line(screen, RED, (989, 535), (889, 595), width=6)
        screen.blit(ATA, (1000, 530))
        if not audience:
            pygame.draw.line(screen, RED, (999, 535), (1099, 595), width=6)
            pygame.draw.line(screen, RED, (1099, 535), (999, 595), width=6)

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
                        if type(button) == Ellipse:
                            button.update(screen)
                    
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