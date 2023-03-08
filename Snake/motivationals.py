from turtle import Turtle
from scoreboard import ScoreBoard
import random
ALIGNMENT = "center"
FONT = ("Arial", 15,"bold")

list_of_motivation = ["Fuck yes!", "Yesssss!", "Oh yes.", "Not bad!", "Keep going!"]

class Motivationals(ScoreBoard):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.goto(0,240)
        self.hideturtle()
        

    def awsome_text(self):
        randon_motivation = random.choice(list_of_motivation)
        self.write(f"{randon_motivation}", align=ALIGNMENT, font=FONT)
       

    def new_awsome_text(self):
        self.clear()
        self.awsome_text()
        

