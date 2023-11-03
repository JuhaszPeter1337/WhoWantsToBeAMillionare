# Who Wants To Be A Millionare game with Pygame

## Game Description

The goal is to correctly answer 15 consecutive questions, with each question having a higher prize value than the previous one, culminating in a grand prize of one million currency units.

Choose from letters A, B, C or D to answer the question.

Don't forget you have 3 jokers. 
- "Ask the Audience", where the studio audience votes on the answer. 
* "Phone-a-Friend", allowing contestants to make a call for help with the answer. 
+ "50:50", which removes two incorrect answers, leaving the correct answer and one remaining answer.

You can stop and finish the game whenever you want to. Your money will be the price of the previous known question.

If you answer the question wrong, it's game over.

## Prerequisites

### python3

```
sudo apt update
sudo apt install python3 -y
```

### pip3

```
sudo apt install python3-pip -y
```

### Tkinter

```
sudo apt-get install python3-tk -y
```

### pygame-ce

```
pip/pip3 install pygame-ce==2.2.0
```

### matplotlib

```
pip/pip3 install matplotlib
```

### pillow (only if plot does not work)

```
pip/pip3 install --upgrade pillow
```

## Start app

```
python/python3 main.py
```

## Design

### Menu

![Alt text](repo_images/menu.JPG?raw=true "Menu")
### Game description scene

![Alt text](repo_images/description.png?raw=true "Description")
### Starting screen

![Alt text](repo_images/start_screen.JPG?raw=true "Starting screen")
### The game
 
![Alt text](repo_images/game.JPG?raw=true "Game") 
### Phone a friend

![Alt text](repo_images/phone.JPG?raw=true "Phone") 
### Fifty fifty

![Alt text](repo_images/fifty_fifty.JPG?raw=true "Fifty") 
### Ask audience

![Alt text](repo_images/audience.JPG?raw=true "Audience") 
### Game over scene

![Alt text](repo_images/game_over.JPG?raw=true "Game over") 
