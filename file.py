from question import *

questions = "questions/questions.txt"

quiz = []

def read_from_file() -> None:
    try:
        with open(questions, "r") as file:
            for line in file:
                data = line.strip().split(",")
                quiz.append(Question(data[0], data[1], data[2], data[3], data[4], data[5]))
    except FileNotFoundError:
        print("File not found.")

def write_to_file() -> None:
    try:
        with open(questions, "w") as file:
            for i in range(0, len(quiz)):
                if i < len(quiz) - 1:
                    question = f"{quiz[i].question},{quiz[i].option_A},{quiz[i].option_B},{quiz[i].option_C},{quiz[i].option_D},{quiz[i].correct_answer}\n"
                else:
                    question = f"{quiz[i].question},{quiz[i].option_A},{quiz[i].option_B},{quiz[i].option_C},{quiz[i].option_D},{quiz[i].correct_answer}"
                file.write(question)
    except FileNotFoundError:
        print("File not found.")