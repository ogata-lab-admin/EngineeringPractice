#!/usr/bin/env python                                                                                                                                                                                                                         
# -*- coding: utf-8 -*-                                                                                                                                                                                                                       

import Tkinter as tk

root = tk.Tk()

def on_button1_clicked():
    print 'Button 1 clicked.'

def on_button2_clicked():
    print 'Button 2 clicked.'

button1 = tk.Button(root, text = "Button 1", command = on_button1_clicked)
button1.pack()

button2 = tk.Button(root, text = "Button 2", command = on_button2_clicked)
button2.pack()

root.mainloop()
