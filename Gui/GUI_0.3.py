'''
Best Version of Gui So Far
'''

'''
Imports
'''
### Imports ###
import PIL
import tkinter as tk
from PIL import Image, ImageTk
import os
from pathlib import Path


# | Logger | #
def logger(function):
    import logging
    logging.basicConfig(filename=f'{function.__name__}', level=logging.INFO)

    def inner(*args, **kwargs):
        logging.info(f"ran with {args} and {kwargs}")
        return function(*args, **kwargs)

    return inner
'''
-------
Widgets
-------
'''
### Tkinter Root Window ###
window_h = 480  #window height#
window_w = 720  #window width#
#root = tk.toplevel()  #In the case of weird bug that sometimes occours#
root = tk.Tk()  #Actual Root#
root.geometry(f"{window_w}x{window_h}") # Window Size = 'widthxheight' #

# Window Title and window icon image #
root.title("Tuesday's GUI")
#root.iconbitmap(Path('Gui/Images/Window_Icon'))


### The top toolbar for time battery ect ###
displaybar_h = window_h*.1   #height#
displaybar_w = window_w*1    #width#
Display_Bar_Color = '#00b584' #darker mint green#
#Display Bar#
Display_Bar = tk.Frame(root,
                       bg=Display_Bar_Color,
                       height=displaybar_h
                       )
Display_Bar.pack(fill='x', side='top') #placing on top of window#


### Canvases ###
Canvas1_Height = window_h*1-displaybar_h  #height#
Canvas1_Width = window_w*1                #width#
Background1_Color = '#00E5B4'             #mint green#
Active_Background_Color = '#bdffed'       #when clicked darker mint green#
Button_Size = {'w': window_w*.174, 'h': window_h*.29}   #percent of window w and h#
#Canvas#
main_canvas = tk.Canvas(root,
                        bg=Background1_Color)
main_canvas.pack(fill='both', expand=True)   #fills height and width of canvas to window - top bar#

'''
Not Work

main_canvas.create_image(Canvas1_Width, Canvas1_Height, image=Water.water if Water is True else None)
main_canvas.image = Water.water
'''


'''
-----------------
Classes and Stuff
------------------
'''
### App Class And App List ###
class App:
    App_Positions = {
                     'top_left': (.1, .2), 'top_middle': (.4, .2), 'top_right': (.7, .2),
                     'bottom_left': (.1, .6), 'bottom_middle': (.4, .6), 'bottom_right': (.7, .6)
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
                                command=lambda: os.system(f"{self.Exe}") if self.Executable else None
                                )
    
    def __repr__(self):  #repr()#
        return f'{self.Name} = App(icon_path={self.icon_path}, description={self.Description}, name={self.Name}, exe={self.Exe}'

    def __str__(self):   #str()#
        return f'The Application Name is: {self.Name} \nThe Description is: {self.Description}'


    @staticmethod
    def Create_App():  #initiate all apps onto screen#
        for index, object in enumerate(App.Object_List):
            if index == 0:
                object.Button.place(relx=App.App_Positions['top_left'][0], rely=App.App_Positions['top_left'][1])
            elif index == 1:
                object.Button.place(relx=App.App_Positions['top_middle'][0], rely=App.App_Positions['top_middle'][1])
            elif index == 2:
                object.Button.place(relx=App.App_Positions['top_right'][0], rely=App.App_Positions['top_right'][1])
            elif index == 3:
                object.Button.place(relx=App.App_Positions['bottom_left'][0], rely=App.App_Positions['bottom_left'][1])
            elif index == 4:
                object.Button.place(relx=App.App_Positions['bottom_middle'][0], rely=App.App_Positions['bottom_middle'][1])
            elif index == 5:
                object.Button.place(relx=App.App_Positions['bottom_right'][0], rely=App.App_Positions['bottom_right'][1])
            else:
                break
                pass



Settings = App(icon_path='Gui/Images/Settings.png', description='Play With Tuesdays Settings ;) ', name='Settings')
Strunes = App(icon_path='Gui/Images/Music_Icon.png', description='To Jam Out When You are Likely a Lonely Loser', name='Strunes')
Clock = App(icon_path='Gui/Images/Clock.png', description='To Wake Yo Stupid Ass Up', name='Clock')
Desktop = App(icon_path='Gui/Images/Desktop_Icon.png', description='to get to the desktop', name='Desktop')
Tuesday = App(icon_path='Gui/Images/AI.png', description='For all your robot needs', name='Tuesday')
Weather = App(icon_path='Gui/Images/Weather_Icon.png', description='An App for Weather... lol', name='Weather')





def execute_file():
    App.Create_App()
    root.mainloop()


execute_file()
