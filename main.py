import sys
import pygame
import random
from file import *
from constants import *
from rectangular import *
import ellipse
from ellipse import *
import button
from screens import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Who wants to be a millionare?")

money = [100, 200, 500, 700, 1000,
        2000, 4000, 8000, 16000, 32000,
        64000, 125000, 250000, 500000, 1000000]

my_money = 0

def find_correct_answer(answer) -> int:
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

def money_calc(money) -> int:
    if money < 1000:
        return 0
    if money < 32000:
        return 1000
    if money < 1000000:
        return 32000

def main():
    running = True

    question_counter = 1
    correct_answers = 0

    screen.blit(BACKGROUND, (0, 0))

    while running:
        length = len(quiz)
        rnd = random.randint(0, length-1)

        objects = [
            Rectangular(415, 533, 350, 75, WHITE, f"Question {question_counter} for {money[correct_answers]}$"),
            Rectangular(100, 610, 1000, 130, WHITE, quiz[rnd].question),
            button.Button(100, 770, 450, 80, WHITE, "A","A, " + quiz[rnd].option_A),
            button.Button(650, 770, 450, 80, WHITE, "B","B, " + quiz[rnd].option_B),
            button.Button(100, 880, 450, 80, WHITE, "C","C, " + quiz[rnd].option_C),
            button.Button(650, 880, 450, 80, WHITE, "D","D, " + quiz[rnd].option_D),
            button.Button(105, 535, 140, 60, BLUE, "stop"),
            Ellipse(779, 535, 100, 65, "fifty"),
            Ellipse(889, 535, 100, 65, "phone"),
            Ellipse(999, 535, 100, 65, "audience")
        ]

        for obj in objects:
            obj.draw(screen)

        screen.blit(STOP, (100, 530))

        screen.blit(FIFTYFIFTY, (780, 530))
        if not ellipse.fifty:
            pygame.draw.line(screen, RED, (779, 535), (877, 600), width=6)
            pygame.draw.line(screen, RED, (879, 535), (779, 595), width=6)
        screen.blit(PAF, (890, 530))
        if not ellipse.phone:
            pygame.draw.line(screen, RED, (889, 535), (989, 595), width=6)
            pygame.draw.line(screen, RED, (989, 535), (889, 595), width=6)
        screen.blit(ATA, (1000, 530))
        if not ellipse.audience:
            pygame.draw.line(screen, RED, (999, 535), (1099, 595), width=6)
            pygame.draw.line(screen, RED, (1099, 535), (999, 595), width=6)

        pygame.display.update()

        answered = False
        while(not answered):
            for event in pygame.event.get():
                global my_money
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for obj in objects:
                        if type(obj) == button.Button:
                            obj.update(screen, my_money)
                        if type(obj) == button.Button and obj.pushed:
                            obj.draw(screen, answered=True)
                            pygame.display.update()
                            pygame.time.delay(3000)
                            pygame.event.pump()
                        if type(obj) == ellipse.Ellipse:
                            obj.update(screen, quiz[rnd])
                    
                    for obj in objects:
                        if type(obj) == button.Button:
                            if obj.pushed:
                                if obj.type == quiz[rnd].correct_answer:
                                    obj.correct()
                                    obj.draw(screen, answered=True, correct=True)
                                    pygame.display.update()
                                    pygame.time.delay(3000)
                                    pygame.event.pump()
                                    if question_counter < 15 and correct_answers < 14:
                                        question_counter = question_counter + 1
                                        correct_answers = correct_answers + 1
                                        my_money = money[correct_answers - 1]
                                        quiz.pop(rnd)
                                        answered = True
                                    else:
                                        winner(screen, money[-1])
                                else:
                                    obj.incorrect()
                                    obj.draw(screen, answered=True, incorrect=True)
                                    number = find_correct_answer(quiz[rnd].correct_answer)
                                    objects[number].outline = ORANGE
                                    objects[number].draw(screen, answered=True, incorrect=False)
                                    pygame.display.update()
                                    pygame.time.delay(5000)
                                    pygame.event.pump()
                                    calculated_money = money_calc(my_money)
                                    gameover(screen, calculated_money)

                elif event.type == pygame.QUIT:
                    root = tkinter.Tk()
                    root.withdraw()
                    answer = tkinter.messagebox.askyesno(title='Exit', message="Are you sure you want to quit?")
                    pygame.event.pump()
                    if answer == True:
                        pygame.quit()
                        sys.exit()

            pygame.event.pump()

if __name__ == "__main__":
    read_from_file()
    menu(screen)
    start(screen)
    main()