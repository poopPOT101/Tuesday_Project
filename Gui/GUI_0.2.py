import tkinter as tk
import PIL

import os




#All Perams#
BG_COLOR = '#00E5B4'
ACTIVE_BG_COLOR = '#bdffed'
DISPLAY_BAR_COLOR = '#00b584'
ICON_SIZE = 128, 128
HEIGHT = 480
WIDTH = 720
App_Images = ('', 'Images\Settings.png',
                  'Images\Settings.png',
                  'Images\Settings.png',
                  'Images\Settings.png',
                  'Images\Settings.png',
                  'Images\Settings.png')

#root = tk.Toplevel()
root = tk.Tk()

def Set_Icon(Image=''):
    PIL_image=PIL.Image.open(Image)
    PIL_image.thumbnail(ICON_SIZE)
    app_icon = PIL.ImageTk.PhotoImage(PIL_image)          
    return app_icon
    
#Canvas#
main_canvas = tk.Canvas(root, height=HEIGHT,
                              width=WIDTH, 
                              bg=BG_COLOR)
main_canvas.pack()

#Frame#

display_bar= tk.Frame(main_canvas, bg=DISPLAY_BAR_COLOR)
display_bar.place(relwidth=1, relheight=0.1, relx=0., rely=0)




"""
APPS
"""
Apps=['Settings', 'Weather', 'Tuesday', 'Clock', 'Music', 'PC Mode']

#Application One (Settings)#
open_app_1 = tk.Button(root,
                       image = Set_Icon(Image=App_Images[1]),
                       borderwidth=0, 
                       height=ICON_SIZE[0],
                       width=ICON_SIZE[1],
                       activebackground=ACTIVE_BG_COLOR, bg=BG_COLOR)
open_app_1.place(relx=.1, rely=.2)

"""

#Application Two (Weather)#
open_app_2 = tk.Button(root,
                       image=SetIcon(App_Images[2]),
                       borderwidth=0, 
                       height=ICON_SIZE[0],
                       width=ICON_SIZE[1],
                       activebackground=ACTIVE_BG_COLOR, bg=BG_COLOR)
open_app_2.place(relx=.4, rely=.2)

#Application Three (Tuesday)#
open_app_3 = tk.Button(root,
                       image=SetIcon(App_Images[3]),
                       borderwidth=0, 
                       height=ICON_SIZE[0],
                       width=ICON_SIZE[1],
                       activebackground=ACTIVE_BG_COLOR, bg=BG_COLOR)
open_app_3.place(relx=.7, rely=.2)

#Application Four (Clock)#
open_app_4 = tk.Button(root,
                       image=SetIcon(App_Images[4]),
                       borderwidth=0, 
                       height=ICON_SIZE[0],
                       width=ICON_SIZE[1],
                       activebackground=ACTIVE_BG_COLOR, bg=BG_COLOR)
open_app_4.place(relx=.1, rely=.6)

#Application Five (Music)#
open_app_5 = tk.Button(root,
                       image=SetIcon(App_Images[5]),
                       borderwidth=0, 
                       height=ICON_SIZE[0],
                       width=ICON_SIZE[1],
                       activebackground=ACTIVE_BG_COLOR, bg=BG_COLOR)
open_app_5.place(relx=.4, rely=.6)

#Application Six (DesktopMode)#
open_app_6 = tk.Button(root,
                       image=SetIcon(App_Images[6]),
                       borderwidth=0, 
                       height=ICON_SIZE[0],
                       width=ICON_SIZE[1],
                       activebackground=ACTIVE_BG_COLOR, bg=BG_COLOR)
open_app_6.place(relx=.7, rely=.6)
"""
root.mainloop()