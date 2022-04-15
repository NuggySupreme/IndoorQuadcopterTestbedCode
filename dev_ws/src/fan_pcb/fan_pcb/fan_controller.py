import rclpy
from rclpy.node import Node
import smbus2
from smbus2 import SMBus
import sys
import os
import RPi.GPIO
import time
import math

multiplexAddr = 0x77

SPEED_REGISTER = 0x00 #X
CONFIG_REGISTER = 0x02 #X
GPIO_DEF_REGISTER = 0x04 #X
TACH0_REGISTER = 0x0C
TACH1_REGISTER = 0x0E
TACH2_REGISTER = 0x10
TACH3_REGISTER = 0x12
COUNT_REGISTER = 0x16

class FanController(Node):
   def __init__(self, chNum):
      self.multiplexCh = 2 ** chNum
      self.address = [0x1b, 0x1f, 0x48, 0x4B]
      self.isOn = [False, False, False, False]
      self.K_SCALE = 4000/60 * (64+1) / 992 #max_rps * (K_TACH (should be around 64) + 1) / 992 since using internal oscillator

      print("Calculated: " + str(self.K_SCALE))
      if self.K_SCALE < 1:
         self.K_SCALE = 1
      elif self.K_SCALE >= 1 and self.K_SCALE < 2:
         if (self.K_SCALE - 1) < (2 - self.K_SCALE):
            self.K_SCALE = 1
         else:
            self.K_SCALE = 2
      elif self.K_SCALE >= 2 and self.K_SCALE < 4:
         if (self.K_SCALE - 2) < (4 - self.K_SCALE):
            self.K_SCALE = 2
         else:
            self.K_SCALE = 4
      elif self.K_SCALE >= 4 and self.K_SCALE < 16:
         if (self.K_SCALE - 4) < (16 - self.K_SCALE):
            self.K_SCALE = 4
         else:
            self.K_SCALE = 16
      else:
         self.K_SCALE = 16
      print("Best fit: " + str(self.K_SCALE))

      bus = SMBus(1)
      bus.write_byte(multiplexAddr, self.multiplexCh)
      time.sleep(0.1)
      os.system("i2cdetect -y 1")

      print("Turning off")
      self.turnOff(0)
      time.sleep(2)

      print("Configuring")
      bus.write_byte_data(self.address[0], GPIO_DEF_REGISTER, 0b00101010)
      bus.write_byte_data(self.address[0], COUNT_REGISTER, 0b00000010)

      print("Turning fully on")
      self.fullOn(0)
      time.sleep(5)

      print("Turning off")
      self.turnOff(0)
      time.sleep(2)
      self.turnOn(0)
      self.setSpeed(0, 0.80)
      time.sleep(20)
      self.setSpeed(0, 0.25)
      time.sleep(20)
      self.setSpeed(0, 2.00)
      time.sleep(2)
      self.turnOff(0)
      time.sleep(2)

   def fullOn(self, addr):
      bus = SMBus(1)
      bus.write_byte(multiplexAddr, self.multiplexCh)
      bus.write_byte_data(self.address[addr], CONFIG_REGISTER, 0b00001010)

   def turnOn(self, addr):
      bus = SMBus(1)
      bus.write_byte(multiplexAddr, self.multiplexCh)

      if self.isOn[addr] == False:
         bus.write_byte_data(self.address[addr], CONFIG_REGISTER, 0b00001010)
         time.sleep(0.25)
      bus.write_byte_data(self.address[addr], CONFIG_REGISTER, 0b00101010)
      self.isOn[addr] = True

   def turnOff(self, addr):
      bus = SMBus(1)
      bus.write_byte(multiplexAddr, self.multiplexCh)
      bus.write_byte_data(self.address[addr], CONFIG_REGISTER, 0b00011010)
      self.isOn[addr] = False

   def setSpeed(self, addr, speed):
      if speed < 0.01:
         self.turnOff(self.address[addr])
      elif speed > 1.00:
         print("error can't go higher than 4000 rpm")
      else:
         if self.isOn[addr] == False:
            self.turnOn(self.address[addr])

         FAN_RPS = 2000 * speed / 60 #max speed_rpm * % / 60 to conver to speed_rps
         K_TACH = int(math.floor((992 * self.K_SCALE / speed) - 1))
         print(K_TACH)

         bus = SMBus(1)
         bus.write_byte(multiplexAddr, self.multiplexCh)
         bus.write_byte_data(self.address[addr], SPEED_REGISTER, K_TACH)

def main():
   fcontroller = FanController(7)

if __name__ == '__main__':
   main()
