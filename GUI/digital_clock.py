from tkinter import *
import datetime

def get_time():
    current_time=datetime.datetime.now()
    x=current_time.strftime("%H:%M:%S")
    l2.config(text=x)
    l2.after(1000,get_time)

def get_date():
    current_date=datetime.datetime.now()
    y=current_date.strftime("%d/%m/%Y")
    l3.config(text=y)
    l3.after(3600000,get_date)

screen=Tk()
screen.configure(bg="lightgrey")
screen.geometry("500x500")
screen.title("Digital Clock")

l1=Label(text="Digital Calendar and Clock",width=30,height=3,fg="black",bg="lightgrey",font=('Arial',25))
l1.place(x=-10,y=50)

b1=Button(text="Show time",width=20,height=2,bg="lime",fg="black",command=get_time)
b1.place(x=200,y=150)

l2=Label(text="",width=20,height=3,fg="black",bg="lightgrey",font=('TKDefaultFont',20))
l2.place(x=100,y=200)

b2=Button(text="Show date",width=20,height=2,bg="lime",fg="black",command=get_date)
b2.place(x=200,y=300)

l3=Label(text="",width=20,height=3,fg="black",bg="lightgrey",font=('TKDefaultFont',20))
l3.place(x=100,y=350)

screen.mainloop()