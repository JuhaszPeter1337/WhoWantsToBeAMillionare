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

answer = None

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
    
def wait_for_answer():
    global answer
    root = tkinter.Tk()
    root.withdraw()
    message = tkinter.messagebox.askyesno(title='Exit', message="Are you sure you want to quit?")
    answer = message
    root.destroy()
    root.mainloop()

def draw(objects):
    screen.blit(BACKGROUND, (0, 0))

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

def main():
    running = True

    global answer

    question_counter = 1
    correct_answers = 0

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

        draw(objects)
        pygame.display.update()

        answered = False
        while(not answered):
            for event in pygame.event.get():
                global my_money
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for obj in objects:
                        if type(obj) == button.Button and obj.enabled:
                            obj.update(screen, my_money)
                        if type(obj) == button.Button and obj.pushed and obj.enabled:
                            obj.draw(screen, answered=True)
                            pygame.display.update()
                            pygame.time.delay(3000)
                            pygame.event.pump()
                        if type(obj) == ellipse.Ellipse:
                            if obj.type == "fifty":
                                q = obj.update(screen, quiz[rnd])
                                if q != None:
                                    objects[2].text = "A, " + q[0]
                                    if q[0] == "-":
                                        objects[2].enabled = False
                                    objects[3].text = "B, " + q[1]
                                    if q[1] == "-":
                                        objects[3].enabled = False
                                    objects[4].text = "C, " + q[2]
                                    if q[2] == "-":
                                        objects[4].enabled = False
                                    objects[5].text = "D, " + q[3]
                                    if q[3] == "-":
                                        objects[5].enabled = False
                            elif obj.type == "audience":
                                obj.update(screen, quiz[rnd])
                                draw(objects)
                            else:
                                obj.update(screen, quiz[rnd])

                    for obj in objects:
                        if type(obj) == button.Button:
                            if obj.pushed and obj.enabled:
                                if obj.type == quiz[rnd].correct_answer:
                                    obj.correct()
                                    obj.draw(screen, answered=True, correct=True)
                                    pygame.display.update()
                                    pygame.time.delay(3000)
                                    pygame.event.pump()
                                    if question_counter < 15 and correct_answers < 14:
                                        question_counter += 1
                                        correct_answers += 1
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
                    exit(screen)
                    draw(objects)

            pygame.event.pump()

if __name__ == "__main__":
    read_from_file()
    menu(screen)
    start(screen)
    main()