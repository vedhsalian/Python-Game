from tkinter import *

def convert_currency():
    dollar=float(e1.get())
    rupees=dollar*94.89
    l2.config(text=str(rupees)+"Rs.")

screen=Tk()
screen.geometry("500x500")
screen.configure(bg="grey")
screen.title("Currency Converter")

l1=Label(text="Enter the amount in USD:",width=20,height=1,fg="black",bg="grey")
l1.place(x=50,y=50)

e1=Entry(width=30,bg="white",fg="black")
e1.place(x=250,y=50)

b1=Button(text="Convert",width=15,height=2,bg="yellow",fg="black",command=convert_currency)
b1.place(x=200,y=150)

l2=Label(text="In INR",width=15,height=1,bg="white",fg="black")
l2.place(x=200,y=250)

screen.mainloop()