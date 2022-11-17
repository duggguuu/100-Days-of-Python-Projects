#importing classes
from turtle import Turtle,Screen

#setting permanent turtle start position
POSITION_START=([0,-380])

class Tim(Turtle):

    def __init__(self):
        super().__init__()
        self.create_tim()

#creating tim

    def create_tim(self):
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.screen.tracer(False)
        self.setheading(90)
        self.goto(POSITION_START)
        self.screen.update()

#setting up user commands

    def go_up(self):
        self.screen.tracer(True)
        self.forward(10)
        self.screen.tracer(False)

    def go_down(self):
        self.screen.tracer(True)
        self.backward(10)
        self.screen.tracer(False)

    def go_left(self):
        self.screen.tracer(False)
        self.setheading(180)
        self.forward(10)
        self.setheading(90)
        self.screen.update()

    def go_right(self):
        self.screen.tracer(False)
        self.setheading(0)
        self.forward(10)
        self.setheading(90)
        self.screen.update()