# coding:utf-8
from __future__ import unicode_literals, division, print_function

__author__ = 'timmyliang'
__email__ = '820472580@qq.com'
__date__ = '2020-05-12 11:31:30'

"""

"""

import os
import sys
import subprocess

MAYA_DIR = r"C:\Program Files\Autodesk\Maya2017"
DIR = os.path.dirname(__file__)


# NOTE Python 3 & 2 兼容
try:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import filedialog, messagebox
except:
    import ttk
    import Tkinter as tk
    import tkFileDialog as filedialog
    import tkMessageBox as messagebox


class SelectPathWidget(tk.Frame):
    def __init__(self, label_text="", path_text="", button_text="", clickEvent=None, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        # self.grid_propagate(0)
        self.grid_columnconfigure(1, weight=5)

        if label_text:
            self.label = tk.Label(self, text=label_text)
            # self.label.pack(side="left", fill=tk.X)
            self.label.grid(row=0, column=0, sticky="nsew")

        self.edit = tk.Entry(self, text='', width=25)
        self.edit.insert(0, path_text)
        # self.edit.pack(side="left", fill=tk.X, expand=1, padx=(0,100))
        self.edit.grid(row=0, column=1, sticky="nsew",padx=10)

        callback = clickEvent if callable(clickEvent) else self.selectDirectory

        self.btn = tk.Button(self, text=button_text, command=callback,width=15)
        # self.btn.place(relx=1, rely=0.5, anchor="e")
        self.btn.grid(row=0, column=2, sticky="nsew")


    def selectDirectory(self):
        path = filedialog.askdirectory()
        self.edit.delete(0, tk.END)
        self.edit.insert(0, path)


class DriveCombobox(tk.Frame):
    def __init__(self, label_text="", state='readonly',*args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        if label_text:
            self.label = tk.Label(self, text=label_text)
            self.label.pack(side="left", fill=tk.X, padx=(0,10))

        self.combo = ttk.Combobox(self,state=state)
        
        
        self.updateDrive()

        self.combo.pack(side="left", fill=tk.X, expand=1)
        self.combo.current(0)
        self.combo.bind("<Button-1>", self.updateDrive)

    def updateDrive(self,*args):
        dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        options = ['%s:' % d for d in dl if not os.path.exists('%s:' % d)]
        self.combo['values'] = options

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        comboBox = DriveCombobox(label_text="可映射盘符")
        comboBox.pack(side="top", fill=tk.X, expand=1, padx=5,pady=5)
        path_widget = SelectPathWidget(label_text="本地路径", button_text="选择")
        path_widget.pack(side="top", fill="both", expand=1, padx=5,pady=5)

        gen_frame = tk.Frame()
        gen_btn = tk.Button(gen_frame,text ="映射盘符",command=self.getAllDrive)
        gen_btn.pack(side="top", fill=tk.X, expand=1)
        gen_frame.pack(side="top", fill=tk.X, expand=1, padx=5,pady=5)
        # print (dir(tk))
        
    
    def getAllDrive(self):
        res = subprocess.check_output(["cmd","/c vol "])
        print([res])

if __name__ == "__main__":
    root = tk.Tk()
    root.winfo_toplevel().title("盘符映射工具")
    MainApplication(root).pack(side="top", expand=True, padx=100, pady=100)
    root.mainloop()

# import subprocess 
# def getDriveName(driveletter):
#     return subprocess.check_output(["cmd","/c vol "+driveletter]).decode().split("\r\n")[0].split(" ").pop()

# import subprocess 
# def getDriveName(driveletter):
#     return subprocess.check_output(["cmd","/c vol "+driveletter]).split("\r\n")[0].split(" ").pop()


# def TK_GUI():
#     try:
#         from tkinter import filedialog,messagebox
#     except ImportError:
#         import tkFileDialog as filedialog
#         import tkMessageBox as messagebox

#     def getDirectory(e):
#         path = filedialog.askdirectory()
#         e.delete(0,tk.END)
#         e.insert(0,path)

#     def install(master_window,maya_dir,install_dir):
#         maya_dir = maya_dir.get()
#         install_dir = install_dir.get()

#     master_window = tk.Tk()
#     master_window.winfo_toplevel().title("Mini Maya Installer")

#     # Parent widget for the buttons
#     group = tk.Frame(master_window)
#     group.grid(row=0, column=0, columnspan=3, sticky=tk.E+tk.W)

#     tk.Label(group, text='Maya Installation Path').grid(row=0)
#     tk.Label(group, text='Mini Maya Installation Path').grid(row=1)

#     e1 = tk.Entry(group,text='',width=50)
#     e1.insert(0,MAYA_DIR if os.path.exists(MAYA_DIR) else '')
#     e2 = tk.Entry(group,width=50)
#     e2.insert(0,os.path.realpath(os.path.dirname(__file__)))
#     e1.grid(row=0, column=1,sticky=tk.E+tk.W)
#     e2.grid(row=1, column=1,sticky=tk.E+tk.W)

#     btn_1 = tk.Button(group,text = "Browse",command=lambda: getDirectory(e1))
#     btn_2 = tk.Button(group,text = "Browse",command=lambda: getDirectory(e2))
#     btn_1.grid(row=0, column=2, padx=10)
#     btn_2.grid(row=1, column=2, padx=10)

#     # Group1 Frame ----------------------------------------------------
#     group1 = tk.Frame(master_window)
#     group1.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky=tk.E+tk.W)

#     btn_3 = tk.Button(group1,text = "Install",width=80,command=lambda: install(master_window,e1,e2))
#     btn_3.grid(padx=10, pady=10,sticky=tk.E+tk.W)

#     master_window.columnconfigure(0, weight=1)
#     master_window.rowconfigure(1, weight=1)

#     group.rowconfigure(0, weight=1)
#     group.columnconfigure(0, weight=1)
#     group1.rowconfigure(0, weight=1)
#     group1.columnconfigure(0, weight=1)

#     tk.mainloop()

# TK_GUI()
