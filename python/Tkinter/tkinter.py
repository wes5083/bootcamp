from tkinter import *

window = Tk()  # instantiate an instance of a window
window.geometry("420x420")
window.title("GUI Program")
icon = PhotoImage(file='../Basic/python.png')
window.iconphoto(True, icon)
window.config(background="#5cfcff")

# label: an area widget that holds text and/or an image within a window
label = Label(window,
              text="Hello World",
              font=('Arial', 40, 'bold'),
              fg='green',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=icon,
              compound='bottom')  # top, right, left
label.pack()
label.place(x=0, y=0)  # position

window.mainloop()  # place window on computer screen, listen for events
