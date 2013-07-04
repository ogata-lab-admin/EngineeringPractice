#!/usr/bin/env python                                                                                                                                                                                                                         
# -*- coding: utf-8 -*-                                                                                                                                                                                                                       

from Tkinter import *
import time, math

def initialize(): # 初期化用関数
    id0 = c0.create_oval(10, 10, 110, 110, fill='red', tags='red_oval')
    id1 = c0.create_oval(10, 120, 110, 220, fill='green', tags='green_oval')
    id2 = c0.create_oval(10, 240, 110, 340, fill='blue', tags='blue_oval')

def on_execute(): # 周期実行用関数
    now_time = time.time() - start_time
    r = g = b = 50.0 * math.sin(5 * now_time) + 50
    rgb = '#%02d%02d%02d' % (r, g, b)
    c0.itemconfig('red_oval', fill=rgb) # 色を変える

    A = 150
    omega = 5
    x = A * math.sin(omega*now_time) + A
    c0.coords('green_oval', 10 + x, 120, 110 + x, 220) # 位置を変える

    c0.coords('blue_oval', 10, 240, 110 + x, 340) # 大きさを変える

    root.after(100, on_execute)


# ここからメインコード
root = Tk()
c0 = Canvas(root, width = 480, height = 360)
c = 0

start_time = time.time()
initialize()

root.after(100, on_execute)
c0.pack()
root.mainloop()
