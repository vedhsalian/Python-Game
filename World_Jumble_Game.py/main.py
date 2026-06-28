from tkinter import *
from tkinter import messagebox
import random

q=0
n=0
score=0
actual_answer=""

riddles={"What five-letter word becomes shorter when you add two letters to it?":"short","What begins with an “e” and only contains one letter?":"envelope","What has to be broken before you can use it?":"egg","I’m tall when I’m young, and I’m short when I’m old. What am I?":"candle","What is full of holes but still holds water?":"sponge"}

questions=list(riddles.keys())

current_key=questions[q]

def start_game():
    global riddles,questions,current_key,actual_answer
    l2.config(text=current_key)
    actual_answer=riddles[current_key]
    wordlist=list(actual_answer)
    random.shuffle(wordlist)
    shuffledword="".join(wordlist)
    l3.config(text=shuffledword)
    b1.config(state="disabled")


def next():
    global q,current_key,questions,n,actual_answer,score
    answer=e1.get()
    answer=answer.lower()
    answer=answer.strip()
    if actual_answer==answer:
        score+=1
        messagebox.showinfo("Correct","You guessed it correct")
    else:
        messagebox.showinfo("Incorrect","The correct answer is "+actual_answer)
    q+=1
    current_key=questions[q]
    e1.delete(0,END)
    start_game()
    if n>=4:
        b2.config(state="disabled")
    n+=1

def submit():
    global score,n
    if n==4:
        l4.config(text="Score: "+str(score))
    else:
        messagebox.showinfo("Incomplete","Ensure you answer all 5 questions")

screen=Tk()
screen.title("Word Jumble Game")
screen.geometry("1000x700")
screen.configure(bg="black")

l1=Label(text="Word Jumble Game",width=30,height=3,fg="grey",bg="black",font=('TKDefaultFont',25))
l1.place(x=200,y=20)

l2=Label(text="Click Start",width=70,height=2,fg="lightgrey",bg="black",font=('TKDefaultFont',15))
l2.place(x=150,y=150)

l3=Label(text="",width=25,height=2,fg="white",bg="black",font=('TKDefaultFont',20))
l3.place(x=270,y=200)

e1=Entry(width=25,fg="black",bg="white")
e1.place(x=400,y=300)

b1=Button(text="Start",width=20,height=2,fg="black",bg="lime",command=start_game)
b1.place(x=200,y=400)

b2=Button(text="Next",width=20,height=2,fg="black",bg="red",command=next)
b2.place(x=400,y=400)

b3=Button(text="Submit",width=20,height=2,fg="black",bg="cyan",command=submit)
b3.place(x=600,y=400)

l4=Label(text="Score: ",width=20,height=1,fg="white",bg="black")
l4.place(x=400,y=550)

screen.mainloop()