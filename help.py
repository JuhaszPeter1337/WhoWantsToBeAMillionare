import random
import pygame
from tkinter import *
from tkinter import messagebox
from typing import List, Dict
from question import *

phone = [
    "I'm not sure but I think\nthe correct answer is...", 
    "I am pretty sure that\nthe answer is...",
    "This question is very\neasy the answer is..."
]

def use_audience(question) -> List[int]:
    if (question.option_A == '-' or question.option_B == '-' or question.option_C == '-' or question.option_D == '-'):
        correct = random.randint(51,99)
        wrong_one = 100 - correct
        return [correct, wrong_one]
    else:
        correct = random.randint(51,70)
        diff = 100 - correct
        wrong_one = random.randint(1, diff - 2)
        diff = 100 - correct - wrong_one
        wrong_two = random.randint(1, diff - 1)
        diff = 100 - correct - wrong_one - wrong_two
        wrong_three = diff
        return [correct, wrong_one, wrong_two, wrong_three]

def checkKey(my_dict, key):
    if key not in my_dict.keys():
        my_dict.update({key: 0})

def evaluate_audience(question, values) -> Dict[str, int]:
    options = ["A", "B", "C", "D"]
    my_dict = {}

    if len(values) == 4:
        my_dict[question.correct_answer] = values[0]
        options.remove(question.correct_answer)
        values.pop(0)

        for _ in range(3):
            answer = random.choice(options)
            number = random.choice(values)
            my_dict[answer] = number
            options.remove(answer)
            values.remove(number)
    else:
        my_dict[question.correct_answer] = values[0]
        options.remove(question.correct_answer)
        
        for option in ["A", "B", "C", "D"]:
            if getattr(question, f"option_{option}") == "-":
                options.remove(option)

        my_dict[options[0]] = values[1]

        checkKey(my_dict, "A")
        checkKey(my_dict, "B")
        checkKey(my_dict, "C")
        checkKey(my_dict, "D")

    return my_dict

def phone_call(question) -> str:
    text = random.choice(phone)
    complete_text = f"""*ringing sound*
Let me hear the question.
*thinking*
{text}"""
    return complete_text, question.correct_answer

def fifty_fifty(question) -> Question:
    options = ["A", "B", "C", "D"]
    option1 = random.choice(options)
    option2 = random.choice(options)
    while option1 == question.correct_answer:
        option1 = random.choice(options)
    while option2 == question.correct_answer or option2 == option1:
        option2 = random.choice(options)
    if option1 == "A" or option2 == "A":
        question.option_A = "-"
    if option1 == "B" or option2 == "B":
        question.option_B = "-"
    if option1 == "C" or option2 == "C":
        question.option_C = "-"
    if option1 == "D" or option2 == "D":
        question.option_D = "-"
    return question
