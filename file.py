from question import *

questions = "questions/questions.txt"

quiz = []

def read_from_file():
    try:
        with open(questions, "r") as file:
            for line in file:
                data = line.strip().split(",")
                quiz.append(Question(data[0], data[1], data[2], data[3], data[4], data[5]))
    except FileNotFoundError:
        print("File not found.")