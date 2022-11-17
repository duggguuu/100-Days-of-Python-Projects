#importing classes
from turtle import Turtle,Screen

#initializing permanent variables
UP=90
DOWN=270

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        position_user=((470,0))
        position_pc=((-470,0))
        self.create_paddle_user(position_user)
        self.create_paddle_pc(position_pc)
        # self.paddle_user=self.paddle_1
        # self.paddle_pc=self.paddle_2

#creating paddles

    def create_paddle_user(self,position):    
        paddle_1=Turtle("square")
        paddle_1.color("white")
        paddle_1.shapesize(stretch_wid=5,stretch_len=1)
        paddle_1.penup()
        paddle_1.goto(position)
        self.paddle_user=paddle_1

    def create_paddle_pc(self,position):    
        paddle_2=Turtle("square")
        paddle_2.color("white")
        paddle_2.shapesize(stretch_wid=5,stretch_len=1)
        paddle_2.penup()
        paddle_2.goto(position)
        self.paddle_pc=paddle_2

#move paddle

    def user_up(self):
        new_x=470
        new_y=self.paddle_user.ycor()+40
        self.paddle_user.goto(new_x,new_y)
        self.screen.update()
    def user_down(self):
        new_x=470
        new_y=self.paddle_user.ycor()-40
        self.paddle_user.goto(new_x,new_y)
        self.screen.update()
    def pc_up(self):
        new_x=-470
        new_y=self.paddle_pc.ycor()+40
        self.paddle_pc.goto(new_x,new_y)
        self.screen.update()
    def pc_down(self):
        new_x=-470
        new_y=self.paddle_pc.ycor()-40
        self.paddle_pc.goto(new_x,new_y)
        self.screen.update()






