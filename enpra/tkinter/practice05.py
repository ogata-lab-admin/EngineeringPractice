#!/usr/bin/env python                                                                                                                                                                                                                        # -*- coding: utf-8 -*-                                                                                                                                                                                                                      


import Tkinter as tk
import time, math, serial


s = serial.Serial('/dev/cu.usbmodem1412', 9600)

def on_button00_clicked():
    s.write('Y, 0\n')
    line = s.readline()
def on_button01_clicked():
    s.write('N, 0\n')
    line = s.readline()
root = tk.Tk()
f0 = tk.Frame(root)
button00 = tk.Button(f0, text = "LED 0 ON", command = on_button00_clicked)
button00.pack(side = tk.LEFT)
button01 = tk.Button(f0, text = "LED 0 OFF", command = on_button01_clicked)
button01.pack(side = tk.LEFT)
f0.pack()

def on_button10_clicked():
    s.write('Y, 1\n')
def on_button11_clicked():
    s.write('N, 1\n')

f1 = tk.Frame(root)
button10 = tk.Button(f1, text = "LED 1 ON", command = on_button10_clicked)
button10.pack(side = tk.LEFT)
button11 = tk.Button(f1, text = "LED 1 OFF", command = on_button11_clicked)
button11.pack(side = tk.LEFT)
f1.pack()

def on_button20_clicked():
    s.write('Y, 2\n')
    line = s.readline()

def on_button21_clicked():
    s.write('N, 2\n')
    line = s.readline()

f2 = tk.Frame(root)
button20 = tk.Button(f2, text = "LED 2 ON", command = on_button20_clicked)
button20.pack(side = tk.LEFT)
button21 = tk.Button(f2, text = "LED 2 OFF", command = on_button21_clicked)
button21.pack(side = tk.LEFT)
f2.pack()

def on_button30_clicked():
    s.write('Y, 3\n')
    line = s.readline()

def on_button31_clicked():
    s.write('N, 3\n')
    line = s.readline()

f3 = tk.Frame(root)
button30 = tk.Button(f3, text = "LED 3 ON", command = on_button30_clicked)
button30.pack(side = tk.LEFT)
button31 = tk.Button(f3, text = "LED 3 OFF", command = on_button31_clicked)
button31.pack(side = tk.LEFT)
f3.pack()


c0 = tk.Canvas(root, width = 200, height = 130)
c0.pack()

c0.create_rectangle(0, 10, 10, 30, fill='black', tags='ain0')
c0.create_rectangle(0, 40, 10, 60, fill='black', tags='ain1')
c0.create_rectangle(0, 70, 10, 90, fill='black', tags='ain2')
c0.create_rectangle(0, 100, 10, 120, fill='black', tags='ain3')

def on_execute(): # 周期実行用関数
    s.write('R, 0\n')
    line = s.readline()
    tokens = line.split(',')
    if tokens[0].strip() == 'R':
        a0 = float(tokens[1])
        a1 = float(tokens[2])
        a2 = float(tokens[3])
        a3 = float(tokens[4])

        c0.coords('ain0', 0, 10, 200*a0, 30)
        c0.itemconfig('ain0', fill='#%02d3030' % int(a0*99))
        c0.coords('ain1', 0, 40, 200*a1, 60)
        c0.itemconfig('ain1', fill='#3030%02d' % int(a1*99))
        c0.coords('ain2', 0, 70, 200*a2, 90)
        c0.itemconfig('ain2', fill='#30%02d30' % int(a2*99))
        c0.coords('ain3', 0, 100, 200*a3, 120)
        c0.itemconfig('ain3', fill='#3030%02d' % int(a3*99))
    root.after(100, on_execute)

on_execute()
root.mainloop()
