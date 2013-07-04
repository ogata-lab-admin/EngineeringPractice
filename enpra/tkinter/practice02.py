#!/usr/bin/env python                                                                                                                                                                                                                         
# -*- coding: utf-8 -*-                                                                                                                                                                                                                       

import serial
import Tkinter as tk
root = tk.Tk()

s = serial.Serial('/dev/cu.usbmodem1412', 9600)

def on_button0_clicked():
    s.write('0¥n')

def on_button1_clicked():
    s.write('1¥n')

def on_button2_clicked():
    s.write('2¥n')

def on_button3_clicked():
    s.write('3¥n')


button0 = tk.Button(root, text = "Button 0", command = on_button0_clicked)
button0.pack()
button1 = tk.Button(root, text = "Button 1", command = on_button1_clicked)
button1.pack()
button2 = tk.Button(root, text = "Button 2", command = on_button2_clicked)
button2.pack()
button3 = tk.Button(root, text = "Button 3", command = on_button3_clicked)
button3.pack()

root.mainloop()
