#importing classes

from tkinter import *
import math

#setting up permanent variables

PINK="#e2979c"
RED="#e7305b"
GREEN="#9bdeac"
YELLOW="#f7f5dd"
FONT_NAME="Courier"
WORK_MIN=25
SHORT_BREAK_MIN=5
LONG_BREAK_MIN=20
global reps
reps=0
global check
check=""
timer_move=None

#reset timer

def reset_timer():
    window.after_cancel(timer_move)
    canvas.itemconfig(timer_text,text="00:00")
    timer.config(text="Timer",fg=GREEN)
    checkmarks.config(text="")
    global reps
    reps=0

#start timer

def start_timer():
    global reps
    global check
    reps+=1
    if reps%2==0:
        if reps%8==0:
            timer.config(text="Long Break",fg=RED)
            checkmarks.config(text="Kudos!")
            countdown(15)
        else:
            timer.config(text="Break",fg=PINK)
            check=check+"✔"
            checkmarks.config(text=check)
            countdown(5)
    elif reps%2==1:
        timer.config(text="Work",fg=GREEN)
        countdown(10)

#setting countdown

def countdown(count):
    min=math.floor(count/60)
    sec=count%60
    if sec<10:
        sec=f"0{sec}"
    canvas.itemconfig(timer_text,text=f"{min}:{sec}")
    if count>0:
        global timer_move
        timer_move=window.after(1000,countdown,count-1)
    else:
        start_timer()

#setting UI

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,32,"bold"))
canvas.grid(column=1,row=1)

timer=Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,32,"bold"))
timer.grid(column=1,row=0)

checkmarks=Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,24,"bold"))
checkmarks.grid(column=1,row=3)

start_button=Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",command=reset_timer)
reset_button.grid(column=2,row=2)

window.mainloop()