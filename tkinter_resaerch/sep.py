# coding:utf-8
from __future__ import division,print_function

__author__ =  'timmyliang'
__email__ =  '820472580@qq.com'
__date__ = '2020-05-12 20:29:00'

"""
https://stackoverflow.com/questions/55281326/python-tkinter-line-seperator-between-buttons
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
toolbar = tk.Frame(root)
toolbar.pack(side="top", fill="x", padx=20, pady=20)

button1 = tk.Button(toolbar, text="Home")
button2 = tk.Button(toolbar, text="Insert")
sep = ttk.Separator(toolbar)

button1.pack(side="left")
sep.pack(side="left", fill="both", padx=4, pady=4)
button2.pack(side="left")

root.mainloop()