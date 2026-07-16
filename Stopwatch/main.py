import time
from tkinter import *

screen=Tk()
screen.geometry("700x400")
screen.configure(bg="lightgrey")
screen.title("Stopwatch")

start_time=0
hrs=0
mins=0
secs=0
running=False
id=None

def start_timer():
    global start_time,hrs,mins,secs,running,id
    running=True
    start_time=time.time()
    secs+=1
    if secs>59:
        mins+=1
        secs=0
    if mins>59:
        hrs+=1
        mins=0
    l2.config(text=str(hrs))
    l4.config(text=str(mins))
    l6.config(text=str(secs))
    if running:
        id=l6.after(1000,start_timer)
    b1.configure(state="disabled")

def stop_timer():
    global running,id
    running=False
    l6.after_cancel(id)
    b1.configure(state="active")

def reset_timer():
    global hrs,mins,secs,running
    running=False
    
    l6.after_cancel(id)
    b1.configure(state="active")
    hrs=0
    mins=0
    secs=0
    l2.config(text=str(hrs))
    l4.config(text=str(mins))
    l6.config(text=str(secs))

l1=Label(text="Stopwatch",width=20,height=3,fg="black",bg="lightgrey",font=('TKDefaultFont',15))
l1.place(x=270,y=20)

l2=Label(text=str(hrs),width=10,height=1,fg="black",bg="lightgrey",font=('TKDefaultFont',14))
l2.place(x=100,y=200)

l3=Label(text=":",width=10,height=1,fg="black",bg="lightgrey",font=('TKDefaultFont',14))
l3.place(x=200,y=200)

l4=Label(text=str(mins),width=10,height=1,fg="black",bg="lightgrey",font=('TKDefaultFont',14))
l4.place(x=300,y=200)

l5=Label(text=":",width=10,height=1,fg="black",bg="lightgrey",font=('TKDefaultFont',14))
l5.place(x=400,y=200)

l6=Label(text=str(secs),width=20,height=1,fg="black",bg="lightgrey",font=('TKDefaultFont',14))
l6.place(x=500,y=200)

b1=Button(text="Start",width=15,height=2,fg="black",bg="green",command=start_timer)
b1.place(x=150,y=300)

b2=Button(text="Stop",width=15,height=2,fg="black",bg="red",command=stop_timer)
b2.place(x=300,y=300)

b3=Button(text="Reset",width=15,height=2,fg="black",bg="orange",command=reset_timer)
b3.place(x=450,y=300)

screen.mainloop()