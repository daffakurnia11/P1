import serial
import pycrc
import time

s = serial.Serial("COM7", 9600)
cmd = [0, 0, 0, 0, 0, 0, 0, 0]

cmd[0] = 0x01  # Modbus Address
cmd[1] = 0x05  # Write single Relay

while True:
    for i in range(8):
        cmd[2] = 0
        cmd[3] = i
        cmd[4] = 0  # Normally Open
        cmd[5] = 0
        crc = pycrc.ModbusCRC(cmd[0:6])
        cmd[6] = crc & 0xFF
        cmd[7] = crc >> 8
        print(cmd)
        s.write(cmd)
        time.sleep(0.2)  # Program Delay
