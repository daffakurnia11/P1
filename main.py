import serial
import pycrc
import time

s = serial.Serial("COM7", 9600)
cmd = [0, 0, 0, 0, 0, 0, 0, 0]

cmd[0] = 0x01  # Modbus Address
cmd[1] = 0x05  # Write single Relay

while True:
    for i in range(8):
        # First Variation
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
            cmd[4] = 0xFF
            cmd[5] = 0
            crc = pycrc.ModbusCRC(cmd[0:6])
            cmd[6] = crc & 0xFF
            cmd[7] = crc >> 8
            print(cmd)
            s.write(cmd)
            time.sleep(1)
        if i == 2:
            cmd[2] = 0
            cmd[3] = i
            cmd[4] = 0xFF
            cmd[5] = 0
            crc = pycrc.ModbusCRC(cmd[0:6])
            cmd[6] = crc & 0xFF
            cmd[7] = crc >> 8
            print(cmd)
            s.write(cmd)
            time.sleep(1)

        # VARIASI 2 - DAFFA
        # if i == 0:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 1:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 3:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)

        # VARIASI 3 - DAFFA
        # if i == 0:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 1:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 5:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)

        # VARIASI 1 - ARDA
        # if i == 1:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 2:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 4:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)

        # VARIASI 2 - ARDA
        # if i == 1:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 2:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 6:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)

        # VARIASI 3 - ARDA
        # if i == 1:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 3:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 7:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)

        # VARIASI 1 - RANU
        # if i == 3:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 4:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 5:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)

        # VARIASI 2 - RANU
        # if i == 3:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 5:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 7:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)

        # VARIASI 3 - RANU
        # if i == 3:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 6:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 7:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)

        # VARIASI 1 - DINAR
        # if i == 0:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 1:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 6:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)

        # VARIASI 2 - DINAR
        # if i == 0:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 2:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 4:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)

        # VARIASI 3 - DINAR
        # if i == 0:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 2:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 7:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)

        # VARIASI 1 - NATA
        # if i == 2:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 3:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 4:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)

        # VARIASI 2 - NATA
        # if i == 2:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 3:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 6:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)

        # VARIASI 3 - NATA
        # if i == 2:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 4:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
        # if i == 7:
        #     cmd[2] = 0
        #     cmd[3] = i
        #     cmd[4] = 0xFF
        #     cmd[5] = 0
        #     crc = pycrc.ModbusCRC(cmd[0:6])
        #     cmd[6] = crc & 0xFF
        #     cmd[7] = crc >> 8
        #     print(cmd)
        #     s.write(cmd)
        #     time.sleep(1)
