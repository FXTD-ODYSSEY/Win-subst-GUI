# coding:utf-8
from __future__ import division,print_function

__author__ =  'timmyliang'
__email__ =  '820472580@qq.com'
__date__ = '2020-05-12 16:38:18'

"""
https://stackoverflow.com/questions/4399180/how-to-set-the-min-and-max-height-or-width-of-a-frame
"""

from Tkinter import *

root = Tk()
#Configure line 0 and 1
Grid.rowconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)

#Configure column 0 and 1
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)

que_labl = Label(root, text='Question')
choice1 = Button(root, text='Choice one')
choice2 = Button(root, text='Choice one plus one')
choice3 = Button(root, text='Choice 3')
choice4 = Button(root, text='Choice eight divided by 2')

que_labl.grid(row=0, columnspan=2)
choice1.grid(row=2, column=0, sticky=E+W)
choice2.grid(row=2, column=1, sticky=E+W)
choice3.grid(row=3, column=0, sticky=E+W)
choice4.grid(row=3, column=1, sticky=E+W)

root.mainloop()