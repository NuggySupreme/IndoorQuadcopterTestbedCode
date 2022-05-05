import rclpy #ROS libraries
from rclpy.node import Node

from bed_messages.msg import PSControl #ROS messages
from std_msgs.msg import String

import smbus2
from smbus2 import SMBus #I2C library
import time #random other libraries
import os
import sys


multiplexAddr = 0x70 #I2C address of multiplexer

ON = 0b10000001
OFF = 0b10000000

CONTROL_REGISTER = 0x7C
VOLTAGE_SET_REGISTER = 0x70
CURRENT_SET_REGISTER = 0x72
VOLTAGE_READ_REGISTER = 0x60
CURRENT_READ_REGISTER = 0x62

class PowerSupplyController(Node):
   def __init__(self, chNum):
      super().__init__('ps_controller')
      self.subscription = self.create_subscription(PSControl, '/ps_control_messages', self.pscontrol_callback, 10)
      self.errorPublisher = self.create_publisher(String, '/error_messages', 20)

      print("init i2cdetect")
      os.system("i2cdetect -y 1")
      self.address = [0b1010000, 0b1010001, 0b1010010, 0b1010011] #power supply I2C addresses equates to 0x50-0x53
      self.isOn = [False, False, False, False] #tells if power supply is on or not
      self.multiplexCh = 2 ** chNum #multiplexer channel the power supplies are on

   def pscontrol_callback(self, msg):
      if msg.voltage == 0.00 and msg.turn_off == 1: #turn off power supply if it should be
         self.turnOffTarget(msg.ps_num)

      elif msg.voltage >= 0.00 and msg.voltage <= 12.00: #otherwise change the output voltage to what the message says
         if self.isOn[msg.ps_num] == False: #if the power supply to change isn't on, turn it on
            self.turnOnTarget(msg.ps_num)

         self.setVoltage(msg.ps_num, msg.voltage) #set the output voltage

      if msg.current >= 0.00: #set the maximum output current to what it is set to in the message
         self.setCurrent(msg.ps_num, msg.current)

      print("callback i2cdetect")
      os.system("i2cdetect -y 1")

   def start(self): #start up sequence for the power supplies
      print("Start() i2cdetect")
      os.system("i2cdetect -y 1")
      self.turnOff() #turn on
      for i in range(4):
         self.setVoltage(i, 12.00) #set the output voltage and max current
         self.setCurrent(i, 60.00)
      print("Turning on at full power")
      self.turnOn()
      time.sleep(5)
      print("Turning off")
      self.turnOff()
      time.sleep(5)
      print("Turning back on")
      self.turnOn()
      print("Done with init")

   def turnOff(self): #turn off all power supplies
      for i in range(4):
         self.turnOffTarget(i)

   def turnOffTarget(self, ps): #turn off specific power supply
      #try: #get i2c bus
      #   bus = SMBus(1)
      #except:
      #   e = sys.exc_info()[1]
      #   self.sendError("PSController/turnOffTarget: Error getting I2C bus " + str(e))

      with SMBus(1) as bus:
         try: #change multiplexer channel to one with power supplies on it
            bus.write_byte(multiplexAddr, self.multiplexCh)
            time.sleep(0.1)
         except:
            e = sys.exc_info()[1]
            self.sendError("PSController/turnOffTarget: Error changing multiplexer channel " + str(e))

         try: #write to power supply
            bus.write_byte_data(self.address[ps], CONTROL_REGISTER, OFF)
            time.sleep(0.1)
            self.isOn[ps] = False
         except:
            e = sys.exc_info()[1]
            self.sendError("PSController/turnOffTarget: Error turning off power supply " + str(ps) + " " + str(e))

   def turnOn(self): #turn on all power supplies
      for i in range(4):
         self.turnOnTarget(i)

   def turnOnTarget(self, ps): #turn on specific power supply
      #try: #get i2c bus
      #   bus = SMBus(1)
      #except:
      #   e = sys.exc_info()[1]
      #   self.sendError("PSController/turnOnTarget: Error getting I2C bus " + str(e))

      with SMBus(1) as bus:
         try: #change multiplexer channel to one with power supplies on it
            bus.write_byte(multiplexAddr, self.multiplexCh)
            time.sleep(0.1)
         except:
            e = sys.exc_info()[1]
            self.sendError("PSController/turnOnTarget: Error changing multiplexer channel " + str(e))

         try: #write to power supply
            bus.write_byte_data(self.address[ps], CONTROL_REGISTER, ON)
            time.sleep(0.1)
            self.isOn[ps] = True
         except:
            e = sys.exc_info()[1]
            self.sendError("PSController/turnOnTarget: Error turning on power supply " + str(ps) + " " + str(e))

   def setVoltage(self, ps_num, voltage): #set power supply voltage
      if voltage < 0 or voltage > 12.00:
         self.sendError("PSController/setVoltage: " + voltage + "V is not in the range [0, 12.00]. Please specify a different voltage.")

      else:
         #try: #get i2c bus
         #   bus = SMBus(1)
         #except:
         #   e = sys.exc_info()[1]
         #   self.sendError("PSController/setVoltage: Error getting I2C bus " + str(e))
         with SMBus(1) as bus:
            try: #change multiplexer channel
               bus.write_byte(multiplexAddr, self.multiplexCh)
               time.sleep(0.1)
            except:
               e = sys.exc_info()[1]
               self.sendError("PSController/setVoltage: Error changing multiplexer channel " + str(e))

            try: #convert voltage appropriately 12.96V -> gets sent as hex(12) and hex(96)
               voltage *= 100
               vAsInt = int(voltage)
               high = (vAsInt & 0xFF00) >> 8
               low = vAsInt & 0x00FF
               bus.write_byte_data(self.address[ps_num], VOLTAGE_SET_REGISTER, low)
               bus.write_byte_data(self.address[ps_num], VOLTAGE_SET_REGISTER+1, high)
               time.sleep(0.1)
            except:
               e = sys.exc_info()[1]
               self.sendError("PSController/setVoltage: Error writing to set register on ps " + str(ps_num) +  " " + str(e))

            try: #apply changes to power supply
               regVal = bus.read_byte_data(self.address[ps_num], CONTROL_REGISTER)
               regVal = regVal | 0b00000100
               bus.write_byte_data(self.address[ps_num], CONTROL_REGISTER, regVal)
               time.sleep(0.1)
            except:
               e = sys.exc_info()[1]
               self.sendError("PSController/setVoltage: Error applying changes to ps " + str(ps_num) +  " " + str(e))

   def setCurrent(self, ps_num, current): #set power supply current
      if current < 0 or current > 60.01 :
         self.sendError("PSController/setCurrent: " + current + "A is not in the range [0, 48.00]. Please specify a different current.")

      else:
         #try: #get i2c bus
         #   bus = SMBus(1)
         #except:
         #   e = sys.exc_info()[1]
         #   self.sendError("PSController/setCurrent: Error getting I2C bus " + str(e))
         with SMBus(1) as bus:
            try: #change multiplexer channel
               bus.write_byte(multiplexAddr, self.multiplexCh)
               time.sleep(0.1)
            except:
               e = sys.exc_info()[1]
               self.sendError("PSController/setCurrent: Error changing multiplexer channel " + str(e))

            try: #set current appropriately 12.96A -> gets sent as hex(12) and hex(96)
               current *= 100
               iAsInt = int(current)
               high = (iAsInt & 0xFF00) >> 8
               low = iAsInt & 0x00FF
               bus.write_byte_data(self.address[ps_num], CURRENT_SET_REGISTER, low)
               bus.write_byte_data(self.address[ps_num], CURRENT_SET_REGISTER+1, high)
               time.sleep(0.1)
            except:
               e = sys.exc_info()[1]
               self.sendError("PSController/setCurrent: Error writing to set register on ps " + str(ps_num) + " " + str(e))

            try: #apply changes to multiplexer
               regVal = bus.read_byte_data(self.address[ps_num], CONTROL_REGISTER)
               regVal = regVal | 0b00000100
               bus.write_byte_data(self.address[ps_num], CONTROL_REGISTER, regVal)
               time.sleep(0.1)
            except:
               e = sys.exc_info()[1]
               self.sendError("PSController/setCurrent: Error applying changes to ps " + str(ps_num) + " " + str(e))

   def sendError(self, str): #publish error message
      msg = String()
      msg.data = str
      self.errorPublisher.publish(msg)

def main(args=None):
   rclpy.init(args=args) #start ROS node
   ps_controller = PowerSupplyController(0) #create controller object
   ps_controller.start() #do startup sequence
   try:
      rclpy.spin(ps_controller) #spin ROS node so it can receive messages until it is stopped manually
   except KeyboardInterrupt:
      ps_controller.turnOff() #when node is stopped, turn off power supplies
   finally:
      ps_controller.destroy_node() #destroy ROS node
      rclpy.shutdown() #ROS cleanup

if __name__ == '__main__':
   main()
