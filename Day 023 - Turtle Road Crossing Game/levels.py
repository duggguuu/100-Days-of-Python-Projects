#initializing classes

from turtle import Turtle

#setting up permanent variables

ALIGNMENT="center"
FONT=(("Courier",20,"bold"))

class Levels(Turtle):

    def __init__(self):
        super().__init__()
        self.level=1
        self.color("black")
        self.penup()
        self.goto(0,360)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}",align=ALIGNMENT,font=FONT)

    def increase(self):
        self.level+=1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align=ALIGNMENT,font=FONT)