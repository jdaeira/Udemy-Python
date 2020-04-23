
import tkinter
from tkinter import *

top = Tk()
L1 = Label(top, text = "Enter stock symbols seperated by a space: ")
L1.place(x = 10,y = 20)
E1 = Entry(top, bd = 1)
E1.place(x = 295, y = 17, height = 25, width = 135 )


L2 = Label(top,text = "Symbol")
L2.place(x = 10,y = 50)


# E2 = Entry(top,bd = 5)
# E2.place(x = 60,y = 50)

L3 = Label(top,text = "Name:")
L3.place(x = 10,y = 150)
E3 = Entry(top,bd = 2)
E3.place(x = 60,y = 150)

def printText():
    L2.configure(text = E1.get())

B = Button(top, text = "Add", command=printText)
B.place(x = 100, y = 100)
top.geometry("500x500+10+10")
top.mainloop()