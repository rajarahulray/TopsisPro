# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 14:53:44 2017

@author: stpl
"""

from tkinter import Entry, Tk, Button

l = [];

def enter(l):
    for i in l:
        print(i.get());


r = Tk();
for i in range(5):
    e = Entry(r);
    l.append(e);
    e.pack();

b = Button(r, text = "Click", command = lambda: enter(l)).pack();
r.mainloop();