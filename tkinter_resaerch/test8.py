# coding:utf-8
from __future__ import division,print_function

__author__ =  'timmyliang'
__email__ =  '820472580@qq.com'
__date__ = '2020-05-12 19:43:44'

"""
https://stackoverflow.com/questions/36575890/how-to-set-a-tkinter-window-to-a-constant-size
"""

import tkinter as tk

def startgame():

    pass

mw = tk.Tk()

#If you have a large number of widgets, like it looks like you will for your
#game you can specify the attributes for all widgets simply like this.
mw.option_add("*Button.Background", "black")
mw.option_add("*Button.Foreground", "red")

mw.title('The game')
#You can set the geometry attribute to change the root windows size
mw.geometry("500x500") #You want the size of the app to be 500x500
mw.resizable(0, 0) #Don't allow resizing in the x or y direction

back = tk.Frame(master=mw,bg='black')
back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window

#Changed variables so you don't have these set to None from .pack()
go = tk.Button(master=back, text='Start Game', command=startgame)
go.pack()
close = tk.Button(master=back, text='Quit', command=mw.destroy)
close.pack()
info = tk.Label(master=back, text='Made by me!', bg='red', fg='black')
info.pack()

mw.mainloop()