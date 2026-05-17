import gtts
import os

text1=input("What do you want to convert to speech?")

speech=gtts.gTTS(text=text1,lang="en",slow=False)
speech.save("speech.mp3")

os.system("start speech.mp3")