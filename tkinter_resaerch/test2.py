from Tkinter import *

root = Tk()
root.geometry("500x500")
widget = Button(root, text='text1')
widget.pack(fill=X, expand=1)
widget = Button(root, text='text2')
widget.pack(fill=Y, expand=1)
widget = Button(root, text='text3')
widget.pack(fill=BOTH, expand=1)
root.mainloop()