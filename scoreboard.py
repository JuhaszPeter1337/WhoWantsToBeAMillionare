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

def modify_scores(scores) -> List:
    tmp_list = []

    for i in range(0, len(scores)):
        counter = 0
        for j in range(0, len(scores[i])):
            if scores[i][j] == ".":
                break
            counter +=1
        tmp_list.append(scores[i][counter+2:])

    return tmp_list

def add_score(scores, name, score) -> list:
    new_score = f"{name}: {score}$"
    scores.append(new_score)
    scores.sort(key=lambda x: -int(x.split(':')[1].strip('$')))
    if(len(scores) > 20):
        top_20 = scores[:20]
        return top_20
    else:
        return scores
    
def create_list(scores) -> None:
    for i in range(len(scores)):
        scores[i] = f"{i + 1}. {scores[i]}"

def write_scores(file_path, scores) -> None:
    with open(file_path, 'w') as file:
        for score in scores:
            file.write(f"{score}\n")