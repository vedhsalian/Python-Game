import tkinter as tk

screen=tk.Tk()
screen.title("My First Screen")
screen.configure(bg="light blue")
screen.geometry("800x800")

l1=tk.Label(text="Welcome to tkinter",width=30,height=2,bg="green",fg="blue",font=("Arial",15))
l1.place(x=300,y=50)

l2=tk.Label(text="Enter your name: ",width=15,height=1,fg="black")
l2.place(x=50,y=150)

e1=tk.Entry(width=30,bg="white",fg="blue")
e1.place(x=300,y=150)

l3=tk.Label(text="Enter something about yourself: ",width=25,height=1,fg="black")
l3.place(x=50,y=250)

t1=tk.Text(width=30,height=3,bg="white",fg="blue")
t1.place(x=300,y=250)

l4=tk.Label(text="Select your gender:",width=15,height=1,bg="white",fg="black")
l4.place(x=50,y=350)

r1=tk.Radiobutton(text="Male",value=1)
r1.place(x=300,y=350)

r2=tk.Radiobutton(text="Female",value=2)
r2.place(x=400,y=350)

l5=tk.Label(text="Select your hobbies:",width=15,height=1,bg="white",fg="black")
l5.place(x=50,y=450)

c1=tk.Checkbutton(text="Coding",onvalue=1,offvalue=0)
c1.place(x=300,y=450)

c2=tk.Checkbutton(text="Sports",onvalue=1,offvalue=0)
c2.place(x=400,y=450)

c3=tk.Checkbutton(text="Singing",onvalue=1,offvalue=0)
c3.place(x=500,y=450)

c4=tk.Checkbutton(text="Dancing",onvalue=1,offvalue=0)
c4.place(x=600,y=450)

b1=tk.Button(text="Submit",width=10,height=2,bg="green",fg="white")
b1.place(x=100,y=600)
screen.mainloop()