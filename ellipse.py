import pygame
import math
from constants import *
from shape import *
from help import *
from button import *
from screens import *
from typing import List
from music import *

audience, phone, fifty = True, True, True

def popup(text) -> None:
    top = Tk() # to hide the main window
    top.wm_withdraw()
    messagebox.showinfo(title='Phone-a-Friend', message=text)
    pygame.event.pump()
    top.destroy()
    top.mainloop()

class Ellipse(Shape):
    def __init__(self, x, y, width, height, type) -> None:
        super().__init__(x, y, width, height)
        self.type = type

    def draw(self, screen) -> None:
        pygame.draw.ellipse(screen, BLUE, (self.x, self.y, self.width, self.height))

    #(x - h)^2 / a^2 + (y - k)^2 / b^2 <= 1
    def isOver(self, pos) -> float:
        point_x, point_y = pos[0], pos[1]
        ellipse_center_x, ellipse_center_y = self.x + self.width / 2, self.y + self.height / 2
        half_width, half_height = self.width / 2, self.height / 2
        p = ((math.pow((point_x - ellipse_center_x), 2) / math.pow(half_width, 2)) + (math.pow((point_y - ellipse_center_y), 2) / math.pow(half_height, 2)))
        return p

    def update(self, screen, question) -> List[str]:
        global fifty, phone, audience
        collision = self.isOver(pygame.mouse.get_pos())
        if collision <= 1:
            if self.type == "fifty" and fifty:
                fifty = False
                obj = fifty_fifty(question)
                
                buttons = [
                    Button(100, 770, 450, 80, WHITE, "A","A, " + obj.option_A),
                    Button(650, 770, 450, 80, WHITE, "B","B, " + obj.option_B),
                    Button(100, 880, 450, 80, WHITE, "C","C, " + obj.option_C),
                    Button(650, 880, 450, 80, WHITE, "D","D, " + obj.option_D)
                ]

                for button in buttons:
                    button.draw(screen)

                pygame.draw.line(screen, RED, (779, 535), (879, 595), width=6)
                pygame.draw.line(screen, RED, (879, 535), (779, 595), width=6)
                threading.Thread(target=fifty_fifty_song, daemon=True).start()
                pygame.display.update()

                return [obj.option_A, obj.option_B, obj.option_C, obj.option_D]

            elif self.type == "phone" and phone:
                phone = False
                text, correct_answer = phone_call(question)
                phone_screen(screen, text, correct_answer)
                
            elif self.type == "audience" and audience:
                audience = False
                values = use_audience(question)
                evaulate = evaluate_audience(question, values)
                sorted_dict = dict(sorted(evaulate.items()))
                my_list = list(sorted_dict.values())
                audience_diagram(screen, my_list)
