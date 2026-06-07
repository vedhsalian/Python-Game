from tkinter import *
from tkinter import messagebox

def calculate_grade():
    global result
    math=int(e3.get())
    english=int(e4.get())
    science=int(e5.get())
    marksobtained=math+english+science
    percentage=(marksobtained/300)*100
    if percentage>=80:
        grade="A"
    elif percentage>=60 and percentage<80:
        grade="B"
    elif percentage>=50 and percentage<60:
        grade="C"
    elif percentage>=40 and percentage<50:
        grade="D"
    else:
        grade="F"
    name=e1.get()
    number=e2.get()
    result="Name: "+name+", Roll No.: "+number+", Percentage: "+str(percentage)+"%, Grade: "+grade+"\n"
    t1.insert(END,result)

def save_text():
    global result
    file=open("GUI/student_grade.txt","a")
    file.write("\n")
    file.write(result)
    file.close()
    messagebox.showinfo("Operation successful","Details Saved")

def clear_text():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    t1.delete("1.0","end-1c")

screen=Tk()
screen.geometry("500x800")
screen.configure(bg="lightgrey")
screen.title("Student Grading System")

l1=Label(text="Student Grading System",width=20,height=3,fg="black",bg="lightgrey",font=('TKDefaultFont',15))
l1.place(x=150,y=40)

l2=Label(text="Enter your name:",width=15,height=1,fg="black",bg="lightgrey")
l2.place(x=100,y=120)

e1=Entry(width=20,fg="black",bg="white")
e1.place(x=300,y=120)

l3=Label(text="Enter your roll number:",width=20,height=1,fg="black",bg="lightgrey")
l3.place(x=100,y=190)

e2=Entry(width=10,fg="black",bg="white")
e2.place(x=300,y=190)

l4=Label(text="Enter your Math marks:",width=20,height=1,fg="black",bg="lightgrey")
l4.place(x=100,y=260)

e3=Entry(width=10,fg="black",bg="white")
e3.place(x=300,y=260)

l5=Label(text="Enter your English marks:",width=20,height=1,fg="black",bg="lightgrey")
l5.place(x=100,y=330)

e4=Entry(width=10,fg="black",bg="white")
e4.place(x=300,y=330)

l6=Label(text="Enter your Science marks:",width=20,height=1,fg="black",bg="lightgrey")
l6.place(x=100,y=400)

e5=Entry(width=10,fg="black",bg="white")
e5.place(x=300,y=400)

b1=Button(text="Calculate grade",width=16,height=2,fg="black",bg="green",command=calculate_grade)
b1.place(x=50,y=450)

b2=Button(text="Clear text",width=16,height=2,fg="black",bg="red",command=clear_text)
b2.place(x=200,y=450)

b3=Button(text="Save text",width=16,height=2,fg="black",bg="orange",command=save_text)
b3.place(x=350,y=450)

t1=Text(width=50,height=5,fg="black",bg="white")
t1.place(x=50,y=550)

screen.mainloop()