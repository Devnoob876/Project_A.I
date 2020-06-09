import tkinter as tk
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


url = "www.google.com"


engiene = pyttsx3.init('sapi5')
voices = engiene.getProperty('voices')

engiene.setProperty('voice', voices[0].id)


def wishuser():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning user")
    elif hour >= 12 and hour < 18:
        speak("Good after noon user")
    else:
        speak("Good   evening   user")
    speak("Hi i am your personal assistant how can i help you?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        return "none"
    return query


def speak(audio):
    try:
     engiene.say(audio)
     engiene.runAndWait()
    except Exception as tortise:
        print(tortise)







if __name__ == "__main__":
    wishuser()

    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak("I am searching to wikipedia...please wait for sometime")

            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia..")
            speak(results)
        elif 'open google' in query:


            speak("opening google")


            webbrowser.get(using='google-chrome').open(url)
        elif 'who are you' in query:

            speak("i am Nooby bot to help you with your pc and i am your personal assistant")
            print("iama booooot")
        elif 'how are you' in query:

            speak("i am doing great sir")

        elif 'discord' in query:
            try:

              speak("i m opening discord please wait for some time.....")
              discord = "C:\\Users\\User\\AppData\\Local\\Discord\\app-0.0.306\\Discord.exe"
              os.startfile(discord)
            except Exception as error:
                print(error)
                speak(error)
        elif 'close app' in query:
            try:
              os.system('TASKILL /F /IM Discord.exe')
            except Exception as error:
                print(error)
                speak(error)


        elif 'time' in query:

            strtime = datetime.datetime.now().strftime("%H:%M")
            speak(strtime)
            print(strtime)
        elif 'exit' in query:
            speak("i am very happy to serve you")
            speak("you can call me anytime")

        elif 'pycharm' in query:
            try:
              speak("opening pycharm please kindly wait for sometimes....")
              pycharm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.1\\bin\\pycharm64.exe"
              os.open(pycharm)
            except Exception as error:
                print(error)
                speak(error)

        elif 'close pycharm' in query:
            try:
              os.system('TASKILL /F /IM pycharm64.exe')
            except Exception as error:
                print(error)
                speak(error)

        elif 'close chrome' in query:
            try:
              os.system('TASKILL /F /IM chrome.exe')
            except Exception as error:
                print(error)
                speak(error)

        else:
            speak("i dont understand what you commanded ")
            speak("please make sure you read the instruction")





