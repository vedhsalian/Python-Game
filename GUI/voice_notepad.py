from tkinter import *
import speech_recognition as sr

def record_speech():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audiodata=r.listen(source)
        try:
            textdata=r.recognize_google(audiodata)
            t1.insert(END,textdata)
        except sr.UnknownValueError:
            print("Can't understand this line")

def save_text():
    text1=t1.get("1.0","end-1c")
    file=open("GUI/stt.txt","a")
    file.write("\n")
    file.write(text1)
    file.close()

def read_text():
    file=open("GUI/stt.txt","r")
    t2.delete("1.0","end-1c")
    file_content=file.read()
    t2.insert(END,file_content)
    file.close()

def clear_text():
    t1.delete("1.0",END)

screen=Tk()
screen.configure(bg="lightgrey")
screen.title("Voice Notepad")
screen.geometry("1000x500")

l1=Label(text="Voice Notepad",width=20,height=3,fg="black",bg="lightgrey",font=('TKDefaultFont',20))
l1.place(x=350,y=20)

b1=Button(text="Click me to start recording",width=20,height=2,fg="black",bg="grey",font=('TKDefaultFont',12),command=record_speech)
b1.place(x=100,y=180)

t1=Text(width=50,height=8,fg="black",bg="white")
t1.place(x=300,y=150)

b2=Button(text="Save text",width=20,height=2,fg="black",bg="lime",command=save_text)
b2.place(x=720,y=150)

b3=Button(text="Clear text",width=20,height=2,fg="black",bg="orange",command=clear_text)
b3.place(x=720,y=195)

b4=Button(text="Read text",width=20,height=2,fg="black",bg="red",command=read_text)
b4.place(x=720,y=240)

t2=Text(width=80,height=10,fg="black",bg="white")
t2.place(x=180,y=300)

screen.mainloop()