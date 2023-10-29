import pygame
import sys
from rectangular import *
from constants import *

pygame.font.init()

font = pygame.font.Font('freesansbold.ttf', 26)
font2 = pygame.font.Font('freesansbold.ttf', 30)
font3 = pygame.font.Font('freesansbold.ttf', 28)

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

def loading_screen(screen):
    screen.blit(BACKGROUND, (0, 0))
    pygame.display.update()
    pygame.time.delay(5000)