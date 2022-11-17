#importing classes

from turtle import Turtle,Screen
from tim import Tim
from cars import Cars
import time
from levels import Levels

#setting up variables

game_is_on=True
s=1
p=1

#setting up screen

screen=Screen()
screen.setup(800,800)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")

#calling classes

tim=Tim()
cars=Cars()
levels=Levels()

#setting up user commands

screen.listen()
screen.onkey(tim.go_up,"Up")
screen.onkey(tim.go_down,"Down")
screen.onkey(tim.go_left,"Left")
screen.onkey(tim.go_right,"Right")

while game_is_on:

#car being generated every 0.1 seconds (but the chances have in set in car module)

    time.sleep(0.1)
    screen.update()

#car behavious

    cars.create_cars(p)
    cars.move(s)

#detecting collision

    for c in cars.all_cars:
        if c.distance(tim)<20:
            levels.game_over()
            game_is_on=False

    if tim.ycor()>340:
        levels.increase()
        s+=1 #increasing speed
        p+=1 #increasing cars generated
        tim.create_tim()

screen.exitonclick()