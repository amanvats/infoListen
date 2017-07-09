
import wikipedia       #https://pypi.python.org/pypi/wikipedia/
from gtts import gTTS
import os


topic = input("Enter the topic you want to hear about: ")
lang = input("Enter your preferred language(Hindi/English): ")

#function to handle request to listen in hindi language


def hindi():
    wikipedia.set_lang("hi")
    info = wikipedia.summary(topic, sentences=1)
    language = 'hi'       #for hindi audio by gTTS
    myObj = gTTS(text=info, lang=language, slow=False)
    myObj.save("go.mp3")
    os.system("go.mp3")

#function to handle request to listen in english language


def eng():
    wikipedia.set_lang("en")
    info = wikipedia.summary(topic, sentences=2)
    language = 'en'
    myObj = gTTS(text=info, lang=language, slow=False)
    myObj.save("go.mp3")
    os.system("go.mp3")

if lang == "hindi" or lang == "Hindi" or lang == "HINDI":
    hindi()
else:
    eng()

#Aman Vats Creation

