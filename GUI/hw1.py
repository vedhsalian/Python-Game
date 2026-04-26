import tkinter as tk

screen=tk.Tk()
screen.title("My First Screen")
screen.configure(bg="grey")
screen.geometry("800x800")

l1=tk.Label(text="Hello",width=30,height=5,bg="yellow",fg="black")
l1.place(x=400,y=400)
screen.mainloop() 