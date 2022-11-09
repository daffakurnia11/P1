import serial
import pycrc
import time

s = serial.Serial("COM7", 9600)
cmd = [0, 0, 0, 0, 0, 0, 0, 0]

cmd[0] = 0x01  # Modbus Address
cmd[1] = 0x05  # Write single Relay

while True:
    for i in range(8):
        # First Variation (EXAMPLE)
        # Channel 1, 2, 3
        if i == 0:
            cmd[2] = 0
            cmd[3] = i
            cmd[4] = 0xFF  # Normally Closed
            cmd[5] = 0
            crc = pycrc.ModbusCRC(cmd[0:6])
            cmd[6] = crc & 0xFF
            cmd[7] = crc >> 8
            print(cmd)
            s.write(cmd)
            time.sleep(1)  # Program Delay
        if i == 1:
            cmd[2] = 0
            cmd[3] = i
            cmd[4] = 0xFF  # Normally Closed
            cmd[5] = 0
            crc = pycrc.ModbusCRC(cmd[0:6])
            cmd[6] = crc & 0xFF
            cmd[7] = crc >> 8
            print(cmd)
            s.write(cmd)
            time.sleep(1)  # Program Delay
        if i == 2:
            cmd[2] = 0
            cmd[3] = i
            cmd[4] = 0xFF  # Normally Closed
            cmd[5] = 0
            crc = pycrc.ModbusCRC(cmd[0:6])
            cmd[6] = crc & 0xFF
            cmd[7] = crc >> 8
            print(cmd)
            s.write(cmd)
            time.sleep(1)  # Program Delay
