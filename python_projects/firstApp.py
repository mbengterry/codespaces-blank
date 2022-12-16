from tkinter import *
from tkinter.ttk import *
import pyglet
from pyglet import font

from datetime import datetime

col1 = "#3d3d3d"
col2 = "#21c25c"

root = Tk()
root.title("Clock")
root.geometry('350x180')
root.resizable(width=FALSE, height=FALSE)
root.configure(background=col1)

def clock():
    time = datetime.now()
    hour = time.strftime("H:%M:%S")
    weekday = time.strftime("%A")
    day = time.day
    month = time.strftime("%b")
    year = time.strftime("%Y")

    l1.config(text=hour)
    l.after(200, clock)

    l2.config(text=weekday + "" + str(day) + "/" + str(month) + "/" + str(year))

l1 = Label(root, font=('digit-780'), background=col1, foreground=col2)
l1.grid(row=0, column=0, sticky=NW)

l2 = Label(root, font=('digit-720'), background=col1, foreground=col2)
l2.grid(row=1, column=0, sticky=NW)

clock()
root.mainloop()