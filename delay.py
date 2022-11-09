import serial
import pycrc
import time

s = serial.Serial("COM10", 9600)
cmd = [0, 0, 0, 0, 0, 0, 0, 0]

cmd[0] = 0x01  # Modbus Address
cmd[1] = 0x05  # Write single Relay

while True:
    for i in range(8):
        # Turn on Red lamp
        if i == 2:
            # First Red Lamp
            cmd[2] = 2
            cmd[3] = i
            cmd[4] = 0xFF
            cmd[5] = 30  # 3 second
            crc = pycrc.ModbusCRC(cmd[0:6])
            cmd[6] = crc & 0xFF
            cmd[7] = crc >> 8
            print(cmd)
            s.write(cmd)
            time.sleep(0.2)

            # Second Red Lamp
            cmd[2] = 2
            cmd[3] = i + 3
            cmd[4] = 0xFF
            cmd[5] = 30  # 3 second
            crc = pycrc.ModbusCRC(cmd[0:6])
            cmd[6] = crc & 0xFF
            cmd[7] = crc >> 8
            print(cmd)
            s.write(cmd)
            time.sleep(3)

        # Turn on Yellow lamp
        if i == 2:
            # FIrst Yellow Lamp
            cmd[2] = 2
            cmd[3] = i
            cmd[4] = 0xFF
            cmd[5] = 15  # 1.5 second
            crc = pycrc.ModbusCRC(cmd[0:6])
            cmd[6] = crc & 0xFF
            cmd[7] = crc >> 8
            print(cmd)
            s.write(cmd)
            time.sleep(0.2)

            # Second Yellow Lamp
            cmd[2] = 2
            cmd[3] = i + 3
            cmd[4] = 0xFF
            cmd[5] = 15  # 1.5 second
            crc = pycrc.ModbusCRC(cmd[0:6])
            cmd[6] = crc & 0xFF
            cmd[7] = crc >> 8
            print(cmd)
            s.write(cmd)
            time.sleep(1.5)

        # Turn on Green lamp
        if i == 2:
            # First Green Lamp
            cmd[2] = 2
            cmd[3] = i
            cmd[4] = 0xFF
            cmd[5] = 40  # 4 second
            crc = pycrc.ModbusCRC(cmd[0:6])
            cmd[6] = crc & 0xFF
            cmd[7] = crc >> 8
            print(cmd)
            s.write(cmd)
            time.sleep(0.2)

            # Second Green Lamp
            cmd[2] = 2
            cmd[3] = i + 3
            cmd[4] = 0xFF
            cmd[5] = 40  # 4 second
            crc = pycrc.ModbusCRC(cmd[0:6])
            cmd[6] = crc & 0xFF
            cmd[7] = crc >> 8
            print(cmd)
            s.write(cmd)
            time.sleep(4)
