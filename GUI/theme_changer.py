from tkinter import *


def get_colour():
    color=str(colour.get())
    screen.configure(bg=color)
    l1.configure(bg=color)
    r1.configure(bg=color)
    r2.configure(bg=color)
    r3.configure(bg=color)

screen=Tk()
screen.config(bg="white")
screen.title("Theme Changer")
screen.geometry("500x500")

l1=Label(text="Choose background theme",width=20,height=2,fg="black",bg="white",font=('TKDefaultFont',20))
l1.place(x=100,y=20)

colour=StringVar()

r1=Radiobutton(text="red",width=10,value="red",fg="black",bg="white",variable=colour)
r1.place(x=200,y=100)

r2=Radiobutton(text="green",width=10,value="green",fg="black",bg="white",variable=colour)
r2.place(x=200,y=150)

r3=Radiobutton(text="blue",width=10,value="blue",fg="black",bg="white",variable=colour)
r3.place(x=200,y=200)

b1=Button(text="Confirm",width=20,height=2,fg="white",bg="black",command=get_colour)
b1.place(x=200,y=300)

screen.mainloop()