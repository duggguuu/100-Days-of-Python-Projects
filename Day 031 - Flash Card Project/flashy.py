#importing classes

from tkinter import *
import pandas
import random

current_card={}
to_learn={}

#reading the french words csv file

try:
    data=pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas_f.itemconfig(text_f1,text="French Word")
    canvas_f.itemconfig(text_f2,text=current_card["French"],fill="Black")
    canvas_f.itemconfig(card_bg,image=card_f)
    flip_timer=window.after(10000,func=flip_card)

#flipping card

def flip_card():
    global current_card
    canvas_f.itemconfig(text_f1,text="Meaning in English")
    canvas_f.itemconfig(text_f2,text=current_card["English"],fill="White")
    canvas_f.itemconfig(card_bg,image=card_b)

#removing from original list

def is_known():
    to_learn.remove(current_card)
    data_to_learn=pandas.DataFrame(to_learn)
    data_to_learn.to_csv("words_to_learn.csv",index=False)
    next_card()

#setting up cards

BG="#B1DDC6"
FONT_NAME="Arial"

window=Tk()
window.title("Flashy")
window.minsize(900,900)
window.config(padx=50,pady=50,background=BG)

flip_timer=window.after(5000,func=flip_card)

canvas_f=Canvas(width=800,height=526,bg=BG,highlightthickness=0)
card_f=PhotoImage(file="card_front.png")
card_b=PhotoImage(file="card_back.png")
card_bg=canvas_f.create_image(400,264,image=card_f)
text_f1=canvas_f.create_text(400,150,text="French Words Will Appear Here",fill="black",font=(FONT_NAME,32,"italic"))
text_f2=canvas_f.create_text(400,264,text="Let's Begin?",fill="black",font=(FONT_NAME,32,"bold"))
canvas_f.grid(column=0,row=0,columnspan=2)

#setting up tick and cross

cross=PhotoImage(file="wrong.png")
button_cross=Button(image=cross,highlightthickness=0,command=flip_card)
button_cross.grid(column=0,row=1)

tick=PhotoImage(file="right.png")
button_tick=Button(image=tick,highlightthickness=0,command=is_known)
button_tick.grid(column=1,row=1)

next_card()

window=mainloop()