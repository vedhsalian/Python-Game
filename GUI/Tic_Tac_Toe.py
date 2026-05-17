from tkinter import *
from tkinter import messagebox

turn="X"
turns=0
winner=False

def tic_tac_toe(button_id):
    global turn,turns,winner
    turns+=1
    button_id.config(text=turn)
    button_id.config(state="disabled")
    if turn=="X":
        button_id.config(bg="pink")
    else:
        button_id.config(bg="skyblue")
    if b1.cget("text")==b2.cget("text")==b3.cget("text"):
        winner=True
        messagebox.showinfo("You Win!",turn+" wins")
        next_round()
    if b4.cget("text")==b5.cget("text")==b6.cget("text") != "":
        winner=True
        messagebox.showinfo("You Win!",turn+" wins")
        next_round()
    if b7.cget("text")==b8.cget("text")==b9.cget("text") != "":
        winner=True
        messagebox.showinfo("You Win!",turn+" wins")
        next_round()
    if b1.cget("text")==b4.cget("text")==b7.cget("text") != "":
        winner=True
        messagebox.showinfo("You Win!",turn+" wins")
        next_round()
    if b2.cget("text")==b5.cget("text")==b8.cget("text") != "":
        winner=True
        messagebox.showinfo("You Win!",turn+" wins")
        next_round()
    if b3.cget("text")==b6.cget("text")==b9.cget("text") != "":
        winner=True
        messagebox.showinfo("You Win!",turn+" wins")
        next_round()
    if b1.cget("text")==b5.cget("text")==b9.cget("text") != "":
        winner=True
        messagebox.showinfo("You Win!",turn+" wins")
        next_round()
    if b3.cget("text")==b5.cget("text")==b7.cget("text") != "":
        winner=True
        messagebox.showinfo("You Win!",turn+" wins")
        next_round()
    if turns==9 and winner==False:
        messagebox.showinfo("Draw","Nobody won")
    if turn=="X":
        turn="O"
    else:
        turn="X"
    l1.config(text="Turn - "+turn)

def next_round():
    global turns,winner
    b1.config(text="",bg="lightgrey",state="normal")
    b2.config(text="",bg="lightgrey",state="normal")
    b3.config(text="",bg="lightgrey",state="normal")
    b4.config(text="",bg="lightgrey",state="normal")
    b5.config(text="",bg="lightgrey",state="normal")
    b6.config(text="",bg="lightgrey",state="normal")
    b7.config(text="",bg="lightgrey",state="normal")
    b8.config(text="",bg="lightgrey",state="normal")
    b9.config(text="",bg="lightgrey",state="normal")
    winner=False
    turns=0


screen=Tk()
screen.geometry("500x700")
screen.title=("Tic-Tac-Toe")
screen.config(bg="white")

l1=Label(text="Turn - "+turn,width=10,height=1,fg="black",bg="white",font=('TKDefaultFont',20))
l1.place(x=150,y=20)

b1=Button(text="",width=22,height=8,fg="black",bg="lightgrey",font=('TKDefaultFont',15),command=lambda:tic_tac_toe(b1))
b1.place(x=0,y=100)

b2=Button(text="",width=22,height=8,fg="black",bg="lightgrey",font=('TKDefaultFont',15),command=lambda:tic_tac_toe(b2))
b2.place(x=166,y=100)

b3=Button(text="",width=22,height=8,fg="black",bg="lightgrey",font=('TKDefaultFont',15),command=lambda:tic_tac_toe(b3))
b3.place(x=332,y=100)

b4=Button(text="",width=22,height=8,fg="black",bg="lightgrey",font=('TKDefaultFont',15),command=lambda:tic_tac_toe(b4))
b4.place(x=0,y=232)

b5=Button(text="",width=22,height=8,fg="black",bg="lightgrey",font=('TKDefaultFont',15),command=lambda:tic_tac_toe(b5))
b5.place(x=166,y=232)

b6=Button(text="",width=22,height=8,fg="black",bg="lightgrey",font=('TKDefaultFont',15),command=lambda:tic_tac_toe(b6))
b6.place(x=332,y=232)

b7=Button(text="",width=22,height=6,fg="black",bg="lightgrey",font=('TKDefaultFont',15),command=lambda:tic_tac_toe(b7))
b7.place(x=0,y=364)

b8=Button(text="",width=22,height=6,fg="black",bg="lightgrey",font=('TKDefaultFont',15),command=lambda:tic_tac_toe(b8))
b8.place(x=166,y=364)

b9=Button(text="",width=22,height=6,fg="black",bg="lightgrey",font=('TKDefaultFont',15),command=lambda:tic_tac_toe(b9))
b9.place(x=332,y=364)

b10=Button(text="Next Round",width=30,height=3,fg="black",bg="orange",font=('TKDefaultFont',15),command=next_round)
b10.place(x=80,y=600)

screen.mainloop()