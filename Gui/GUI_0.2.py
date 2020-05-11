"""
Best Version of Gui So Far
"""
import os
import PIL
import tkinter as tk
from PIL import Image, ImageTk


Apps=[]
class App():
    
    def __init__(self, icon='', description=''):
        Apps.append(self)
        index=0
        for x in Apps:
            index+=1
        self.icon=icon
        self.index=index
        self.description=description
        
Weather=App('Images\Weather_Icon.png', 'An App for Weather... lol')
Settings=App('Images\Settings.png', 'Play With Tuesdays Settings ;) ')
Strunes=App('Images\Music_Icon.png', 'To Jam Out When You are Likely a Lonely Loser')
Clock=App('Images\Clocks.png', 'To Wake Yo Stupid Ass Up')
Tuesday=App('Images\AI.png', 'For all your robot needs')