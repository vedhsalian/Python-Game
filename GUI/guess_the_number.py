from tkinter import *
from tkinter import messagebox
import random

correct=random.randint(1,20)
attempts=0

def get_result():
    global correct,attempts
    guess=int(e1.get())
    if 0<guess<21 and guess<correct:
        attempts+=1
        answer="Guess higher"
    elif 0<guess<21 and guess>correct:
        attempts+=1
        answer="Guess lower"
    elif guess==correct:
        answer="You guessed correct"
        attempts+=1
        b1.config(state="disabled")
        e1.config(state="disabled")
    messagebox.showinfo("Result",answer)
    l3.config(text="Attempts:{}".format(attempts))


screen=Tk()
screen.configure(bg="lightgrey")
screen.geometry("800x800")
screen.title("Guess the Number")

l1=Label(text="Guess the Number Game",width=20,height=3,fg="black",bg="lightgrey",font=('Arial',25))
l1.place(x=200,y=50)

l2=Label(text="Guess the number :",width=20,height=1,fg="black",bg="lightgrey",font=('TKDefaultFont',15))
l2.place(x=200,y=200)

e1=Entry(width=30,fg="grey",bg="white")
e1.place(x=400,y=205)

b1=Button(text="Submit",width=40,height=2,fg="black",bg="yellow",command=get_result)
b1.place(x=300,y=300)

l3=Label(text="Attempts : 0",width=20,height=1,fg="black",bg="lightgrey",font=('TKDefaultFont',15))
l3.place(x=300,y=400)

screen.mainloop()