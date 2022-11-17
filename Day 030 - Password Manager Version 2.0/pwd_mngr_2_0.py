#importing classes

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

#adding password to json file

def add_password():
    the_website=web_input.get()
    the_username_email=username_input.get()
    the_password=pwd_input.get()

    new_data={ #creating dictionary for json file
        the_website: {
            "email":the_username_email,
            "password":the_password
        }
        }

    if len(the_website)<1 and len(the_username_email)<1 and len(the_password)<1:
        messagebox.showinfo(title="Error",message="It seems some fields are empty.")
    else:
        is_ok=messagebox.askokcancel(title=the_website,message=f"These are your details: \nUsername: {the_username_email} \nPassword: {the_password} \nIs this okay?")
        if is_ok:
            try:
                with open("password_data.json","r") as f:
                    data=json.load(f)
            except FileNotFoundError:
                with open("password_data.json","w") as f:
                    json.dump(new_data,f,indent=4)
            else:
                data.update(new_data)
                with open("password_data.json","w") as f:
                    json.dump(data,f,indent=4)
            finally:
                web_input.delete(0,END)
                pwd_input.delete(0,END)
                username_input.delete(0,END)

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

#search password

def search_password():
    the_website=web_input.get()
    try:
        with open("password_data.json","r") as f:
            data=json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Not Data Found!",message="Start saving passwords and the search :)")
    else:
        if the_website in data:
            messagebox.showinfo(title="Found!",message=f"{the_website} \nUsername: {data[the_website]['email']} \nPassword: {data[the_website]['password']}")
        else:
            messagebox.showinfo(title="Not Found!",message="The data you are trying to search does not exist. Try Again")
    finally:
        web_input.delete(0,END)
        pwd_input.delete(0,END)
        username_input.delete(0,END)

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

web_input=Entry(width=30) #website input
web_input.get()
web_input.grid(column=1,row=1)
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

search=Button(text="Search",width=14,command=search_password)
search.grid(column=2,row=1)

window.mainloop()