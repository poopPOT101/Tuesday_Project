"""
Best Version of Gui So Far
"""

### Imports ###
import PIL
import tkinter as tk
from PIL import Image, ImageTk
import os
from pathlib import Path
import weakref

### Tkinter Root Window ###
root = tk.Tk()
#root = tk.toplevel()

### Canvases ###
Canvas1_Height = 480
Canvas1_Width = 720
Background1_Color = '#00E5B4'
Active_Background_Color = '#bdffed'
Button_Size = {'w': 125, 'h': 125}
#Button_Size = 125, 125
main_canvas = tk.Canvas(root,
                        height=Canvas1_Height, #Canvas Height#
                        width=Canvas1_Width, #Canvas Width#
                        bg=Background1_Color) #Canvas Background Color#
main_canvas.pack()

### Frame ###
Display_Bar_Color = '#00b584'
Display_Bar = tk.Frame(main_canvas,
                       bg=Display_Bar_Color
                       )
Display_Bar.place(relwidth=1,
                  relheight=.1,
                  relx=0,
                  rely=0
                  )
### App Class And App List ###
class App:
    App_Positions = {
                     'top_left': (.1,.2), 'top_middle': (.4, .2)   , 'top_right':(.7, .2),
                     'bottom_lef':(.1, .6), 'bottom_middle':(.4,.6), 'bottom_right':(.7, .6)
                    }
    App_List = {}
    def __init__(self, icon_path=None, description=None, width=125, height=125, name=None, exe=None):
        self.Exe = exe
        self.Icon_Path = Path(icon_path)
        self.Description = description
        self.Width = width
        self.Height = height
        self.size = (width, height)
        self.Name = name
        self.icon_path = icon_path
        App.App_List.update({repr(self): self.Name})

        ### Initializing Icon For Each Object ###
        self.PIL_image = PIL.Image.open(self.Icon_Path)
        self.PIL_image.thumbnail(self.size)
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

        for index in range(len(App.App_List)):
            if index == 0:
                self.Button.place(relx=App.App_Positions['top_left'][0], rely=App.App_Positions['top_left'][1])
            elif index == 1:
                self.Button.place(relx=App.App_Positions['top_middle'][0], rely=App.App_Positions['top_middle'][1])
            elif index == 2:
                self.Button.place(relx=App.App_Positions['top_right'][0], rely=App.App_Positions['top_right'][1])
            elif index == 3:
                self.Button.place(relx=App.App_Positions['bottom_lef'][0], rely=App.App_Positions['bottom_lef'][1])
            elif index == 4:
                self.Button.place(relx=App.App_Positions['bottom_middle'][0], rely=App.App_Positions['bottom_middle'][1])
            elif index == 5:
                self.Button.place(relx=App.App_Positions['bottom_right'][0], rely=App.App_Positions['bottom_right'][1])
            else:
                break
                pass

    def __repr__(self):
        return f'{self.Name} = App(icon_path={self.icon_path}, description={self.Description}, name={self.Name}, exe={self.Exe}'


Settings = App(icon_path='Gui/Images/Settings.png', description='Play With Tuesdays Settings ;) ', name='Settings')
Strunes = App(icon_path='Gui/Images/Music_Icon.png', description='To Jam Out When You are Likely a Lonely Loser', name='Strunes', exe='iTunes')
Clock = App(icon_path='Gui/Images/Clock.png', description='To Wake Yo Stupid Ass Up', name='Clock')
Desktop = App(icon_path='Gui/Images/Desktop_Icon.png' , description = 'to get to the desktop', name='Desktop' )
Tuesday = App(icon_path='Gui/Images/AI.png', description='For all your robot needs', name='Tuesday')
Weather = App(icon_path='Gui/Images/Weather_Icon.png', description='An App for Weather... lol', name='Weather')

'''
Clock.Create_App()
Tuesday.Create_App()
Weather.Create_App()
Settings.Create_App()
Strunes.Create_App()
'''


root.mainloop()
