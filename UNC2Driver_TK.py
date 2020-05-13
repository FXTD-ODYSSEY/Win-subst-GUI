# coding:utf-8
from __future__ import unicode_literals, division, print_function

__author__ = 'timmyliang'
__email__ = '820472580@qq.com'
__date__ = '2020-05-12 11:31:30'

"""

"""

import os
import sys
import json
import codecs
import tempfile

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

def takeParm(kwargs,key,default = None):
    res = kwargs.get(key,default)
    if key in kwargs:
        del kwargs[key]
    return res

class SelectPathWidget(tk.Frame):
    def __init__(self, *args, **kwargs):
        label_text = takeParm(kwargs,"label_text","")
        path_text = takeParm(kwargs,"path_text","")
        button_text = takeParm(kwargs,"button_text","")
        clickEvent = takeParm(kwargs,"clickEvent")

        tk.Frame.__init__(self, *args, **kwargs)

        self.grid_columnconfigure(1, weight=1)

        if label_text:
            self.label = tk.Label(self, text=label_text)
            self.label.grid(row=0, column=0, sticky="nsew")

        self.edit = tk.Entry(self, text='', width=25)
        self.edit.insert(0, path_text)
        self.edit.grid(row=0, column=1, sticky="nsew",padx=10)

        callback = clickEvent if callable(clickEvent) else self.selectDirectory

        self.btn = tk.Button(self, text=button_text, command=callback,width=15)
        self.btn.grid(row=0, column=2, sticky="nsew")


    def selectDirectory(self):
        path = filedialog.askdirectory()
        if path:
            self.edit.delete(0, tk.END)
            self.edit.insert(0, path)

    def get(self):
        return self.edit.get()

class DriveCombobox(tk.Frame):
    def __init__(self, *args, **kwargs):

        label_text = takeParm(kwargs,"label_text","")
        state = takeParm(kwargs,"state","readonly")
        self.exists = takeParm(kwargs,"exists",False)

        tk.Frame.__init__(self, *args, **kwargs)

        if label_text:
            self.label = tk.Label(self, text=label_text)
            self.label.pack(side="left", fill="x", padx=(0,10))

        self.combo = ttk.Combobox(self,state=state)
        
        
        self.update()

        self.combo.pack(side="left", fill="x", expand=1)
        self.combo.current(0)
        self.combo.bind("<Button-1>", self.update)

    def update(self,*args):
        dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        options =   ['%s:' % d for d in dl if os.path.exists('%s:' % d)] if self.exists else ['%s:' % d for d in dl if not os.path.exists('%s:' % d)]
        self.combo['values'] = options
        option = self.combo.get()
        if option not in options:
            self.combo.current(0)

    def get(self):
        return self.combo.get()
    def current(self,i):
        return self.combo.current(i)

