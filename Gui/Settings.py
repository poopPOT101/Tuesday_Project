'''# | Penguins Rock | #'''
import tkinter as tk
from pathlib import Path
from glob import glob
from PIL import Image, ImageTk
import PIL

# added a basic idea of the start of settings that sends it's info into the "Water.py" files that we could #
# possibly draw from to change functions in our GUI permanently based on Water's contents #


# def THANK_GOD(): tried making thins work but using os.system i don't think that it's possible so I took it out #
def file_checker(file):
    path = str(Path('Gui/Images/*'))
    Files = glob(path)
    Files_Ext = []
    Files1 = []
    for file1 in Files:
        x, y = file1.split('Gui\Images\\')
        Files_Ext.append(y)
        without, ext = y.split('.')
        Files1.append(without)
        
    if file in Files1:
        return True
    elif file in Files_Ext:
        return True
    else:
        return False



### Root Window ###
root = tk.Tk()
root.title("Settings")
root.geometry('500x500')



"""
Change Background
"""
Background = ''
Background_Changed = False
###Entry Box For Changing Background###
Text_Box = tk.Entry(root, width=50)
Text_Box.pack()
TEXT = 'Enter File Name'
Text_Box.insert(0, TEXT)  #Defult Text#

###Button Command###
def change_background():

    if file_checker(Text_Box.get()) == False:
        print('You need to enter a file')

    else:                                                  
         if '.' in Text_Box.get():
             global Background_Changed
             global Background
             Background = Text_Box.get()

             PIL_image = PIL.Image.open(f'Gui\\Images\\{Text_Box.get()}')
             PIL_image.thumbnail((120,120))
             Background = PIL.ImageTk.PhotoImage(PIL_image)
             Background_Changed = True
             return Background

         else:
             print('Add file extension')

###Button##
background_button = tk.Button(root, command=change_background, text="Change Background of Home")
background_button.pack()
###Canvas###
if Background_Changed == True:
    Canvas = tk.Canvas(root, image=Background)
else:
    Canvas = tk.Canvas(root, bg = 'red')
Canvas.pack()
tk.mainloop()
