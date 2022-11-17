#importing classes
from turtle import Turtle

#initializing permanent variables
ALIGNMENT="center"
FONT=(["Courier",20,"normal"])

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_user=0
        self.score_pc=0
        self.color("white")
        self.penup()
        self.goto(0,460)
        self.hideturtle()
        self.update_score()

#updating score whenever needed

    def update_score(self):
        self.clear()
        self.write(f"{self.score_pc} - score - {self.score_user}",align=ALIGNMENT,font=FONT)

#increase point for user

    def increase_user(self):
        self.score_user+=1
        self.clear
        self.update_score()

#increase point for pc

    def increase_pc(self):
        self.score_pc+=1
        self.clear
        self.update_score()

#game over macha

    def game_over(self):
        self.goto(0,0)
        self.write(f"game over",align=ALIGNMENT,font=FONT)