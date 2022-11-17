#importing classes

from turtle import Turtle

#setting permanent variables

FONT=("Poppins",6,"bold")

class ShowState(Turtle):

    def __init__(self):
        super().__init__()
        self.new_states=[]
        self.hideturtle()

    def show_new_state(self,answer,xcor,ycor):
        new_state=Turtle()
        new_state.color("black")
        new_state.penup()
        new_state.hideturtle()
        new_state.goto(xcor,ycor)
        new_state.write(f"{answer}",font=FONT)
        self.new_states.append(new_state)