from pathlib import Path
from typing import List

scoreboard = "scoreboard.txt"
filePath = Path(scoreboard)
filePath.touch(exist_ok = True)

def read_scores(scoreboard) -> List:
    scores = []
    with open(scoreboard, 'r') as file:
        for line in file:
            scores.append(line.strip())
    return scores

def add_score(scores, name, score):
    new_score = f"{name}: {score}$"
    scores.append(new_score)
    scores.sort(key=lambda x: -int(x.split(':')[1].strip('$')))

def write_scores(file_path, scores):
    with open(file_path, 'w') as file:
        for score in scores:
            file.write(score + '\n')