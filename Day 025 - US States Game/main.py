#importing classes

from tkinter import N
import turtle
import pandas
from showstate import ShowState

#setting up screen

screen=turtle.Screen()
screen.title("U.S. States Game")
map="blank_states_img.gif"
screen.addshape(map)
turtle.shape(map)

#calling classes

showstate=ShowState()

#import the data from csv

data=pandas.read_csv("50_states.csv")
all_states=data["state"].to_list()
n=data.shape[0] #extracting total number of states
i=0 #number of states found
print(n)

#running the game

answer=screen.textinput(title=f"U.S. States Guessing Game",prompt="Guess & type a state's name.") #getting first user input
answer=answer.title()

game_is_on=True
while game_is_on:

#checking for correct answer

    count=len(data[data["state"]==answer])
    
    if count==1:
        i+=1

#checking if you've guessed all 50 states

        if i==50:

#want to play again?

            answer=screen.textinput(title=f"Yayy!! All {i}/{n} States Found",prompt="Do you want to play again? Type 'yes' or 'no.'")
            answer=answer.lower()
            if answer=="no":
                game_is_on=False
            elif answer=="yes":
                i=0
                answer=screen.textinput(title=f"U.S. States Guessing Game",prompt="Guess & type a state's name.") #getting first user input
                answer=answer.title()
                continue

#pulling out co-ordinates of the state

        name=data[data.state==answer]
        xcor=int(name.x)
        ycor=int(name.y)
        showstate.show_new_state(answer,xcor,ycor)
        answer=screen.textinput(title=f"Correct!! {i}/{n} States Found",prompt="Guess & type a state's name.")
        answer=answer.title()

    else:
        answer=screen.textinput(title=f"xx Wrong xx - {i}/{n} States Found",prompt="Guess & type a state's name.")
        answer=answer.title()

#so that the screen doesn't close and game keeps running

screen.exitonclick()