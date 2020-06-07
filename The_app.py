import tkinter as tk
import pyttsx3
import datetime
import speech_recognition


engiene = pyttsx3.init('sapi5')
voices = engiene.getProperty('voices')
print(voices[0].id)
engiene.setProperty('voice', voices[0].id)

def wishuser():
	hour = int(datetime.datetime.now().hour)

	if hour>= 0 and  hour<12:
		speak("Good morning user")
	elif hour>=12 and hour<18:
		speak("Good after noon user")
	else:
		speak("Good   evening   user")
	speak("Hi i am gamer bot   how can i help you?")




def speak(audio):
	engiene.say(audio)
	engiene.runAndWait()

if __name__ == "__main__":
		wishuser()



