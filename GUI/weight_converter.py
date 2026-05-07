from tkinter import *

def fetch_weight():
    kg=float(e1.get())
    grams=kg*1000
    pounds=kg*2.2
    ounces=kg*35.7
    l2.config(text=str(grams))
    l3.config(text=str(ounces))
    l4.config(text=str(pounds))

screen=Tk()
screen.configure(bg="grey")
screen.title("Weight converter")
screen.geometry("800x500")

l1=Label(text="Enter the weight Kg:",width=20,height=1,fg="black",bg="grey")
l1.place(x=50,y=50)

e1=Entry(width=30,bg="white",fg="black")
e1.place(x=250,y=50)

b1=Button(text="Convert",width=15,height=2,bg="yellow",fg="black",command=fetch_weight)
b1.place(x=200,y=150)

l2=Label(text="In grams",width=15,height=2,bg="white",fg="black")
l2.place(x=100,y=250)

l3=Label(text="In ounces",width=15,height=2,bg="white",fg="black")
l3.place(x=350,y=250)

l4=Label(text="In pounds",width=15,height=2,bg="white",fg="black")
l4.place(x=600,y=250)

screen.mainloop()