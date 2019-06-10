import datetime
import webbrowser
import os
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Your Text")
# engine.runAndWait()
# os.system("say 'Your Command'")

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
nama = input()
print("Hello, " + nama + "! How can I help you?")

while (True):
    query = input()
    
    if query == "open youtube":
        webbrowser.open("http://youtube.com")
        print("opening www.youtube.com")

    elif query == "open google":
        webbrowser.open("http://google.com")
        print("opening www.google.com")

    elif query == "open facebook":
        webbrowser.open("http://facebook.com")
        print("opening www.facebook.com")

    elif query == "close browser":
        os.system("pkill chrome")
        print("chrome closed")

    elif query == "search":
        google = input("Google search: ")
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)

    elif query == "greet me":
        greet()

    elif query == "end":
        break

    elif query == "hello":
        print("Hello, "+nama)

    else:
        print("Searching...Query cannot be found")
    
    print("Waiting for another command...")
        
print("Bye, have a good day.")
