from tkinter import *
from tkinter import ttk

def generate_table():
    global tablelist
    number=int(e1.get())
    rangenumber=int(range1.get())
    for i in range(1,rangenumber+1):
        item=str(number)+"x"+str(i)+"="+str(number*i)
        tablelist.append(item)
    c1.config(values=tablelist)

screen=Tk()
screen.config(bg="lightgrey")
screen.title("Multiplication Table Generator")
screen.geometry("500x800")

l1=Label(text="Multiplication Table Generator",width=30,height=3,fg="grey",bg="lightgrey",font=('Impact',20))
l1.place(x=50,y=20)

l2=Label(text="Enter the Number:",width=20,height=1,fg="black",bg="lightgrey")
l2.place(x=50,y=150)

e1=Entry(width=15,fg="black",bg="white")
e1.place(x=250,y=150)

l3=Label(text="Select the Range:",width=20,height=1,fg="black",bg="lightgrey")
l3.place(x=50,y=200)

range1=IntVar()

r1=Radiobutton(text="10",width=5,value=10,variable=range1)
r1.place(x=200,y=200)

r2=Radiobutton(text="20",width=5,value=20,variable=range1)
r2.place(x=300,y=200)

r3=Radiobutton(text="30",width=5,value=30,variable=range1)
r3.place(x=400,y=200)

b1=Button(text="Generate",width=30,height=2,fg="black",bg="lime",command=generate_table)
b1.place(x=150,y=250)

tablelist=[]

c1=ttk.Combobox(height=range1,values=tablelist)
c1.place(x=100,y=300)

screen.mainloop()