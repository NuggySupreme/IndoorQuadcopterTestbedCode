import smbus2
from smbus2 import SMBus
import os
import time
ch = 2 ** 1
with SMBus(1) as bus:
#	bus.write_byte(0x70, 2 ** 0)
#	os.system("i2cdetect -y 1")

   for i in range(5):
      print(i)
      bus.write_byte(0x70, 2 ** i)
      time.sleep(0.5)
      os.system("i2cdetect -y 1")

