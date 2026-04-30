import tkinter as tk

def fetch_details():
    name=e1.get()
    details=t1.get("1.0","end-1c")
    gender1=int(gender.get())
    selected_indexes=list1.curselection()
    index=selected_indexes[0]
    value=list1.get(index)
    weight=s1.get()
    codings=int(coding.get())
    sportss=int(sports.get())
    singings=int(singing.get())
    dancings=int(dancing.get())
    print(name)
    print(details)
    if gender1==1:
        print("Male")
    elif gender1==2:
        print("Female")
    else:
        print("Undefined")
    print(value)
    print(weight)
    print(codings)
    print(sportss)
    print(singings)
    print(dancings)

screen=tk.Tk()
screen.title("My First Screen")
screen.configure(bg="light blue")
screen.geometry("1500x1500")

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

gender=tk.IntVar()
r1=tk.Radiobutton(text="Male",value=1,variable=gender)
r1.place(x=300,y=350)

r2=tk.Radiobutton(text="Female",value=2,variable=gender)
r2.place(x=400,y=350)

l5=tk.Label(text="Select your hobbies:",width=15,height=1,bg="white",fg="black")
l5.place(x=50,y=450)

coding=tk.IntVar()
sports=tk.IntVar()
singing=tk.IntVar()
dancing=tk.IntVar()

c1=tk.Checkbutton(text="Coding",onvalue=1,offvalue=0,variable=coding)
c1.place(x=300,y=450)

c2=tk.Checkbutton(text="Sports",onvalue=1,offvalue=0,variable=sports)
c2.place(x=400,y=450)

c3=tk.Checkbutton(text="Singing",onvalue=1,offvalue=0,variable=singing)
c3.place(x=500,y=450)

c4=tk.Checkbutton(text="Dancing",onvalue=1,offvalue=0,variable=dancing)
c4.place(x=600,y=450)

l6=tk.Label(text="Enter your address:",width=15,height=1,bg="white",fg="black")
l6.place(x=50,y=550)

t2=tk.Text(width=30,height=3,bg="white",fg="blue")
t2.place(x=300,y=550)

l7=tk.Label(text="Choose your known languages:",width=25,height=1,bg="white",fg="black")
l7.place(x=50,y=650)

c5=tk.Checkbutton(text="English",onvalue=1,offvalue=0)
c5.place(x=300,y=650)

c6=tk.Checkbutton(text="Hindi",onvalue=1,offvalue=0)
c6.place(x=400,y=650)

c7=tk.Checkbutton(text="French",onvalue=1,offvalue=0)
c7.place(x=500,y=650)

b1=tk.Button(text="Submit",width=10,height=2,bg="green",fg="white",command=fetch_details)
b1.place(x=700,y=750)

grades=["1","2","3","4","5","6","7","8","9","10"]

l8=tk.Label(text="Select your grade:",width=15,height=1,bg="white",fg="black")
l8.place(x=50,y=700)

list1=tk.Listbox(width=20,height=3,bg="white",fg="black")
list1.place(x=50,y=740)
i=0
for item in grades:
    list1.insert(i,grades[i])
    i+=1

l9=tk.Label(text="Select your weight:",width=15,height=1,bg="white",fg="black")
l9.place(x=50,y=800)

s1=tk.Scale(from_=0,to=100,orient="horizontal")
s1.place(x=300,y=800)

scrollbar1=tk.Scrollbar(screen)
scrollbar1.pack(side=tk.RIGHT,fill=tk.Y)

screen.mainloop()