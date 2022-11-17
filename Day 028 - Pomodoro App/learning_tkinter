from tkinter import *

window=Tk()
window.title("My 1st GUI Program")
window.minsize(500,300)

my_label=Label(text="I am a label",font=("Poppins",24,"normal"))
my_label.pack()

my_label["text"]="new text"
my_label.config(text="new text")

def button_clicked():
    new_text=input.get()
    my_label.config(text=new_text)

button=Button(text="click me",command=button_clicked)
button.pack()

input=Entry(width=50)
input.insert(END, string="type something")
input.pack()
input.get()

text=Text(height=5,width=30)
text.focus()
text.insert(END,"type more details")
print(text.get("1.0",END))
text.pack()

def spinbox_used():
    print(spinbox.get())
spinbox=Spinbox(from_=0,to=10, width=5,command=spinbox_used)
spinbox.pack()

def scale_used(value):
    print(value)
scale=Scale(from_=0,to=100,command=scale_used)
scale.pack()

def checkbutton_used():
    print(checked_state.get())
checked_state=IntVar()
checkbutton=Checkbutton(text="is on?",variable=checked_state,command=checkbutton_used)
checked_state.get()
checkbutton.pack()

def radio_used():
    print(radio_state.get())
radio_state=IntVar()
radiobutton1=Radiobutton(text="option 1",value=1,variable=radio_state,command=radio_used)
radiobutton2=Radiobutton(text="option 2",value=2,variable=radio_state,command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox=Listbox(height=4)
fruits=["apple","banana","mango","orange"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()

window.mainloop()

# def add(*args):
#     t=0
#     for n in args:
#         t+=n
#     print (t)
# add (1,2,3,5,4,7,8,9,7,8,5,2,500,8,5.5,1,1,5,8,5,4,5,5,5,5,5,55,5,4)

# def calculate(n,**kwargs):
#     for key,value in kwargs.items():
#         print(key)
#         print(value)
# calculate(add=3,multiply=5)