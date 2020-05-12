# coding:utf-8
from __future__ import division,print_function

__author__ =  'timmyliang'
__email__ =  '820472580@qq.com'
__date__ = '2020-05-12 19:43:44'

"""
https://stackoverflow.com/questions/59213078/changing-the-width-of-the-character-output-with-tkinter-in-python?noredirect=1&lq=1
"""

import sys
from   Tkinter import Tk
import tkFont
root = Tk()
fnames = list(tkFont.families())
fnames = sorted(fnames)
k = 0
for s in fnames:
    k=k+1
    sys.stdout.write(str(k)+'\t'+s+'\n')