import datetime
import webbrowser
import os
import speech_recognition as sr

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening..')
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print(format(query))
    except:
        print("Cannot recognize! Try to type the command")
        query = str(input('Command: '))
    return query

def salam():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        print("Good Morning!")

    if currentH >= 12 and currentH < 18:
        print("Good Afternoon!")

    if currentH >= 18 and currentH !=0:
        print("Good Evening!")

def greet():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        print("Good Morning, "+ nama +"!")

    if currentH >= 12 and currentH < 18:
        print("Good Afternoon, "+ nama +"!")

    if currentH >= 18 and currentH !=0:
        print("Good Evening, "+ nama +"!")

salam()
print("Hello, I am Jarvis, I am your digital assistant")
print("Who are you?")

nama=command()

print("Hello, " + nama + "! How can I help you?")

while (True):

    query = command()
    
    if query == "open YouTube":
        webbrowser.open("http://youtube.com")
        print("opening www.youtube.com")

    elif query == "open Google":
        webbrowser.open("http://google.com")
        print("opening www.google.com")

    elif query == "open Facebook":
        webbrowser.open("http://facebook.com")
        print("opening www.facebook.com")

    elif query == "close browser":
        os.system("pkill chrome")
        print("chrome closed")

    elif query == "search":
        print("Google search: ")
        google = command()
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)

    elif query == "greet me":
        greet()

    elif query == "bye":
        break

    elif query == "hello":
        print("Hello, "+nama)

    else:
        print("Searching...Query cannot be found! Here are some references from Google")
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % query)
    
    print("Waiting for another command...")
        
print("Bye, have a good day.")
