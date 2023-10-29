import sys
import pygame
import random
from file import *
from constants import *
from rectangular import *
import ellipse
from ellipse import *
from button import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Who wants to be a millionare?")

money = [100, 200, 500, 700, 1000,
        2000, 4000, 8000, 16000, 32000,
        64000, 125000, 250000, 500000, 1000000]

my_money = 0

font = pygame.font.Font('freesansbold.ttf', 26)
font2 = pygame.font.Font('freesansbold.ttf', 30)
font3 = pygame.font.Font('freesansbold.ttf', 28)

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

def money_calc(money) -> (int):
    if money < 1000:
        return 0
    if money < 32000:
        return 1000
    if money < 1000000:
        return 32000
    
def count_digits(number) -> int:
    count=0
    while(number > 0):
        number = number // 10
        count=count+1
    return count

def gameover(money):
    screen.blit(MAN, (0, 0))

    game_over = f"Game over!"
    money_text = f"You won {money}$."
    thanking_text = "Thank you for playing!"
    timing_text = "The game is about to quit in 5 seconds."
    ending_text = f"See you soon, bye!"

    c = count_digits(money)

    end_screen = Rectangular(600, 20, 580, 500, WHITE)
    end_screen.draw(screen)

    first = font3.render(game_over, False, WHITE, BLACK)
    second=font3.render(money_text, False, WHITE, BLACK)
    third=font3.render(thanking_text, False, WHITE, BLACK)
    fourth=font3.render(timing_text, False, WHITE, BLACK)
    fifth=font3.render(ending_text, False, WHITE, BLACK)

    screen.blit(first, (800, 100))
    pygame.display.update()
    pygame.time.delay(3000)

    screen.blit(second, (800 - c * 5, 175))
    pygame.display.update()
    pygame.time.delay(3000)

    screen.blit(third, (730, 250))
    pygame.display.update()
    pygame.time.delay(3000)

    screen.blit(fourth, (620, 325))
    pygame.display.update()
    pygame.time.delay(5000)

    screen.blit(fifth, (750, 400))
    pygame.display.update()
    pygame.time.delay(2000)

    pygame.quit()
    sys.exit()

def start():
    screen.blit(MAN, (0, 0))

    text = "Ladies and Gentlemen!"
    text1 = 'Welcome to a new round of "Who wants to'
    text2 = 'be a millionare!". We have a new candidate'
    text3 = "here. Welcome! Everyone, a big round of"
    text4 = "applause for our candidate."
    text5 = "*applause*"
    text6 = "The game is about to begin in 5 seconds."
    text7 = "Good luck!"

    start_screen = Rectangular(600, 20, 580, 500, WHITE)
    start_screen.draw(screen)

    first=font2.render(text, False, WHITE, BLACK)
    second=font.render(text1, False, WHITE, BLACK)
    third=font.render(text2, False, WHITE, BLACK)
    fourth=font.render(text3, False, WHITE, BLACK)
    fifth=font.render(text4, False, WHITE, BLACK)
    sixth=font.render(text5, False, WHITE, BLACK)
    seventh=font.render(text6, False, WHITE, BLACK)
    eighth=font.render(text7, False, WHITE, BLACK)

    screen.blit(first, (730, 40))
    pygame.display.update()
    pygame.time.delay(3000)

    screen.blit(second, (620, 100))
    screen.blit(third, (620, 160))
    screen.blit(fourth, (620, 220))
    screen.blit(fifth, (620, 280))
    pygame.display.update()
    pygame.time.delay(8000)

    screen.blit(sixth, (820, 340))
    pygame.display.update()
    pygame.time.delay(3000)

    screen.blit(seventh, (620, 400))
    pygame.display.update()
    pygame.time.delay(5000)
    
    screen.blit(eighth, (820, 460))
    pygame.display.update()
    pygame.time.delay(2000)

def main():
    running = True

    question_counter = 1
    correct_answers = 0

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
            Button(105, 535, 140, 60, BLUE, "stop"),
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
                        if type(obj) == Button:
                            obj.update(my_money)
                        if type(obj) == Button and obj.pushed:
                            obj.draw(screen, answered=True)
                            pygame.display.update()
                            pygame.time.delay(3000)
                        if type(obj) == ellipse.Ellipse:
                            obj.update(screen)
                    
                    for obj in objects:
                        if type(obj) == Button:
                            if obj.pushed:
                                if obj.type == quiz[rnd].correct_answer:
                                    obj.correct()
                                    obj.draw(screen, answered=True, correct=True)
                                    pygame.display.update()
                                    pygame.time.delay(3000)
                                    question_counter = question_counter + 1 if question_counter < 15 else 1
                                    correct_answers = correct_answers + 1 if correct_answers < 14 else 0
                                    my_money = money[correct_answers - 1]
                                    quiz.pop(rnd)
                                    answered = True
                                else:
                                    obj.incorrect()
                                    obj.draw(screen, answered=True, incorrect=True)
                                    number = find_correct_answer(quiz[rnd].correct_answer)
                                    objects[number].outline = ORANGE
                                    objects[number].draw(screen, answered=True, incorrect=False)
                                    pygame.display.update()
                                    pygame.time.delay(5000)
                                    calculated_money = money_calc(my_money)
                                    gameover(calculated_money)

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.event.pump()

if __name__ == "__main__":
    read_from_file()
    start()
    main()