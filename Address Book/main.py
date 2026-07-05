from tkinter import *
from tkinter import messagebox

screen=Tk()
screen.geometry("1000x1000")
screen.title("Address Book")
screen.configure(bg="lightgrey")

result=""
index=0

def add_details():
    global result
    name=e1.get()
    address=t2.get("1.0","end-1c")
    mobile=e2.get()
    result="Name:: "+name+"|| Address:: "+address+"|| Mobile No.:: "+mobile
    file=open("Address Book/Address.txt","a")
    file.write("\n")
    file.write(result)
    file.close()
    e1.delete(0,END)
    e2.delete(0,END)
    t2.delete("1.0","end-1c")
    messagebox.showinfo("File updated","You have successfully saved the address")

def fetch_details():
    file=open("Address Book/Address.txt","r")
    file_content=file.read()
    file.close()
    address_list=file_content.split("\n")
    i=0
    for address in address_list:
        t1.insert(i,address)
        i+=1
def edit_details():
    global index
    selected_indices=t1.curselection()
    if selected_indices:
        index=selected_indices[0]
        selected_value=t1.get(index)
        selected_list=selected_value.split("|| ")
        e1.insert(0,selected_list[0].split(":: ")[1])
        t2.insert("1.0",selected_list[1].split(":: ")[1])
        e2.insert(0,selected_list[2].split(":: ")[1])

def update_details():
    global result,index
    name=e1.get()
    address=t2.get("1.0","end-1c")
    mobile=e2.get()
    result="Name:: "+name+"|| Address:: "+address+"|| Mobile No.:: "+mobile
    t1.delete(index)
    t1.insert(index,result)

def save_details():
    file=open("Address Book/Address.txt","w")
    final_result=""
    for item in t1.get(0,END):
        final_result=final_result+item+"\n"
    file.write(final_result)
    file.close()
    messagebox.showinfo("Operation Successful","Details have been saved!")

l1=Label(text="Address Book",width=25,height=3,fg="black",bg="lightgrey",font=('TKDefaultFont',20))
l1.place(x=300,y=20)

b1=Button(text="Open",width=20,height=2,fg="black",bg="lightgrey",font=('TKDefaultFont',12),command=fetch_details)
b1.place(x=400,y=150)

t1=Listbox(width=60,height=35,fg="black",bg="white",font=('TKDefaultFont',10),selectmode=SINGLE)
t1.place(x=10,y=250)

l2=Label(text="Name:",width=20,height=1,fg="black",bg="lightgrey",font=('TKDefaultFont',15))
l2.place(x=500,y=250)

e1=Entry(width=40,fg="black",bg="white")
e1.place(x=700,y=250)

l3=Label(text="Address:",width=20,height=1,fg="black",bg="lightgrey",font=('TKDefaultFont',15))
l3.place(x=500,y=400)

t2=Text(width=35,height=4,fg="black",bg="white")
t2.place(x=700,y=380)

l4=Label(text="Mobile No.:",width=20,height=1,fg="black",bg="lightgrey",font=('TKDefaultFont',15))
l4.place(x=500,y=550)

e2=Entry(width=40,fg="black",bg="white")
e2.place(x=700,y=550)

b4=Button(text="Edit",width=12,height=1,fg="black",bg="lightgrey",font=('TKDefaultFont',12),command=edit_details)
b4.place(x=500,y=650)

b2=Button(text="Add",width=12,height=1,fg="black",bg="lightgrey",font=('TKDefaultFont',12),command=add_details)
b2.place(x=900,y=650)

b3=Button(text="Save",width=50,height=1,fg="black",bg="lightgrey",font=('TKDefaultFont',12),command=save_details)
b3.place(x=250,y=850)

b5=Button(text="Update",width=12,height=1,fg="black",bg="lightgrey",font=('TKDefaultFont',12),command=update_details)
b5.place(x=700,y=650)

screen.mainloop()