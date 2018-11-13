import tkinter
from tkinter import Menu
from tkinter import Menubutton
from tkinter import OptionMenu
from tkinter import *

if __name__ == '__main__':
    root = Tk()
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0,title='PYTHON')
    filemenu.add_command(label="New")
    filemenu.add_command(label="Open")
    filemenu.add_command(label="Save")
    filemenu.add_command(label="Save as...")
    filemenu.add_command(label="Close")

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo")

    editmenu.add_separator()

    editmenu.add_command(label="Cut")
    editmenu.add_command(label="Copy")
    editmenu.add_command(label="Paste")
    editmenu.add_command(label="Delete")
    editmenu.add_command(label="Select All")

    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index")
    helpmenu.add_command(label="About...")
    menubar.add_cascade(label="Help")

    root.config(menu=menubar)
    root.title('MENU PYTHON')
    root.mainloop()
