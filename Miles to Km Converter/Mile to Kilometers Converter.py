from tkinter import *


def button_clicked():
    num = float(input.get())
    new_value = round(num*1.609, 2)
    num_converted.config(text=new_value)


screen = Tk()
screen.title("Miles to Km Converter")
screen.minsize(width=200, height=120)
screen.config(padx = 20, pady = 20)


label1 = Label(text = " Miles", font=("Times New Roman", 18, "normal"))
label1.grid(column=2, row=0)

label2 = Label(text = "is equal to", font = ("Times New Roman", 18, "normal"))
label2.grid(column = 0, row = 1)

label3 = Label(text = "Km", font = ("Times New Roman", 18, "normal"))
label3.grid(column = 2, row = 1)

num_converted = Label(text = "0", font = ("Times New Roman", 20, "bold"))
num_converted.grid(column = 1, row = 1)


#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entry
input = Entry(width=8)
input.grid(column=1, row=0)


screen.mainloop()
