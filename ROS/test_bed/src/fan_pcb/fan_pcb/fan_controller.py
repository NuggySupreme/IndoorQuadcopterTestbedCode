import rclpy #ROS libraries
from rclpy.node import Node

import smbus2 #I2C library
from smbus2 import SMBus

from std_msgs.msg import String
from bed_messages.msg import FanControl

import sys #random other libraries
import os
import time
import math

multiplexAddr = 0x70 #I2C address of multiplexer

SPEED_REGISTER = 0x00 #Value of register sets speed of fans
CONFIG_REGISTER = 0x02 #configuration bits for register
GPIO_DEF_REGISTER = 0x04 #defines purposes of GPIO
TACH0_REGISTER = 0x0C #Read from these registers to get rpm of each fan (not currently used)
TACH1_REGISTER = 0x0E
TACH2_REGISTER = 0x10
TACH3_REGISTER = 0x12
COUNT_REGISTER = 0x16 #Sets count time for tachometer

class FanController(Node):
   def __init__(self, chNum):
      super().__init__('fan_controller')
      self.errorPublisher = self.create_publisher(String, '/error_messages', 20)
      self.subscriber = self.create_subscription(FanControl, '/fan_control_messages', self.fan_callback, 20)
      self.multiplexCh = 2 ** chNum #channel the fan controller is on
      self.address = [0x1b, 0x1f, 0x48, 0x4B] #I2C addresses of fan pcbs
      self.isOn = [False, False, False, False] #tells if fans are on or not
      self.K_SCALE = 4000/60 * (64+1) / 992 #max_rps * (K_TACH (should be around 64) + 1) / 992 since using internal oscillator

      print("Calculated: " + str(self.K_SCALE)) #find closest value of K_SCALE
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

   def fan_callback(self, msg): #address is [0, 3] by integer, speed is a float32 between 0 and 1 inclusive
      self.setSpeed(msg.address % 4, msg.speed)

   def start(self):
      try:
         bus = SMBus(1)
      except:
         e = sys.exc_info()[1]
         self.sendError("FanController/start: Error getting I2C bus " + str(e))

      try:
         bus.write_byte(multiplexAddr, self.multiplexCh)
         time.sleep(0.3)
      except:
         e = sys.exc_info()[1]
         self.sendError("FanController/start: Error changing multiplexer channel " + str(e))

      os.system("i2cdetect -y 1")

      print("Turning off")
      self.turnOffAll()
      time.sleep(5)

      print("Configuring")
      for i in range(4):
         try:
            bus.write_byte_data(self.address[i], GPIO_DEF_REGISTER, 0b00101010)
            time.sleep(0.2)
            bus.write_byte_data(self.address[i], COUNT_REGISTER, 0b00000010)
            time.sleep(0.2)
         except:
            e = sys.exc_info()[1]
            self.sendError("FanController/start: Error configuring registers on pcb at address " + str(self.address[i]) + " " + str(e))

      print("Turning fully on")
      for i in range(4):
         self.fullOn(i)
      time.sleep(10)

      print("Turning off")
      self.turnOffAll()
      time.sleep(10)

      for i in range(4):
         self.setSpeed(i, 0.80)
      self.turnOnAll()
      time.sleep(10)

      for i in range(4):
         self.setSpeed(i, 0.25)
      time.sleep(10)

      for i in range(4):
         self.setSpeed(i, 2.00)
      time.sleep(2)

      self.turnOffAll()

   def fullOn(self, addr): #turn fans at I2C address to full on without control
      try:
         bus = SMBus(1)
      except:
         e = sys.exc_info()[1]
         self.sendError("FanController/fullOn: Error turning on pcb at address " + str(self.address[addr]) + " " + str(e))

      try:
         bus.write_byte(multiplexAddr, self.multiplexCh)
         time.sleep(0.2)
      except:
         e = sys.exc_info()[1]
         self.sendError("FanController/fullOn: error changing multiplexer channel " + str(e))

      try:
         bus.write_byte_data(self.address[addr], CONFIG_REGISTER, 0b00001010)
         self.isOn[addr] = True
         time.sleep(0.2)
      except:
         e = sys.exc_info()[1]
         self.sendError("FanController/fullOn: Error writing to pcb at address " + str(self.address[addr]) + " " + str(e))

   def turnOnAll(self):
      for i in range(4):
         self.turnOn(i)

   def turnOn(self, addr): #turn fans at I2C address on with feedback control
      try:
         bus = SMBus(1)
      except:
         e = sys.exc_info()[1]
         self.sendError("FanController/turnOn: Error getting I2C bus " + str(e))

      try:
         bus.write_byte(multiplexAddr, self.multiplexCh)
         time.sleep(0.2)
      except:
         e = sys.exc_info()[1]
         self.sendError("FanController/turnOn: Error changing multiplexer channel " + str(e))

      try:
         if self.isOn[addr] == False: #do start up sequence defined in MAX6651 datasheet
            bus.write_byte_data(self.address[addr], CONFIG_REGISTER, 0b00001010)
            time.sleep(0.2)
         bus.write_byte_data(self.address[addr], CONFIG_REGISTER, 0b00101010)
         self.isOn[addr] = True
         time.sleep(0.2)
      except:
         e = sys.exc_info()[1]
         self.sendError("FanController/turnOn: Error communicating with pcb at address " + str(self.address[addr]) + " " + str(e))

   def turnOffAll(self):
      for i in range(4):
         self.turnOff(i)

   def turnOff(self, addr): #turn off fans at I2C address
      try:
         bus = SMBus(1)
      except:
         e = sys.exc_info()[1]
         self.sendError("FanController/turnOff: Error getting I2C bus " + str(e))

      try:
         bus.write_byte(multiplexAddr, self.multiplexCh)
         time.sleep(0.2)
         bus.write_byte_data(self.address[addr], CONFIG_REGISTER, 0b00011010)
         self.isOn[addr] = False
         time.sleep(0.2)
      except:
         e = sys.exc_info()[1]
         self.sendError("FanController/turnOff: Error communicating with pcb at address " + str(self.address[addr]) + " " + str(e))

   def setSpeed(self, addr, speed): #set speed of fan as % of max speed
      if speed < 0.01:
         self.turnOff(addr)
      elif speed > 1.00:
         self.sendError("FanController/setSpeed: " + str(speed * 4000) + " rpm is not in the range [0-4000] rpm.")

      else:
         if self.isOn[addr] == False:
            self.turnOn(addr)

         FAN_RPS = 2000 * speed / 60 #max speed_rpm * % / 60 to conver to speed_rps
         K_TACH = int(math.floor((992 * self.K_SCALE / speed) - 1))
         print(K_TACH)

         try:
            bus = SMBus(1)
            bus.write_byte(multiplexAddr, self.multiplexCh)
            time.sleep(0.2)
            bus.write_byte_data(self.address[addr], SPEED_REGISTER, K_TACH)
            time.sleep(0.2)
         except:
            e = sys.exc_info()[1]
            self.sendError("FanController/setSpeed: Error setting speed on pcb with address " + str(self.address[addr]) + " " + str(e))

   def sendError(self, str):
      msg = String()
      msg.data = str
      self.errorPublisher.publish(msg)

def main(args=None):
   rclpy.init(args=args)
   f_controller = FanController(1)
   f_controller.start()
   try:
      rclpy.spin(f_controller)
   except KeyboardInterrupt:
      f_controller.turnOffAll()
   finally:
      f_controller.destroy_node()
      rclpy.shutdown()

if __name__ == '__main__':
   main()
