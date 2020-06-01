# | Penguins Rock | #

import tkinter as tk
from time import sleep
from pathlib import Path

# added a basic idea of the start of settings that sends it's info into the "Water.py" files that we could #
# possibly draw from to change functions in our GUI permanently based on Water's contents #


# def THANK_GOD(): tried making thins work but using os.system i don't think that it's possible so I took it out #

root = tk.Tk()
root.geometry('500x500')
divided = tk.Entry(root, width=50)
root.title("DividedWater was here")
root.iconbitmap(Path("Settings"))
divided.pack()
wd = "Replace me with your file name"


def change_background():
    divided.insert(0, wd)
    done_button.pack()


def button2():
    open('Water.py', 'w')
    with open('Water.py', 'w') as water:
        water.write(f"import os.path\n\n\ndef water():\n    watt = \"{divided.get()}\"\n    if os.path.isfile(watt):\n "
                    f"       return watt\n    else:\n        return False\n")
    done_button.forget()
    divided.insert(0, "successfully saved: ")
    sleep(1)
    divided.delete(0, tk.END)


done_button = tk.Button(root, text="press when done", command=button2)
background = tk.Button(root, command=change_background, text="Change Background of Home")
background.pack()
tk.mainloop()
