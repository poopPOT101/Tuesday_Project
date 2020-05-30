"""
Best Version of Gui So Far
"""

# | I'm a Vandal | #

### Imports ###
import PIL
import tkinter as tk
from PIL import Image, ImageTk
import os
from pathlib import Path
import weakref
from time import sleep

'''
-------
Widgets
-------
'''
### Tkinter Root Window ###
window_h=480
window_w=720
root = tk.Tk()
root.geometry(f"{window_w}x{window_h}")
root.resizable()
#root = tk.toplevel()

### Frame ###
displaybar_h = window_h*.1
displaybar_w = window_w*1
Display_Bar_Color = '#00b584'
Display_Bar = tk.Frame(root,
                       bg=Display_Bar_Color,
                       height=displaybar_h
                       )
Display_Bar.pack(fill='x', side='top')
### Canvases ###
Canvas1_Height = window_h*1-displaybar_h
Canvas1_Width = window_w*1
Background1_Color = '#00E5B4'
Active_Background_Color = '#bdffed'
Button_Size = {'w': window_w*.174, 'h': window_h*.29}
#Button_Size = 125, 125
main_canvas = tk.Canvas(root,#Canvas Height = fill# #Canvas Width = fill#
                        bg=Background1_Color) #Canvas Background Color#
main_canvas.pack(fill='both', expand=True)

# added name instead of opening as tk #
root.title("Tuesday's GUI")

# main_canvas.pack()
# main_canvas.update()

'''
-----------------
Classes and Stuff
------------------
'''
### App Class And App List ###


class App:
    App_Positions = {
                     'top_left': (.1, .2), 'top_middle': (.4, .2), 'top_right': (.7, .2),
                     'bottom_lef': (.1, .6), 'bottom_middle': (.4, .6), 'bottom_right': (.7, .6)
                    }
    App_List = {}
    Object_List = []

    def __init__(self, icon_path=None, description=None, width=Button_Size['h'], height=Button_Size['w'], name=None, exe=None):
        self.Exe = exe
        self.Icon_Path = Path(icon_path)
        self.Description = description
        self.Width = width
        self.Height = height
        self.Size = (width, height)
        self.Name = name
        self.icon_path = icon_path
        App.App_List.update({repr(self): self.Name})
        App.Object_List.append(self)

        ### Initializing Icon For Each Object ###
        self.PIL_image = PIL.Image.open(self.Icon_Path)
        self.PIL_image.thumbnail(self.Size)
        self.Icon = PIL.ImageTk.PhotoImage(self.PIL_image)

        ### Initializing The Command ###
        self.Executable = True if self.Exe is not None else False
        ### Initializing The Button ###
        self.Button = tk.Button(root,
                                image=self.Icon,
                                borderwidth=0,
                                height=Button_Size['h'],
                                width=Button_Size['w'],
                                activebackground=Active_Background_Color,
                                bg=Background1_Color,
                                command=lambda: os.system(f"start {self.Exe}") if self.Executable else None
                                )

    def __repr__(self):
        return f'{self.Name} = App(icon_path={self.icon_path}, description={self.Description}, name={self.Name}, exe={self.Exe}'

    def __str__(self):
        return f'The Application Name is: {self.Name} \nThe Description is: {self.Description}'

    def updater(self):
        self.size =

    @staticmethod
    def Create_App():
        for index, object in enumerate(App.Object_List):
            if index == 0:
                object.Button.place(relx=App.App_Positions['top_left'][0], rely=App.App_Positions['top_left'][1])
            elif index == 1:
                object.Button.place(relx=App.App_Positions['top_middle'][0], rely=App.App_Positions['top_middle'][1])
            elif index == 2:
                object.Button.place(relx=App.App_Positions['top_right'][0], rely=App.App_Positions['top_right'][1])
            elif index == 3:
                object.Button.place(relx=App.App_Positions['bottom_lef'][0], rely=App.App_Positions['bottom_lef'][1])
            elif index == 4:
                object.Button.place(relx=App.App_Positions['bottom_middle'][0], rely=App.App_Positions['bottom_middle'][1])
            elif index == 5:
                object.Button.place(relx=App.App_Positions['bottom_right'][0], rely=App.App_Positions['bottom_right'][1])
            else:
                break
                pass


Settings = App(icon_path='Images/Settings.png', description='Play With Tuesdays Settings ;) ', name='Settings')
Strunes = App(icon_path='Images/Music_Icon.png', description='To Jam Out When You are Likely a Lonely Loser', name='Strunes', exe='iTunes')
Clock = App(icon_path='Images/Clock.png', description='To Wake Yo Stupid Ass Up', name='Clock')
Desktop = App(icon_path='Images/Desktop_Icon.png' , description = 'to get to the desktop', name='Desktop' )
Tuesday = App(icon_path='Images/AI.png', description='For all your robot needs', name='Tuesday')
Weather = App(icon_path='Images/Weather_Icon.png', description='An App for Weather... lol', name='Weather')


# | added logger | #
def logger(function):
    import logging
    logging.basicConfig(filename=f'{function.__name__}', level=logging.INFO)

    def inner(*args, **kwargs):
        logging.info(f"ran with {args} and {kwargs}")
        return function(*args, **kwargs)

    return inner


# @logger
def execute_file():
    App.Create_App()
    root.mainloop()


execute_file()
