import pygame
import sys
from rectangular import *
from constants import *
import button
import tkinter

pygame.font.init()

fonts = [
    pygame.font.Font('freesansbold.ttf', 20),
    pygame.font.Font('freesansbold.ttf', 26),
    pygame.font.Font('freesansbold.ttf', 28),
    pygame.font.Font('freesansbold.ttf', 40)
]

def count_digits(number) -> int:
    count=0
    while(number > 0):
        number = number // 10
        count=count+1
    return count

def create_text(screen, text, pos, font) -> None:
    if text == "Game over!" or text == "The game has ended. You won!":
        font=fonts[font].render(text, False, RED, BLACK)
    else:
        font=fonts[font].render(text, False, WHITE, BLACK)
    screen.blit(font, (pos[0], pos[1]))
    pygame.display.update()
    pygame.time.delay(2000)

def start(screen) -> None:
    screen.blit(MAN, (0, 0))

    texts = [
        "Ladies and Gentlemen!",
        'Welcome to a new round of "Who wants to',
        'be a millionare!". We have a new candidate',
        "here. Welcome! Everyone, a big round of",
        "applause for our candidate.",
        "*applause*",
        "The game is about to begin in 5 seconds.",
        "Good luck!"
    ]

    start_screen = Rectangular(600, 20, 580, 500, WHITE)
    start_screen.draw(screen)

    for i in range(0,8):
        if i == 0:
            create_text(screen, texts[i], (620, 40), 3)
        else:
            create_text(screen, texts[i], (620, 50 + (i * 60)), 1)

    pygame.time.delay(2000)

def gameover(screen, money) -> None:
    screen.blit(MAN, (0, 0))

    texts = [
        "Game over!",
        f"You won {money}$.",
        "Thank you for playing!",
        "The game is about to quit in 5 seconds.",
        "See you soon, bye!"
    ]

    c = count_digits(money)

    end_screen = Rectangular(600, 20, 580, 500, WHITE)
    end_screen.draw(screen)

    create_text(screen, texts[0], (765, 90), 3)
    create_text(screen, texts[1], (800 - c * 7, 175), 2)
    create_text(screen, texts[2], (730, 250), 2)
    create_text(screen, texts[3], (620, 325), 2)
    create_text(screen, texts[4], (750, 400), 2)

    pygame.time.delay(2000)

    pygame.quit()
    sys.exit()

def winner(screen, money) -> None:
    screen.blit(MAN, (0, 0))

    texts = [
        "The game has ended. You won!",
        f"Your prize is {money}$.",
        "Thank you for playing!",
        "The game is about to quit in 5 seconds.",
        "See you soon, bye!"
    ]

    end_screen = Rectangular(600, 20, 580, 500, WHITE)
    end_screen.draw(screen)

    create_text(screen, texts[0], (680, 100), 2)
    create_text(screen, texts[1], (723, 175), 2)
    create_text(screen, texts[2], (730, 250), 2)
    create_text(screen, texts[3], (620, 325), 2)
    create_text(screen, texts[4], (750, 400), 2)

    pygame.time.delay(2000)

    pygame.quit()
    sys.exit()

def description(screen) -> None:
    screen.blit(MAN, (0, 0))

    texts = [
        "The goal is to correctly answer 15 consecutive questions",
        "with each question having a higher prize value than the",
        "previous one, culminating in a grand prize of one million",
        "currency units.",
        "Choose from letters A, B, C or D to answer the question.",
        'Don\'t forget you have 3 jokers. "Ask the Audience",',
        'where the studio audience votes on the answer.',
        '"Phone-a-Friend", allowing contestants to make a call for',
        'help with the answer. "50:50", which removes two',
        'incorrect answers, leaving the correct answer and',
        'one remaining answer.',
        "You can stop and finish the game whenever you want to."
    ]

    start_screen = Rectangular(600, 20, 580, 500, WHITE)
    start_screen.draw(screen)

    for i in range(0,12):
        create_text(screen, texts[i], (605, (i + 1) * 40), 0)

    pygame.time.delay(8000)


def menu(screen) -> None:
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
                        if (value and obj.type == "play"):
                            pushed = True
                            running = False
                        elif (value and obj.type == "description"):
                            description(screen)
                            pushed = True
                            running = False
                        elif (value and obj.type == "quit"):
                            root = tkinter.Tk()
                            root.withdraw()
                            answer = tkinter.messagebox.askyesno(title='Exit', message="Are you sure you want to quit?")
                            if answer == True:
                                pygame.quit()
                                sys.exit()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    pygame.event.pump()