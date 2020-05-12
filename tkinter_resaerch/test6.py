# coding:utf-8
from __future__ import division,print_function

__author__ =  'timmyliang'
__email__ =  '820472580@qq.com'
__date__ = '2020-05-12 19:41:22'

"""
https://stackoverflow.com/questions/51692178/tkinter-frame-not-displaying?noredirect=1&lq=1
"""

from tkinter import *


    #*||Variables||*

#Stylistic Variables:

active_BG = 'DarkGreen' #active background color
active_FG = 'white' #active foreground color
main_font = 'SimSun 30 bold' #main font, size and style
sub_font = 'SimSun 20 bold' #sub font, size and style
sub_font2 = 'SimSun 11 bold' #sub font 2, size and style
sub_font3 = 'SimSun 10'

bg_1 = 'MediumSeaGreen' #background color 1
bg_2 = 'palegreen' #background color 2
bg_3 = 'SeaGreen' #background color 3
fg_1 = 'DarkGreen' #foreground color 1
fg_2 = 'LightCyan' #foreground color 2
hand_cursor = 'hand2' #button hover cursor
raised_relief = 'raised' #relief style 1 (raised)
groove_relief = 'groove' #relief style 2 (groove)

#Game Variables

#STUFF...

    #*||Functions||*

class tenalyzer_V1:

    def __init__(self, root):
        self.root = root
        self.root.grid_propagate(False)
        
        self.title_frame = Frame(self.root)
        self.title_frame.grid(row=0)
        self.title_frame.config(bg=bg_1, width=520, height=100)

        self.title_label = Label(self.title_frame)
        self.title_label.grid(row=0)
        self.title_label.config(text='Tenalyzer v1.0', bg=bg_1, fg=fg_2, font=main_font, width='17', bd=10, relief=groove_relief)

        self.start_frame = Frame(self.root, bg=bg_3, width=520, height=100).grid(row=1)
        self.start_label = Button(self.start_frame)
        self.start_label.grid(row=1)
        self.start_label.config(text='START', bg=bg_2, activebackground=active_BG , fg=fg_1, activeforeground=active_FG, font=sub_font, width=14, bd=5, relief=raised_relief, cursor=hand_cursor, command=self.start_page)

        self.instructions_frame = Frame(self.root, bg=bg_1, width=520, height=100).grid(row=2)
        self.instructions_btn = Button(self.instructions_frame)
        self.instructions_btn.grid(row=2)
        self.instructions_btn.config(text='INSTRUCTIONS', bg=bg_2, activebackground=active_BG , fg=fg_1, activeforeground=active_FG, font=sub_font, width=14, bd=5, relief=raised_relief, cursor=hand_cursor, command=self.instructions_page)

        self.credit_frame = Frame(self.root, bg=bg_3, width=520, height=100).grid(row=3)
        self.credit_btn = Button(self.credit_frame)
        self.credit_btn.grid(row=3)
        self.credit_btn.config(text='CREDITS', bg=bg_2, activebackground=active_BG , fg=fg_1, activeforeground=active_FG, font=sub_font, width=14, bd=5, relief=raised_relief, cursor=hand_cursor, command=self.credits_page)

        self.return_frame = Frame(self.root, bg=bg_1, width=520, height=40).grid(row=4)
        self.return_btn = Button(self.return_frame)
        self.return_btn.grid(row=4)
        self.return_btn.config(text='Exit', bg=bg_2, activebackground=active_BG , fg=fg_1, activeforeground=active_FG, font=sub_font2, width=16, bd=5, relief=raised_relief, cursor=hand_cursor, command=self.exit_command)

    def exit_command(self):
        root.destroy()

    def title_page(self):
        self.title_label.grid(row=0)
        self.start_label.grid(row=1)
        self.instructions_btn.grid(row=2)
        self.credit_btn.grid(row=3)

        self.title_label.config(text='Tenalyzer v1.0')
        self.return_btn.config(text='Exit', command=self.exit_command)

    def start_page(self):
        print('started')

    def instructions_page(self):
        print('instructions page')

    def credits_page(self):
        print('credits page')
        self.title_label.config(text='Credits:')
        self.return_btn.config(text='Go Back', command=self.title_page)

    #*||Main Program||*

root = Tk()
root.title('Tenalyzer v1.0')
# root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(520, 440))
keyword = tenalyzer_V1(root)
root.mainloop()