#!/usr/bin/env python                                                                                                                                                                                                                         
# -*- coding: utf-8 -*-   

import serial

s = serial.Serial('/dev/cu.usbmodem1412') # シリアルポートを開く
print 'Press Enter Key.'

s.write('0\n') # 全消灯
raw_input() # Enterキーを待つ

s.write('1\n')
raw_input()

s.write('2\n')
raw_input()

s.write('3\n')
raw_input()

s.write('4\n')
raw_input()

s.write('0\n')
