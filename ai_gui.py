import tkinter as tk
import os
import wikipedia
import webbrowser
import datetime
import time

root = tk.Tk()


def input_command():
    if e.get() == "":
        label.config(text="", bg='white')
    elif e.get() == "discord" or e.get() == "open discord":
        os.startfile(path)
        label.config(text="opening discord")
    elif e.get() == "close discord" or e.get() == "discord off":
        try:
            os.system('TASKILL /F /IM discord.exe')
            label.config(text="closing discord")
        except Exception as error:
            label.config(text=error)

    elif e.get() == "time" or e.get() == "tell time":
        strtime = datetime.datetime.now().strftime("%H:%M")
        label.config(text=strtime)
    elif e.get() == "how are you" or e.get() == "are you ok":
        label.config(text="i am fine sir", fg='white', bg='black')
        how = True
        time.sleep(5)
        if how == True:
            label.config(text="how are you sir?", fg="yellow")
        else:
            label.config()



    else:
        label.config(text="sir i dont understand what the heck are you trying me to do", fg='red', bg='yellow')


def wishuser():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        label.config(text="good morning")

    elif hour >= 12 and hour < 18:
        label.config(text="good afternoon")
    else:
        label.config(text="good evening")

how = False
path = "C:\\Users\\User\\AppData\\Local\\Discord\\app-0.0.306\\Discord.exe"

e = tk.Entry()
e.pack()
btn = tk.Button(text="ok", bg='black', fg='white', command=input_command)
btn.pack()

label = tk.Label(fg='black', text="", bg='white')
label.pack()

wishuser()
root.title("Nooby bot")
root.mainloop()
