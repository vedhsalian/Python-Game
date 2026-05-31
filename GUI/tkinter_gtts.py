from tkinter import *
import gtts
import os

def text_to_speech():
    text1=t1.get("1.0", "end-1c")

    speech=gtts.gTTS(text=text1,lang="en",slow=False)
    speech.save("speech.mp3")

    os.system("start speech.mp3")

def clear_text():
    t1.delete("1.0",END)

screen=Tk()
screen.configure(bg="lightgrey")
screen.title("Text to Speech Converter")
screen.geometry("600x600")

l1=Label(text="Google Text to Speech",width=25,height=3,fg="black",bg="lightgrey",font=('TKDefaultFont',20))
l1.place(x=100,y=50)

l2=Label(text="Enter your text here: ",width=20,height=1,fg="black",bg="lightgrey",font=('TKDefaultFont',15))
l2.place(x=100,y=200)

t1=Text(width=30,height=3,fg="blue",bg="white")
t1.place(x=300,y=200)

b1=Button(text="Convert",width=20,height=2,fg="black",bg="green",command=text_to_speech)
b1.place(x=150,y=300)

b2=Button(text="Clear",width=20,height=2,fg="black",bg="orange",command=clear_text)
b2.place(x=350,y=300)

screen.mainloop()