import random
from tkinter import *
from tkinter import messagebox

phone = [
    "I'm not sure but I think the correct answer is...", 
    "I am pretty sure that the answer is...", 
    "This question is very easy, the correct answer is..."
]

def popup(text):
    top = Tk() # to hide the main window
    top.wm_withdraw()
    messagebox.showinfo(title='Phone', message=text)

def phone_call(question) -> str:
    text = random.choice(phone)
    return f"{text} {question.correct_answer}"
