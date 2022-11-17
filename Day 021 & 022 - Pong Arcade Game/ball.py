#importing classes
from turtle import Turtle,Screen
from paddle import Paddle
import random
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()

#setting a random initial direction

        self.x_move=random.randint(1,9)
        self.y_move=random.randint(-9,9)

#creating ball

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.screen.update()

#making ball move

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.screen.tracer(True)
        self.goto(new_x,new_y)

#make ball bounce from paddle

    def bounce_paddle(self):
        self.x_move *= -1 #reversing x-axis direction

#make ball bounce from wall

    def bounce_wall(self):
        self.y_move *= -1 #reversing y-axis direction

#reset game

    def reset_position(self):
        self.goto(0,0)