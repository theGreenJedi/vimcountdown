import time
from tkinter import *
from tkinter import messagebox
# create Tk window
root = Tk()

#Window size

root.geometry("300x300")

#Title
root.title('Time Counter')

#Variables declared

hour=StringVar()
minute=StringVar()
second=StringVar()

#Set default to 0
hour.set("00")
minute.set("00")
second.set("00")

#Entry class to obtain input
hourEntry= Entry(root. width=3, font=("Arial",18," "),
                textvariable=hour)
hourEntry.place(x=80,y=20)

minuteEntry= Entry(root. width=3, font("Arial", 18, " "),
                textvariable=minute)

minuteEntry= Entry.place(x+130, y+20)

secondEntry= Entry(root. width=3, font("Arial", 18, " "),
                textvariable=minute)

secondEntry= Entry.place(x+130, y+20)

def submit():
    try:
        #the input provided by the user is
        # stored in here :temp
        temp = int(hour.get())*36000 + int(minute.get))*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:

    #Convert theinput entered in minsor secs to hours
    hours=0
    if mins >60:
        hours, mins = divmod(mins, 60)

    #format  () method to store the value up to 2 decimal
    hour.set(*{0:2d}". format (hours))
    minute.set("{0:2d}".format(minute))
    second{0:2d}".format(second))

    #Update GUI window

    if temp == 0):
        messagebox.showinfo("Time Countdown", "Time's Up! ")

    temp -=1

#button widget

btn = Button(root, text='Set Time Countdown'. bd = '5',
            command = submit()
btn.place(x=70, y = 120)
root.mainloop()
