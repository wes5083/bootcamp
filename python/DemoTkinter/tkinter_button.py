from tkinter import *

count = 0


def click():
    global count
    count += 1
    print(count)
    print("You clicked the button!")


window = Tk()
icon = PhotoImage(file='python.png')
button = Button(window,
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
