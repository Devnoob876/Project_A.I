import tkinter as tk
import os
import wikipedia
import webbrowser
import datetime

root = tk.Tk()


e = tk.Entry()
all_input = e.get()
e.pack()

btn = tk.Button(text="ok", bg='black', fg='white')

btn.pack()

def command_input():
    if all_input == "hey":
      print("fuq u ")
def wishuser():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        label = tk.Label(root, text="good morning user", fg='red')
        label.pack()

    elif hour >= 12 and hour < 18:
        label = tk.Label(root, text="good after noon user", fg='red')
        label.pack()

    else:
      label = tk.Label(root, text="good evening user", fg='red')
      label.pack()







root.title("Nooby bot")











if __name__ == "__main__":
    wishuser()
    root.mainloop()
    command_input()


