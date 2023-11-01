import pygame
import sys
from rectangular import *
from constants import *
import button
import tkinter
from tkinter.simpledialog import askstring
import threading

# Pygame has no opportunity to handle the messages it gets from your operation system. To avoid that, you should call pygame.event.pump()
# should have root.mainloop() in there somewhere, so the gui will listen to os events (like the CloseWindow event).

pygame.font.init()

name = None

answer = None

fonts = [
    pygame.font.Font('freesansbold.ttf', 20),
    pygame.font.Font('freesansbold.ttf', 26),
    pygame.font.Font('freesansbold.ttf', 28),
    pygame.font.Font('freesansbold.ttf', 40)
]

def meets_name_criteria(your_name) -> bool:
    max_len = 16
    restricted_chars = {'`','~','!','@','#','$','%','^','&','*','(',')','_','-',
               '+','=','{','[','}','}','|','\\',':',';','"',"'",'<',',','>','.',
               '?','/'}
    if your_name is not None and your_name != "":
        if (len(your_name) < max_len and not any((char in your_name) for char in restricted_chars)):
            return True
        return False
    else:
        return False

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
    pygame.event.pump()

def wait_for_answer():
    global answer
    root = tkinter.Tk()
    root.withdraw()
    message = tkinter.messagebox.askyesno(title='Exit', message="Are you sure you want to quit?")
    answer = message
    root.mainloop()

def menu(screen) -> None:
    running = True

    global answer

    screen.blit(BACKGROUND, (0, 0))

    while running:
        objects = [
            button.Button(315, 550, 600, 115, WHITE, "play","PLAY"),
            button.Button(315, 700, 600, 115, WHITE, "description","DESCRIPTION"),
            button.Button(315, 850, 600, 115, WHITE, "quit","QUIT")
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
                            answer = None
                            threading.Thread(target=wait_for_answer, daemon=True).start()
                            while (answer != True or answer != False):
                                pygame.event.pump()
                                if answer == True:
                                    pygame.quit()
                                    sys.exit()
                                if answer == False:
                                    break

                if event.type == pygame.QUIT:
                    answer = None
                    threading.Thread(target=wait_for_answer, daemon=True).start()
                    while (answer != True or answer != False):
                        pygame.event.pump()
                        if answer == True:
                            pygame.quit()
                            sys.exit()
                        if answer == False:
                            break

    pygame.event.pump()

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

    for i in range(12):
        create_text(screen, texts[i], (605, (i + 1) * 40), 0)

    pygame.time.delay(8000)
    pygame.event.pump()

    menu(screen)


def start(screen) -> None:
    screen.blit(MAN, (0, 0))

    texts = [
        "Ladies and Gentlemen!",
        'Welcome to a new round of "Who wants to',
        'be a millionare!". We have a new candidate.'
    ]

    start_screen = Rectangular(600, 20, 580, 500, WHITE)
    start_screen.draw(screen)

    for i in range(3):
        if i == 0:
            create_text(screen, texts[i], (620, 40), 3)
        else:
            create_text(screen, texts[i], (620, 50 + (i * 60)), 1)
    global name
    my_w = tkinter.Tk()
    my_w.withdraw()
    name = askstring(title='Your name', prompt='What is your name? (max 16 character long and no special characters)')
    pygame.event.pump()
    crit = meets_name_criteria(name)
    while not crit:
        name = askstring(title='Your name', prompt='Please enter correct name! (max 16 character long and no special characters)')
        new_name = meets_name_criteria(name)
        if new_name:
            crit = True

    texts = [
        f"Welcome {name}!",
        "Everyone, a big round of applause.",
        "*applause*",
        "The game is about to begin in 5 seconds.",
        "Good luck!"
    ]
    for i in range(5):
        create_text(screen, texts[i], (620, 50 + ((i + 3) * 60)), 1)

    pygame.time.delay(2000)
    pygame.event.pump()

def gameover(screen, money) -> None:
    screen.blit(MAN, (0, 0))

    texts = [
        "Game over!",
        f"You won {money}$.",
        "Thank you for playing!",
        "The game is about to quit in 5 seconds.",
        f"See you soon, bye {name}!"
    ]

    c = count_digits(money)

    end_screen = Rectangular(600, 20, 580, 500, WHITE)
    end_screen.draw(screen)

    create_text(screen, texts[0], (766, 90), 3)
    create_text(screen, texts[1], (800 - c * 7, 175), 2)
    create_text(screen, texts[2], (730, 250), 2)
    create_text(screen, texts[3], (620, 325), 2)
    create_text(screen, texts[4], (750 - len(name) * 7 , 400), 2)

    pygame.time.delay(2000)
    pygame.event.pump()

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
    pygame.event.pump()

    pygame.quit()
    sys.exit()