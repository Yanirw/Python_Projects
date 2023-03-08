from turtle import Turtle
import random

COLORS = ['white', 'grey', 'gray', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'orange', 'brown']

class Food(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid= 0.6)
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        self.color(random.choice(COLORS))
        randomx = random.randint(-275, 275)
        randomy = random.randint(-275, 275)
        self.goto(randomx, randomy)

