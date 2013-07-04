#!/usr/bin/env python                                                                                                                                                                                                                        # -*- coding: utf-8 -*-                                                                                                                                                                                                                       

import serial

s = serial.Serial('/dev/cu.usbmodem1412') # シリアルポートを開く                                                                                                                                                                              
s.flushInput()
while True:
    line = s.readline()
    tokens = line.split(',') # カンマで区切られていることを明示                                                                                                                                                                               
    digital = int(tokens[0])
    switch = True if digital == 0 else False
    value = float(tokens[1])  # ここで文字列を数値に変換                                                                                                                                                                                      
    voltage = value * 3.3  # ここで0.0から1.0のデータを電圧の単位に変換                                                                                                                                                                       
    print 'Switch is %s, Input is %s volt!' % (switch, voltage)

