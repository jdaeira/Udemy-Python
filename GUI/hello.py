
import tkinter
from tkinter import *


window = Tk()
window.title("Welcome to Tkinter Practice")
window.geometry("500x500") #Width x Height

lbl = Label(window, text="Hello Label!", width = 10)
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)

score = 0

def clicked_10():
    #res = "Welcome to " + txt.get()
    global score
    score += 10
    lbl.configure(text= score)

def clicked_20():
    global score
    score += 20
    lbl.configure(text= score)

# def clicked():
#     lbl.configure(text="Button was clicked !!")

btn10 = Button(window, text="Add $10", command=clicked_10)
btn10.grid(column=2, row=0)

btn20 = Button(window, text="Add $20", command=clicked_20)
btn20.grid(column=3, row=0)

window.mainloop()