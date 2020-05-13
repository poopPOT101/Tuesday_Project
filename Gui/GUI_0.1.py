"""
Testing the GUI concept
"""
import os
import PIL
import tkinter as tk
from PIL import Image, ImageTk

BG_COLOR = '#00E5B4'
ACTIVE_BG_COLOR = '#bdffed'
DISPLAY_BAR_COLOR = '#00b584'
SETTINGS_BUTTON_SIZE = 125, 125
HEIGHT = 480
WIDTH = 720

# root = tk.Toplevel()
root = tk.Tk()

main_canvas = tk.Canvas(root, height=HEIGHT,
                        width=WIDTH,
                        bg=BG_COLOR)
main_canvas.pack()

# Frame#

display_bar = tk.Frame(main_canvas, bg=DISPLAY_BAR_COLOR)
display_bar.place(relwidth=1, relheight=0.1, relx=0., rely=0)

"""
APPS
"""

# Application One (Settings)#
PIL_image = PIL.Image.open('Gui\\Images\\Settings.png')
PIL_image.thumbnail(SETTINGS_BUTTON_SIZE)
image = PIL.ImageTk.PhotoImage(PIL_image)


open_app_1 = tk.Button(root,
                       image=image,
                       borderwidth=0,
                       height=SETTINGS_BUTTON_SIZE[0],
                       width=SETTINGS_BUTTON_SIZE[1],
                       activebackground=ACTIVE_BG_COLOR, bg=BG_COLOR)
open_app_1.place(relx=.1, rely=.2)

# Application Two (Weather)#
PIL_image2 = PIL.Image.open('Gui\\Images\\Weather_Icon.png')
PIL_image2.thumbnail((120,120))
image2 = PIL.ImageTk.PhotoImage(PIL_image2)

open_app_2 = tk.Button(root,
                       image=image2,
                       borderwidth=0,
                       height=SETTINGS_BUTTON_SIZE[0],
                       width=SETTINGS_BUTTON_SIZE[1],
                       activebackground=ACTIVE_BG_COLOR, bg=BG_COLOR)
open_app_2.place(relx=.4, rely=.2)

# Application Three (Tuesday)#
PIL_image3 = PIL.Image.open('Gui\\Images\\AI.png')
PIL_image3.thumbnail((140,140))
image3 = PIL.ImageTk.PhotoImage(PIL_image3)

open_app_3 = tk.Button(root,
                       image=image3,
                       borderwidth=0,
                       height=SETTINGS_BUTTON_SIZE[0],
                       width=SETTINGS_BUTTON_SIZE[1],
                       activebackground=ACTIVE_BG_COLOR, bg=BG_COLOR)
open_app_3.place(relx=.7, rely=.2)

# Application Four (Clock)#
PIL_image4 = PIL.Image.open('Gui\\Images\\Clock.png')
PIL_image4.thumbnail(SETTINGS_BUTTON_SIZE)
image4 = PIL.ImageTk.PhotoImage(PIL_image4)

open_app_4 = tk.Button(root,
                       image=image4,
                       borderwidth=0,
                       height=SETTINGS_BUTTON_SIZE[0],
                       width=SETTINGS_BUTTON_SIZE[1],
                       activebackground=ACTIVE_BG_COLOR, bg=BG_COLOR)
open_app_4.place(relx=.1, rely=.6)

# Application Five (Music)#
PIL_image5 = PIL.Image.open('Gui\\Images\\Music_Icon.png')
Size=270,270
PIL_image5.thumbnail(Size)
image5 = PIL.ImageTk.PhotoImage(PIL_image5)

open_app_5 = tk.Button(root,
                       image=image5,
                       borderwidth=0,
                       height=SETTINGS_BUTTON_SIZE[0],
                       width=SETTINGS_BUTTON_SIZE[1],
                       activebackground=ACTIVE_BG_COLOR, bg=BG_COLOR)
open_app_5.place(relx=.4, rely=.6)

# Application Six (DesktopMode)#
PIL_image6 = PIL.Image.open('Gui\\Images\\Desktop_Icon.png')
PIL_image6.thumbnail((220,220))
image6 = PIL.ImageTk.PhotoImage(PIL_image6)

open_app_6 = tk.Button(root,
                       image=image6,
                       borderwidth=0,
                       height=SETTINGS_BUTTON_SIZE[0],
                       width=SETTINGS_BUTTON_SIZE[1],
                       activebackground=ACTIVE_BG_COLOR, bg=BG_COLOR)
open_app_6.place(relx=.7, rely=.6)

root.mainloop()
