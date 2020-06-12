import tkinter as tk
import os
import wikipedia
import webbrowser
import datetime
import time


root = tk.Tk()




def input_command():

    if e.get() == "":
        label.config(text="how are you sir??")

        question = True

        while blank  in e.get() and question == True:
          label.config(text="sir i have asked you a qusfsf")








def wishuser():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
       label.config(text="good morning")

    elif hour >= 12 and hour < 18:
       label.config(text="good afternoon")
    else:
      label.config(text="good evening")


e = tk.Entry()

e.pack()
btn = tk.Button(text="ok", bg='black', fg='white', command=input_command)
btn.pack()

label = tk.Label(fg='black', text="")
label.pack()

blank = ""

question = False

wishuser()
root.title("Nooby bot")
root.mainloop()






