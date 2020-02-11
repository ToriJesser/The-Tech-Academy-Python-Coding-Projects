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

import file_drill_main
import file_drill_func



def load_gui(self):

    self.txt_entry1 = tk.Entry(self.master,text='',width=55)
    self.txt_entry1.grid(row=0,column=1,rowspan=1,columnspan=6,padx=(15,0),pady=(45,0),sticky=N+E+W)
    self.txt_entry2 = tk.Entry(self.master,text='',width=55)
    self.txt_entry2.grid(row=1,column=1,rowspan=1,columnspan=6,padx=(15,0),pady=(10,0),sticky=N+E+W)
    
    self.btn_browse = tk.Button(self.master,width=14,height=1,text='Browse...',command=lambda: file_drill_func.openDirectory(self))
    self.btn_browse.grid(row=0,column=0,padx=(15,0),pady=(45,0),sticky=W)
    self.btn_browse1 = tk.Button(self.master,width=14,height=1,text='Browse...',command=lambda: file_drill_func.openDirectory2(self))
    self.btn_browse1.grid(row=1,column=0,padx=(15,0),pady=(10,0),sticky=W)
    self.btn_move = tk.Button(self.master,width=14,height=2,text='Move files',command=lambda: file_drill_func.moveFile(self,self.directory, self.directory_1))
    self.btn_move.grid(row=2,column=0,padx=(15,0),pady=(10,0),sticky=W)
    
    
    
    
