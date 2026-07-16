from tkinter import *

screen=Tk()
screen.configure(bg="white")
screen.geometry("600x600")
screen.title("Digital Blackboard")

lastx=None
lasty=None
eraser=False
color_choice=0
select_color=""
line_size=0

colors=["white","yellow","pink"]

def chalk():
    global eraser
    eraser=False

def continue_drawing(event):
    global lastx,lasty,colors,color_choice,eraser,select_color,line_size
    line_size=int(s1.get())
    if eraser:
        select_color="black"
    elif not eraser:
        select_color=colors[color_choice]
    if lastx is not None and lasty is not None:
        canvas.create_line(lastx,lasty,event.x,event.y,width=line_size,fill=select_color,capstyle=ROUND,smooth=True)
        lastx=event.x
        lasty=event.y

def start_drawing(event):
    global lastx,lasty
    lastx=event.x
    lasty=event.y

def stop_drawing(event):
    global lastx,lasty
    lastx=None
    lasty=None

def color():
    global color_choice,eraser
    eraser=False
    if color_choice<2:
        color_choice+=1
    else:
        color_choice=0

def enable_eraser():
    global eraser
    eraser=True

b1=Button(text="Chalk",width=5,height=1,fg="black",bg="lightgrey",command=chalk)
b1.place(x=50,y=20)

b2=Button(text="Color",width=5,height=1,fg="black",bg="lightgrey",command=color)
b2.place(x=150,y=20)

b3=Button(text="Eraser",width=5,height=1,fg="black",bg="lightgrey",command=enable_eraser)
b3.place(x=250,y=20)

s1=Scale(from_=0,to=30,length=150,orient=HORIZONTAL)
s1.place(x=350,y=2)

canvas=Canvas(screen,width=605,height=550,bg="black")
canvas.place(x=-5,y=50)

canvas.bind("<Button-1>",start_drawing)
canvas.bind("<B1-Motion>",continue_drawing)
canvas.bind("<ButtonRelease-1>",stop_drawing)

screen.mainloop()