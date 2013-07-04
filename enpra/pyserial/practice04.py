#!/usr/bin/env python                                                                                                                                                                                                                                                                                                                                                                                                                                                           
# -*- coding: utf-8 -*-                                                                                                                                                                                                                       

import serial, time

s = serial.Serial('/dev/cu.usbmodem1412') # シリアルポートを開く                                                                                                                                                                              
fout = open('data.csv', 'w') # このファイルにデータを書き出す                                                                                                                                                                                 
start_time = time.time() # timeモジュールを使って時間計測                                                                                                                                                                                     
while True:
    line = s.readline()
    tokens = line.split(',') # カンマで区切られていることを明示                                                                                                                                                                               
    switch = int(tokens[0])
    value = float(tokens[1])  # ここで文字列を数値に変換                                                                                                                                                                                      
    voltage = value * 3.3  # ここで0.0から1.0のデータを電圧の単位に変換                                                                                                                                                                       
    now_time = time.time() - start_time
    fout.write('%f, %d, %f\r\n' % (now_time, switch, voltage)) # ファイルに書き出す                                                                                                                                                           
    if now_time > 10.0:
        break # 10秒たったら終了                                                                                                                                                                                                              

fout.close() # ファイルをクローズする                                                                                                                                                                                                         




