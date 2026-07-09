from tkinter import *

screen=Tk()
screen.configure(bg="grey")
screen.geometry("800x800")
screen.title("Color Paint")

lastx=None
lasty=None
eraser=False
line_width=0

def pen():
    global line_width
    line_width=1

def brush():
    global line_width
    line_width=10

def continue_drawing(event):
    global lastx,lasty
    line_width1=int(s1.get())
    color_index=lb1.curselection()
    if color_index:
        index=color_index[0]
        selected_color=lb1.get(index)
    if eraser:
        selected_color="white"
    if lastx is not None and lasty is not None:
        canvas.create_line(lastx,lasty,event.x,event.y,width=line_width+line_width1,fill=selected_color,capstyle=ROUND,smooth=True)
        lastx=event.x
        lasty=event.y

def erase():
    global eraser
    eraser=True

def start_drawing(event):
    global lastx,lasty
    lastx=event.x
    lasty=event.y

def stop_drawing(event):
    global lastx,lasty
    lastx=None
    lasty=None

b1=Button(text="Pen",width=10,height=1,fg="black",bg="orange",command=pen)
b1.place(x=50,y=20)

b2=Button(text="Brush",width=10,height=1,fg="black",bg="red",command=brush)
b2.place(x=200,y=20)

b3=Button(text="Eraser",width=10,height=1,fg="black",bg="yellow",command=erase)
b3.place(x=350,y=20)

s1=Scale(from_=0,to=30,length=100,orient=HORIZONTAL)
s1.place(x=500,y=20)

l1=Label(text="Color:",width=20,height=1,fg="black",bg="grey",font=('TKDefaultFont',15))
l1.place(x=50,y=100)

lb1=Listbox(width=15,height=3,fg="black",bg="white",selectmode=SINGLE)
lb1.place(x=200,y=90)

colors=["red","blue","yellow","orange","green","purple","black"]

for color in colors:
    lb1.insert(END,color)

canvas=Canvas(screen,width=780,height=640,bg='white')
canvas.place(x=10,y=150)

canvas.bind("<Button-1>",start_drawing)
canvas.bind("<B1-Motion>",continue_drawing)
canvas.bind("<ButtonRelease-1>",stop_drawing)

screen.mainloop()