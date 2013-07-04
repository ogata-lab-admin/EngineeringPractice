#!/usr/bin/env python                                                                                                                                                                                                                         
# -*- coding: utf-8 -*-                                                                                                                                                                                                                       

from Tkinter import *

root = Tk() # Tkを開始．メインウィンドウ作成
c0 = Canvas(root, width = 480, height = 360) #キャンバスを追加

id2 = c0.create_line(0, 0, 480, 360, fill='red') # 線を書く

id0 = c0.create_oval(10, 10, 110, 110, fill='red') # 円を書く．色を変える
id3 = c0.create_oval(220, 50, 320, 150, fill='blue')

id1 = c0.create_rectangle(150, 150, 250, 250, fill='green') # 四角形を書く

points = [ 450, 10, 450, 110, 350, 110, 450, 10] # 任意の多角形を書く
c0.create_polygon(points, fill='yellow')


c0.pack()

root.mainloop()
