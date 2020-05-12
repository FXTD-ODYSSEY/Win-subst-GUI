# coding:utf-8
from __future__ import division,print_function

__author__ =  'timmyliang'
__email__ =  '820472580@qq.com'
__date__ = '2020-05-12 16:38:18'

"""
https://stackoverflow.com/questions/4399180/how-to-set-the-min-and-max-height-or-width-of-a-frame
"""

import Tkinter as tk
root = tk.Tk()
frame1 = tk.Frame(root, width=50, height=50, background="bisque")
frame2 = tk.Frame(root, width=50, height = 50, background="#b22222")

frame1.pack(fill=None, expand=False)
frame2.place(relx=.5, rely=.5, anchor="c")

root.mainloop()