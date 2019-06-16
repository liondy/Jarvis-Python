import datetime
import webbrowser
import os
import speech_recognition as sr
from gtts import gTTS
from time import ctime

def speak(audio):
    tts = gTTS(text=audio, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)
    query=""
    try:
        query = r.recognize_google(audio)
        print(format(query))
    except:
        speak("Cannot recognize! Try to type the command")
        query = str(input('Command: '))
    return query

def salam():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak("Good Morning!")

    if currentH >= 12 and currentH < 18:
        speak("Good Afternoon!")

    if currentH >= 18 and currentH !=0:
        speak("Good Evening!")

def greet():
    currentH = int(datetime.datetime.now().hour)
    speak("Hello")
    if currentH >= 0 and currentH < 12:
        speak("Good Morning, "+ nama +"!")

    if currentH >= 12 and currentH < 18:
        speak("Good Afternoon, "+ nama +"!")

    if currentH >= 18 and currentH !=0:
        speak("Good Evening, "+ nama +"!")

def jarvis(query):
    if "how are you" in query:
        speak("I am fine")

    elif "time" in query:
        speak(ctime())
    
    elif "where is" in query or "where are" in query:
        query = query.split(" ")
        location = query[2]
        speak("Hold on "+ nama + ", I will show you where " + location + " is.")
        webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")

    elif "open" in query:
        query = query.split(" ")
        web = query[1]
        webbrowser.open("http://"+web+".com")
        speak("opening"+web+".com")

    elif "close browser" in query:
        os.system("pkill chrome")
        speak("chrome closed")

    elif "search" in query:
        speak("Google search: ")
        google = command()
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)

    elif "hello" in query:
        greet()

    elif "name" in query:
        speak("Hello "+nama+", my name is Jarvis")

    else:
        speak("Searching...Query cannot be found! Here are some references from Google")
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % query)

salam()
speak("Hello, I am Jarvis, I am your digital assistant")
speak("Tell me your name")

nama=command()

speak("Hello, " + nama + "! How can I help you?")

while (True):
    query = command()
    if "bye" in query or "goodbye" in query or "enough" in query:
        break
    jarvis(query)
    speak("Waiting for another command..")
        
speak("Goodbye"+nama+", have a good day.")
