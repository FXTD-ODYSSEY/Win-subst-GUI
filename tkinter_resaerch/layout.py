# coding:utf-8
from __future__ import division,print_function

__author__ =  'timmyliang'
__email__ =  '820472580@qq.com'
__date__ = '2020-05-12 16:15:41'

"""
https://stackoverflow.com/questions/45543948/tkinter-fill-y-does-not-work-with-button
"""

import Tkinter as tk
root = tk.Tk()
tk.Button(root, text="A").pack(side=tk.LEFT, expand=tk.YES, fill=tk.Y)
tk.Button(root, text="B").pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)
tk.Button(root, text="C").pack(side=tk.RIGHT, expand=tk.YES, fill=tk.NONE, anchor = tk.NE)
tk.Button(root, text="D").pack(side=tk.LEFT, expand=tk.NO, fill=tk.Y)
tk.Button(root, text="E").pack(side=tk.TOP, expand=tk.NO, fill=tk.BOTH)
tk.Button(root, text="F").pack(side=tk.RIGHT, expand=tk.NO, fill=tk.NONE)
tk.Button(root, text="G").pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.Y)
tk.Button(root, text="H").pack(side=tk.TOP, expand=tk.NO, fill=tk.BOTH)
tk.Button(root, text="I").pack(side=tk.RIGHT, expand=tk.NO)
tk.Button(root, text="J").pack(anchor=tk.SE)
root.mainloop()

# import Tkinter as tk
# root = tk.Tk()
# tk.Label(root, text="A", bg='green').pack(side=tk.LEFT, expand=tk.YES, fill=tk.Y)
# tk.Label(root, text="B", bg='red').pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)
# tk.Label(root, text="C", bg='blue').pack(side=tk.RIGHT, expand=tk.YES, fill=tk.NONE, anchor=tk.NE)
# tk.Label(root, text="D", bg='yellow').pack(side=tk.LEFT, expand=tk.NO, fill=tk.Y)
# tk.Label(root, text="E", bg='purple').pack(side=tk.TOP, expand=tk.NO, fill=tk.BOTH)
# tk.Label(root, text="F", bg='pink').pack(side=tk.TOP, expand=tk.NO, fill=tk.NONE)
# tk.Label(root, text="G", bg='green').pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.Y)
# tk.Label(root, text="H", bg='red').pack(side=tk.TOP, expand=tk.NO, fill=tk.BOTH)
# tk.Label(root, text="I", bg='blue').pack(side=tk.RIGHT, expand=tk.NO)
# tk.Label(root, text="J", bg='yellow').pack(anchor=tk.SE)
# root.mainloop()