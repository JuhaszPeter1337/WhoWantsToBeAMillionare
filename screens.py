import pygame
import sys
from rectangular import *
from constants import *
import button

pygame.font.init()

font = pygame.font.Font('freesansbold.ttf', 26)
font2 = pygame.font.Font('freesansbold.ttf', 30)
font3 = pygame.font.Font('freesansbold.ttf', 28)
font4 = pygame.font.Font('freesansbold.ttf', 20)

def count_digits(number) -> int:
    count=0
    while(number > 0):
        number = number // 10
        count=count+1
    return count

def start(screen):
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
    pygame.time.delay(2000)

    screen.blit(second, (620, 100))
    pygame.display.update()
    pygame.time.delay(4000)

    screen.blit(third, (620, 160))
    pygame.display.update()
    pygame.time.delay(4000)

    screen.blit(fourth, (620, 220))
    pygame.display.update()
    pygame.time.delay(4000)
    screen.blit(fifth, (620, 280))

    pygame.display.update()
    pygame.time.delay(4000)

    screen.blit(sixth, (820, 340))
    pygame.display.update()
    pygame.time.delay(5000)

    screen.blit(seventh, (620, 400))
    pygame.display.update()
    pygame.time.delay(5000)
    
    screen.blit(eighth, (820, 460))
    pygame.display.update()
    pygame.time.delay(2000)

def gameover(screen, money):
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

def winner(screen, money):
    screen.blit(MAN, (0, 0))

    win = f"The game has ended. You win!"
    money_text = f"You won {money}$."
    thanking_text = "Thank you for playing!"
    timing_text = "The game is about to quit in 5 seconds."
    ending_text = f"See you soon, bye!"

    end_screen = Rectangular(600, 20, 580, 500, WHITE)
    end_screen.draw(screen)

    first = font3.render(win, False, WHITE, BLACK)
    second=font3.render(money_text, False, WHITE, BLACK)
    third=font3.render(thanking_text, False, WHITE, BLACK)
    fourth=font3.render(timing_text, False, WHITE, BLACK)
    fifth=font3.render(ending_text, False, WHITE, BLACK)

    screen.blit(first, (680, 100))
    pygame.display.update()
    pygame.time.delay(3000)

    screen.blit(second, (765, 175))
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

def description(screen):
    screen.blit(MAN, (0, 0))

    text = "The goal is to correctly answer 15 consecutive questions"
    text2 = "with each question having a higher prize value than the"
    text3 = "previous one, culminating in a grand prize of one million"
    text4 = "currency units."

    text5 = "Choose from letters A, B, C or D to answer the question."
    
    text6 = 'Don\'t forget you have 3 jokers. "Ask the Audience",'
    text7 = 'where the studio audience votes on the answer.'
    text8 = '"Phone-a-Friend", allowing contestants to make a call for'
    text9 = 'help with the answer. "50:50", which removes two'
    text10 = 'incorrect answers, leaving the correct answer and'
    text11 = 'one remaining answer.'

    text12 = "You can stop and finish the game whenever you want to."

    start_screen = Rectangular(600, 20, 580, 500, WHITE)
    start_screen.draw(screen)

    first=font4.render(text, False, WHITE, BLACK)
    second=font4.render(text2, False, WHITE, BLACK)
    third=font4.render(text3, False, WHITE, BLACK)
    fourth=font4.render(text4, False, WHITE, BLACK)

    fifth=font4.render(text5, False, WHITE, BLACK)
    sixth=font4.render(text6, False, WHITE, BLACK)

    seventh=font4.render(text7, False, WHITE, BLACK)
    eighth=font4.render(text8, False, WHITE, BLACK)
    nineth=font4.render(text9, False, WHITE, BLACK)
    tenth=font4.render(text10, False, WHITE, BLACK)
    eleventh=font4.render(text11, False, WHITE, BLACK)

    twelfth=font4.render(text12, False, WHITE, BLACK)

    screen.blit(first, (605, 40))
    pygame.display.update()
    pygame.time.delay(2000)

    screen.blit(second, (605, 80))
    pygame.display.update()
    pygame.time.delay(2000)

    screen.blit(third, (605, 120))
    pygame.display.update()
    pygame.time.delay(2000)

    screen.blit(fourth, (605, 160))
    pygame.display.update()
    pygame.time.delay(2000)

    screen.blit(fifth, (605, 200))
    pygame.display.update()
    pygame.time.delay(2000)

    screen.blit(sixth, (605, 240))
    pygame.display.update()
    pygame.time.delay(2000)

    screen.blit(seventh, (605, 280))
    pygame.display.update()
    pygame.time.delay(2000)

    screen.blit(eighth, (605, 320))
    pygame.display.update()
    pygame.time.delay(2000)

    screen.blit(nineth, (605, 360))
    pygame.display.update()
    pygame.time.delay(2000)

    screen.blit(tenth, (605, 400))
    pygame.display.update()
    pygame.time.delay(2000)

    screen.blit(eleventh, (605, 440))
    pygame.display.update()
    pygame.time.delay(2000)

    screen.blit(twelfth, (605, 480))
    pygame.display.update()
    pygame.time.delay(10000)


def menu(screen):
    running = True

    screen.blit(BACKGROUND, (0, 0))

    while running:
        objects = [
            button.Button(415, 550, 400, 115, WHITE, "play","PLAY"),
            button.Button(415, 700, 400, 115, WHITE, "description","DESCRIPTION"),
            button.Button(415, 855, 400, 115, WHITE, "quit","QUIT")
        ]

        for obj in objects:
            obj.draw(screen)

        pygame.display.update()

        pushed = False
        while(not pushed):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for obj in objects:
                        value = obj.isOver(pygame.mouse.get_pos())
                        if (obj.type == "play"):
                            if (value):
                                pushed = True
                                running = False
                        elif (value and obj.type == "description"):
                            description(screen)
                            pushed = True
                            running = False
                        elif (value and obj.type == "quit"):
                            pygame.quit()
                            sys.exit()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    pygame.event.pump()