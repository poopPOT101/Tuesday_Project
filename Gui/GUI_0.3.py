"""
Best Version of Gui So Far
"""

### Imports ###
import PIL
import tkinter as tk
from PIL import Image, ImageTk


### Tkinter Root Window ###
root = tk.Tk()

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
    App_List = []
#    App_Positions = {
#                     'top_left':None, 'top_middle':None   , 'top_right':None,
#                     'bottom_lef':None, 'bottom_middle':None, 'bottom_right':None
#                    }

    def __init__(self, icon=None, description=None, width=120, height=120, name=None):
        self.Icon_Path = icon
        self.Description = description
        self.Width = width
        self.Height = height
        self.size = (width, height)
        self.Name = name
        ### Initializing Icon For Each Object ###
        self.PIL_image = PIL.Image.open(self.Icon_Path)
        self.PIL_image.thumbnail(self.size)
        self.Icon = PIL.ImageTk.PhotoImage(self.PIL_image)
        App.App_List.append(self.Name)
        self.Button = tk.Button(root,
                               image=self.Icon,
                               borderwidth=0,
                               height=Button_Size['h'],
                               width=Button_Size['w'],
                               activebackground=Active_Background_Color, bg=Background1_Color)
        for index in range(len(App.App_List)):
            if index == 0:
                 self.Button.place(relx=.1, rely=.2)
            elif index == 1:
                self.Button.place(relx=.4, rely=.2)
            elif index == 2:
                self.Button.place(relx=.7, rely=.2)
            elif index == 3:
                self.Button.place(relx=.1, rely=.6)
            elif index == 4:
                self.Button.place(relx=.4, rely=.6)
            else:
                self.Button.place(relx=.7, rely=.6)



Tuesday = App('Gui\\Images\\AI.png', description='For all your robot needs', name='Tuesday')
Weather = App('Gui\\Images\\Weather_Icon.png', description='An App for Weather... lol', name='Weather')
Settings = App('Gui\\Images\\Settings.png', description='Play With Tuesdays Settings ;) ', name='Settings')
Strunes = App('Gui\\Images\\Music_Icon.png', description='To Jam Out When You are Likely a Lonely Loser', name='Strunes')
Clock = App('Gui\\Images\\Clock.png', description='To Wake Yo Stupid Ass Up', name='Clock')
'''
Clock.Create_App()
Tuesday.Create_App()
Weather.Create_App()
Settings.Create_App()
Strunes.Create_App()
'''


root.mainloop()
