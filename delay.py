#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import serial
import pycrc
import time

s = serial.Serial("COM10", 9600)
cmd = [0, 0, 0, 0, 0, 0, 0, 0]

cmd[0] = 0x01
cmd[1] = 0x05

while True:
    for i in range(8):
        # LAMPU MERAH
        if i == 2:
            cmd[2] = 2
            cmd[3] = i
            cmd[4] = 0
            cmd[5] = 30  # 3 DETIK
            crc = pycrc.ModbusCRC(cmd[0:6])
            cmd[6] = crc & 0xFF
            cmd[7] = crc >> 8
            print(cmd)
            s.write(cmd)
            time.sleep(4)
        # LAMPU KUNING
        if i == 2:
            cmd[2] = 2
            cmd[3] = i
            cmd[4] = 0
            cmd[5] = 15  # 1.5 Detik
            crc = pycrc.ModbusCRC(cmd[0:6])
            cmd[6] = crc & 0xFF
            cmd[7] = crc >> 8
            print(cmd)
            s.write(cmd)
            time.sleep(2.5)
        # LAMPU HIJAU
        if i == 2:
            cmd[2] = 2
            cmd[3] = i
            cmd[4] = 0
            cmd[5] = 40  # 4 DETIK
            crc = pycrc.ModbusCRC(cmd[0:6])
            cmd[6] = crc & 0xFF
            cmd[7] = crc >> 8
            print(cmd)
            s.write(cmd)
            time.sleep(5)
