# Python ver 3.8.0
#
# Author:  Tori Jesser
#
# Purpose:    Demonstrate OOP, Tkinter GUI module,
#             using Tkiner Parent and Child relationships.
#
# Tested OS: this code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk
from tkinter import filedialog

import file_drill_gui
import file_drill_func



class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        # define our master from configuration
        self.master = master
        self.master.minsize(600,170) #(Width, Height)
        self.master.maxsize(600,170)
        # This CenterWindow method will center our app on the user's screen
        self.master.title("Check Files")
        self.master.configure(bg="#f0f0f0")
        arg = self.master
        
        
        # loads in the GUI widgets from a separate module
        file_drill_gui.load_gui(self)
        



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
