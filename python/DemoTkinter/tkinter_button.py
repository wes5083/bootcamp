import tkinter
from tkinter.constants import *
count = 0

def click():
    global count
    count += 1
    print(count)
    print("You clicked the button!")


window = tkinter.Tk()
icon = tkinter.PhotoImage(file='python.png')
button = tkinter.Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,  # DISABLED
                image=icon,
                compound="bottom")
button.pack()

window.mainloop()
