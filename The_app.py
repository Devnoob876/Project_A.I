import tkinter as tk
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('hi')
trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    "chatterbot.corpus.english"
)

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
    engiene.say(audio)
    engiene.runAndWait()



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

            webbrowser.open("google.com")
        elif 'who are you' in query:

            speak("test")
            print("iama booooot")


        elif 'discord' in query:
            speak("i m opening discord please wait for some time.....")
            discord = "C:\\Users\\User\\AppData\\Local\\Discord\\app-0.0.306\\Discord.exe"
            os.startfile(discord)
        elif 'close app' in query:
            os.system('TASKKILL /F /IM discord.exe')

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M")
            speak(strtime)
            print(strtime)
        elif 'exit' in query:
            speak("i am very happy to serve you")
            speak("you can call me anytime")
            exit()
        else:
            speak(bot.get_response(query))
##############################################     ORTSPOON UPDATES.

            
##############################################     COMMANDS :

        # OPERATIONS : 1 + 1
        # CONVERTING : G TO KG
        # TURN ON WIFI / BLUETHOOTH
        # SHUTDOWN
        # CHANGE BRIGHTNESS
        # GET WHEATHER
        # PLAY A YOUTUBE VIDEO
        # SET ALARME
        # SEND GMAIL TO SOMEONE
        # PLAY MUSIC
        # SET TIMER
        # TRANSLATE A PHRASE


##############################################     QUESTIONS :

