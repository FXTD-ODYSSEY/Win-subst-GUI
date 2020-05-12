# coding:utf-8
from __future__ import division,print_function

__author__ =  'timmyliang'
__email__ =  '820472580@qq.com'
__date__ = '2020-05-12 20:22:10'

"""
https://stackoverflow.com/questions/60478892/python-tkinter-frame-making-frame-width-span-full-root-window-width
"""

import tkinter
import tkinter.ttk

win = tkinter.Tk()
win.geometry('600x600')

frame = tkinter.Frame(win, bg='red', height=300)
frame.grid(row=0, column=0, sticky='ew')
win.grid_columnconfigure(0,weight=1)

win.mainloop()