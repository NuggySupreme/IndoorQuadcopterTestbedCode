import rclpy
from rclpy.node import Node
import smbus2
from smbus2 import SMBus
import sys
import os
import RPi.GPIO
import time

multiplexAddr = 0x77

class FanController(Node):
   def __init__(self, chNum):
      self.multiplexCh = 2 ** chNum
      print(self.multiplexCh)

      bus = SMBus(1)
      time.sleep(0.1)
      bus.write_byte(0x77, 0x80)
      time.sleep(0.1)
      os.system("i2cdetect -y 1")

def main():
   fcontroller = FanController(7)

if __name__ == '__main__':
   main()
