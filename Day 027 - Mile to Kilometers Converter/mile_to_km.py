from tkinter import *

window=Tk()
window.title("Mile to Km Converter")
window.minsize(300,300)
window.config(padx=20,pady=20)


mile_input=Entry(width=10)
mile_input.get()
mile_input.grid(column=1,row=0)


miles_label=Label(text="Miles",font=("Poppins",16,"normal"))
miles_label.grid(column=2,row=0)
miles_label.config(padx=10,pady=10)


miles_label=Label(text="is equal to",font=("Poppins",16,"normal"))
miles_label.grid(column=0,row=1)


kms_label=Label(text="0",font=("Poppins",16,"normal"))
kms_label.grid(column=1,row=1)


miles_label=Label(text="Km",font=("Poppins",16,"normal"))
miles_label.grid(column=2,row=1)


def button_clicked():
    ml=int(mile_input.get())
    km=ml*1.6
    round(km,2)
    kms_label.config(text=km)
calculate=Button(text="Calculate",command=button_clicked)
calculate.grid(column=1,row=2)


window.mainloop()