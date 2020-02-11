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
import shutil
import os
import time
import sqlite3

import file_drill_main
import file_drill_gui





def openDirectory(self):
    self.directory = filedialog.askdirectory()
    print(self.txt_entry1.insert(INSERT,self.directory))
    return str(self.directory)


def openDirectory2(self):
    self.directory_1 = filedialog.askdirectory()
    print(self.txt_entry2.insert(INSERT,self.directory_1))
    return str(self.directory_1)

def moveFile(self, directory, directory_1):
    create_db(self)
    self.source = self.directory
    self.destination = self.directory_1
    modification_time = os.path.getmtime(directory)
    local_time = time.ctime(modification_time)
    for filename in os.listdir(self.source):
            if filename.endswith(".txt"):
                dest = shutil.move(os.path.join(self.source, filename), (os.path.join(self.destination, filename)))
                abpath = (os.path.join(directory,filename))
                print(filename, local_time)
                addToDB(self, filename, local_time)
            else:
                 continue
                
def create_db(self):
    conn = sqlite3.connect('db_files.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_fileTime( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename TEXT, \
            col_timestamp TEXT \
            );")
        conn.commit()
    conn.close()
    
def addToDB(self, filename, local_time):
    self.file = self.filename
    self.time = self.local_time
    conn = sqlite3.connect('db_files.db')
    with conn:
        cur = conn.cursor()
        cursor.execute("""INSERT INTO tbl_fileTime (col_filename, col_timestamp) VALUES (?,?)""",(self.file, self.time))
        conn.commit()
    conn.close()












    
