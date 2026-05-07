from tkinter import *

def fetch_temp():
    celsius=float(e1.get())
    fahrenheit=celsius*9/5+32
    l4.config(text=str(fahrenheit))

screen=Tk()
screen.configure(bg="lightgrey")
screen.title("Celsius to Fahrenheit converter")
screen.geometry("800x500")

l1=Label(text="Celsius -> Fahrenheit",width=30,height=3,fg="grey",bg="lightgrey",font=('Arial',30))
l1.place(x=100,y=20)

l2=Label(text="Enter the temperature in Celsius:",width=25,height=1,fg="black",bg="lightgrey",font=('TKDefaultFont',12))
l2.place(x=200,y=200)

e1=Entry(width=30,fg="black",bg="white")
e1.place(x=450,y=200)

l3=Label(text="Temperature in Fahrenheit :",width=40,height=2,fg="black",bg="lightgrey",font=('TKDefaultFont',15))
l3.place(x=100,y=250)

l4=Label(text="",width=10,height=2,fg="black",bg="lightgrey",font=('TKDefaultFont',15))
l4.place(x=450,y=250)

b1=Button(text="Convert",width=15,height=2,bg="lightgreen",fg="black",command=fetch_temp)
b1.place(x=350,y=350)

screen.mainloop()