#importing classes
from turtle import Turtle,Screen
import random

#permanent variables
SIZE_OF_CAR=([1,5])
COLORS=["red","blue","green","yellow","purple","orange","violet","black","brown"]

class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars=[]

    def create_cars(self,p):

#creating a chance for levels

        chance=random.randint(p,10)
        if chance==p:

#setting up new car

            car=Turtle("square")
            car.color("black")
            random_color=COLORS[random.randint(0,8)]
            car.color(random_color)
            car.shapesize(1,2)
            car.penup()

#setting start positions na ddirection

            y=random.randrange(-340,340,20)
            car.goto(380,y)
            car.setheading(180)
            self.all_cars.append(car) #appending all cars into one variable

#moving cars

    def move(self,s):
        for c in self.all_cars:
            c.speed(s)
            c.forward(10)