class LabelSeperator(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        label_text = kwargs.get("label_text")
        if label_text:
            self.grid_columnconfigure(0, weight=100)
            self.grid_columnconfigure(1, weight=1)
            self.grid_columnconfigure(2, weight=100)
            ttk.Separator(self,orient=tk.HORIZONTAL).grid(row=0, column=0, sticky="ew")
            tk.Label(self, text=label_text).grid(row=0, column=1, sticky="nsew",padx=10)
            ttk.Separator(self,orient=tk.HORIZONTAL).grid(row=0, column=2, sticky="ew")
        else:
            sep = ttk.Separator(self,orient=tk.HORIZONTAL)
            sep.pack(side="top", fill="x", expand=1, padx=5,pady=5)

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        parent.title("盘符映射工具")
        parent.protocol("WM_DELETE_WINDOW", self.onClosing)

        # NOTE 获取系统临时路径
        temp_dir = tempfile.gettempdir()
        self.json_file = os.path.join(temp_dir,"subst_TK_GUI.json")
        # NOTE 获取 startup 目录
        user_path = os.path.expanduser('~')
        self.startup_path = os.path.join(user_path, r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")

        
        # NOTE 生成菜单 
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="使用说明", command=self.helpWin)
        filemenu.add_separator()
        filemenu.add_command(label="退出", command=self.onClosing)
        menubar.add_cascade(label="帮助", menu=filemenu)
        parent.config(menu=menubar)

        UNC_Frame = tk.Frame()
        gen_frame = tk.LabelFrame(UNC_Frame,text="映射盘符")
        gen_frame.pack(side="top",fill="both", expand=1) 

        self.gen_comboBox = DriveCombobox(gen_frame,label_text="可映射盘符")
        self.gen_comboBox.pack(side="top", fill="x", expand=1, padx=5,pady=5)
        self.path_widget = SelectPathWidget(gen_frame,label_text="本地路径", button_text="选择")
        self.path_widget.pack(side="top", fill="both", expand=1, padx=5,pady=5)

        gen_btn = tk.Button(gen_frame,text ="映射盘符",command=self.generateDriver)
        gen_btn.pack(side="top", fill="x", expand=1, padx=5,pady=5)

        del_frame = tk.LabelFrame(UNC_Frame,text="删除盘符")

        self.del_comboBox = DriveCombobox(del_frame,label_text="可删除盘符",exists=True)
        self.del_comboBox.pack(side="top", fill="x", expand=1, padx=5,pady=5)

        del_btn = tk.Button(del_frame,text ="删除盘符",command=self.deleteDriver)
        del_btn.pack(side="top", fill="x", expand=1, padx=5,pady=5)

        del_frame.pack(side="top",fill="both", expand=1) 

        UNC_Frame.pack(side="top", fill="x", expand=1, padx=5,pady=5)

        self.loadJson()
    
    def helpWin(self):
        help_win = tk.Toplevel(self.parent)
        help_win.title("使用说明")
        tk.Label(help_win, text="选择可映射盘符进行映射").pack(side="top", fill="x", expand=1, padx=5,pady=5)
        tk.Label(help_win, text="如果盘符已经存在需要先删除已有盘符再映射").pack(side="top", fill="x", expand=1, padx=5,pady=5)
        tk.Label(help_win, text="删除盘符为系统分区会提示执行出错，不用担心错误删除系统分区").pack(side="top", fill="x", expand=1, padx=5,pady=5)

    def onClosing(self):
        self.saveJson()
        self.parent.destroy()

    def loadJson(self,directory=None):
        directory = self.json_file if directory is None else directory
        if not os.path.exists(directory):
            return

        data = {}
        try:
            with open(directory, "r") as f:
                data = json.load(f,encoding="utf-8")
        except:
            import traceback
            traceback.print_exc()
            return

        gen_drive = data.get("gen_comboBox")
        del_drive = data.get("del_comboBox")
        path = data.get("path")

        for i,val in enumerate(self.gen_comboBox.combo['values']):
            if val == gen_drive:
                self.gen_comboBox.current(i)
                break

        for i,val in enumerate(self.del_comboBox.combo['values']):
            if val == del_drive:
                self.del_comboBox.current(i)
                break
        
        self.path_widget.edit.delete(0,tk.END)
        self.path_widget.edit.insert(0,path)
    
    def saveJson(self,directory=None):
        data = {
            "gen_comboBox" : self.gen_comboBox.get(),
            "del_comboBox" : self.del_comboBox.get(),
            "path" : self.path_widget.get(),
        }
        directory = self.json_file if directory is None else directory
        with open(directory, "w") as f:
            json.dump(data,f,indent=4)

    def generateDriver(self):
        Driver = self.gen_comboBox.get()
        directory = self.path_widget.get()
        if not os.path.exists(directory):
            messagebox.showerror("Error", u"%s 路径不存在" % directory )
            return
        
        command = "subst %s %s" % (Driver,directory)
        val = os.system(command)
        if val != 0:
            messagebox.showerror(u"错误", u"执行出错" )
            return
        else:
            messagebox.showinfo(u"恭喜您", u"执行成功" )

        self.gen_comboBox.update()
        self.del_comboBox.update()

        
        if os.path.exists(self.startup_path):
            bat_path = os.path.join(self.startup_path, "subst_%s_Driver.bat" % Driver[0])
            with codecs.open(bat_path, 'w', encoding="utf-8") as f:
                f.write("subst %s /D\n%s" % (Driver,command))

        self.saveJson()


    def deleteDriver(self):
        Driver = self.del_comboBox.get()
        val = os.system("subst %s /D" % Driver)
        if val != 0:
            messagebox.showerror(u"错误", u"执行出错" )
            return
        else:
            messagebox.showinfo(u"恭喜您", u"执行成功" )

        self.gen_comboBox.update()
        self.del_comboBox.update()

        bat_path = os.path.join(self.startup_path, "subst_%s_Driver.bat" % Driver[0])
        if os.path.exists(bat_path):
            os.remove(bat_path)

        self.saveJson()

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", expand=True)
    root.mainloop()
