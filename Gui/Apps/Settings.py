# | Penguins Rock | #

from tkinter import *
from time import sleep

# added a basic idea of the start of settings that sends it's info into the "Water.py" files that we could #
# possibly draw from to change functions in our GUI permanently based on Water's contents #


root = Tk()
root.geometry('500x500')
divided = Entry(root, width=50)
root.title("DividedWater was here")
root.iconbitmap("Settings.png")
divided.pack()
wd = "Replace me with your file name"


def change_background():
    divided.insert(0, wd)
    done_button.pack()


def button2():
    open('../../Water.py', 'w')
    with open('../../Water.py', 'w') as water:
        water.write(f"Water = r\"{divided.get()}\"\n")
    done_button.forget()
    divided.insert(0, "successfully saved: ")
    sleep(1)
    divided.delete(0, END)


done_button = Button(root, text="press when done", command=button2)
background = Button(root, command=change_background, text="Change Background of Home")
background.pack()
mainloop()
