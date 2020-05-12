import Tkinter as tk
import tkFileDialog
import os

class AutoScrollbar(tk.Scrollbar):
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        tk.Scrollbar.set(self, lo, hi)

class Window(tk.Frame):

    def UserFileInput(self,status,name):
        row = self.row
        optionLabel = tk.Label(self)
        optionLabel.grid(row=row, column=0, sticky='w')
        optionLabel["text"] = name
        text = status#str(dirname) if dirname else status
        var = tk.StringVar(root)
        var.set(text)
        w = tk.Entry(self, textvariable= var)
        w.grid(row=row, column=1, sticky='ew')
        w.grid_columnconfigure(1,weight=1)
        self.row += 1
        return w, var

    def __init__(self,parent):
        tk.Frame.__init__(self,parent)

        self.row = 0
        currentDirectory = os.getcwd()
        directory,var = self.UserFileInput(currentDirectory, "Directory")


if __name__ == "__main__":
    root = tk.Tk()
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0,weight=1)

    vscrollbar = AutoScrollbar(root,orient=tk.VERTICAL)
    vscrollbar.grid(row=0, column=1, sticky='ns')
    hscrollbar = AutoScrollbar(root, orient=tk.HORIZONTAL)
    hscrollbar.grid(row=1, column=0, sticky='ew')

    canvas=tk.Canvas(root,yscrollcommand=vscrollbar.set,xscrollcommand=hscrollbar.set)
    canvas.grid(row=0, column=0, sticky='nsew')
    vscrollbar.config(command=canvas.yview)
    hscrollbar.config(command=canvas.xview)


    window = Window(canvas)
    canvas.create_window(0, 0, anchor=tk.NW, window=window)
    window.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    root.mainloop()