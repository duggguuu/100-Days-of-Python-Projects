#importing classes

from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#adding password to text file

def add_password():
    the_website=web_input.get()
    the_username_email=username_input.get()
    the_password=pwd_input.get()
    if len(the_website)<1 and len(the_username_email)<1 and len(the_password)<1:
        messagebox.showinfo(title="Error",message="It seems some fields are empty.")
    else:
        is_ok=messagebox.askokcancel(title=the_website,message=f"These are your details: \nUsername: {the_username_email} \nPassword: {the_password} \nIs this okay?")
        if is_ok:
            f=open("password_data.txt","a")
            f.write(f"{the_website} | {the_username_email} | {the_password}\n")
            web_input.delete(0,END)
            pwd_input.delete(0,END)

#password_generator

def password_generator():
    letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters=[random.choice(letters) for _ in range(random.randint(8,10))]
    password_numbers=[random.choice(numbers) for _ in range(random.randint(2,4))]
    password_symbols=[random.choice(symbols) for _ in range(random.randint(2,4))]
    password_list=password_letters+password_numbers+password_symbols
    random.shuffle(password_list)
    gen_pwd="".join(password_list)
    pwd_input.insert(0,gen_pwd)
    pyperclip.copy(gen_pwd)

#setting up UI

window=Tk()
window.title("My Pass - A Password Manager")
window.minsize(400,300)
window.config(padx=50,pady=50)
canvas=Canvas(width=200,height=190)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,95,image=logo)
canvas.grid(column=1,row=0)

website_name=Label(text="Website:")
website_name.grid(column=0,row=1)

web_input=Entry(width=48) #website input
web_input.get()
web_input.grid(column=1,row=1,columnspan=2)
web_input.focus()

username=Label(text="Email/Username:")
username.grid(column=0,row=2)

username_input=Entry(width=48) #username input
username_input.get()
username_input.grid(column=1,row=2,columnspan=2)

pwd_txt=Label(text="Password:")
pwd_txt.grid(column=0,row=3)

pwd_input=Entry(width=30) #password input
pwd_input.get()
pwd_input.grid(column=1,row=3)

generator=Button(text="Generate Password",command=password_generator)
generator.grid(column=2,row=3)

adder=Button(text="Add",width=60,command=add_password)
adder.grid(column=0,row=4,columnspan=3)

window.mainloop()