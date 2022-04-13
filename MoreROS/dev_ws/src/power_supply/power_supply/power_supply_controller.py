import rclpy
from rclpy.node import Node

from bed_messages.msg import PSControl
from std_msgs.msg import String

from smbus2 import SMBus
import time
import os
import sys

multiplexAddr = 0x77 #address of multiplexer channel

ON = 0b10000001
OFF = 0b10000000

CONTROL_REGISTER = 0x7C
VOLTAGE_SET_REGISTER = 0x70
CURRENT_SET_REGISTER = 0x72
VOLTAGE_READ_REGISTER = 0x60
CURRENT_READ_REGISTER = 0x62

class PowerSupplyController(Node):
   def __init__(self):
      super().__init__('ps_controller')
      self.subscription = self.create_subscription(PSControl, 'ps_control_messages', self.pscontrol_callback, 10)
      self.subscription
      self.errorPublisher = self.create_publisher(String, 'error_messages', 20)

      self.address = [0b1010000, 0b1010001, 0b1010010, 0b1010011]
      self.isOn = [False, False, False, False]
      self.multiplexCh = 0x80

      self.turnOff()

      for i in range(4):
         self.setVoltage(i, 12.00)
         self.setCurrent(i, 48.00)

      print("Turning On At Full power")
      self.turnOn()
      time.sleep(5)
      print("Turning Off")
      self.turnOff()
      time.sleep(5)

      for i in range(4):
         self.setVoltage(i, 8.00)

      self.turnOn()
      time.sleep(5)
      self.turnOff()

      for i in range(4):
         self.setVoltage(i, 12.00)
      self.turnOn()

      print("Done with init")

   def pscontrol_callback(self, msg):
      if msg.voltage == 0.00 and msg.turn_off == 1:
         self.turnOffTarget(msg.ps_num)

      elif msg.voltage >= 0.00:
         if self.isOn[msg.ps_num] == False:
            self.turnOnTarget(msg.ps_num)

         self.setVoltage(msg.ps_num, msg.voltage)

      if msg.current >= 0.00:
         self.setCurrent(msg.ps_num, msg.current)

   def turnOff(self):
      try:
         bus = SMBus(1)
      except:
         e = sys.exc_info()[1]
         self.sendError("PSController/turnOff: Error getting I2C bus " + str(e))

      try:
         bus.write_byte(multiplexAddr, self.multiplexCh)
      except:
         e = sys.exc_info()[1]
         self.sendError("PSController/turnOff: Error changing multiplexer channel " + str(e))

      time.sleep(0.1)

      #try:
         #multiVal = bus.read_byte(multiplexAddr)
         #multiVal = hex(multiVal)
         #print("Multiplexer Value: " , multiVal)
         #os.system("i2cdetect -y 1")
      #except:
         #e = sys.exc_info()[1]
         #self.sendError("PSController: Error reading multiplexer value " + str(e))

      #time.sleep(0.1)

      for i in range(4):
         try:
            bus.write_byte_data(self.address[i], CONTROL_REGISTER, OFF)
            self.isOn[i] = False
         except:
            e = sys.exc_info()[1]
            self.sendError("PSController/turnOff: Error turning off power supply " + str(i) + " " + str(e))

         time.sleep(0.1)

   def turnOffTarget(self, ps):
      try:
         bus = SMBus(1)
         bus.write_byte(multiplexAddr, self.multiplexCh)
         time.sleep(0.1)
         bus.write_byte_data(self.address[ps], CONTROL_REGISTER, OFF)
         time.sleep(0.1)
         self.isOn[ps] = False
      except:
         e = sys.exc_info()[1]
         self.sendError("PSController/turnOffTarget: Error turning off power supply " + str(ps) + " " + str(e))

   def turnOn(self):
      try:
         bus = SMBus(1)
      except:
         e = sys.exc_info()[1]
         self.sendError("PSController/turnOn: Error getting I2C bus " + str(e))

      try:
         bus.write_byte(multiplexAddr, self.multiplexCh)
      except:
         e = sys.exc_info()[1]
         self.sendError("PSController/turnOn: Error changing multiplexer channel " + str(e))

      time.sleep(0.1)

      for i in range(4):
         try:
            bus.write_byte_data(self.address[i], CONTROL_REGISTER, ON)
            self.isOn[i] = True
         except:
            e = sys.exc_info()[1]
            self.sendError("PSController/turnOn: Error turning on power supply " + str(i) + " " + str(e))

         time.sleep(0.1)

   def turnOnTarget(self, ps):
      try:
         bus = SMBus(1)
         bus.write_byte(multiplexAddr, self.multiplexCh)
         time.sleep(0.1)
         bus.write_byte_data(self.address[ps], CONTROL_REGISTER, ON)
         time.sleep(0.1)
         self.isOn[ps] = True
      except:
         e = sys.exc_info()[1]
         self.sendError("PSController/turnOnTarget: Error turning on power supply " + str(ps) + " " + str(e))

   def setVoltage(self, ps_num, voltage):
      if voltage < 0 or voltage > 12.00 :
         self.sendError("PSController/setVoltage: " + voltage + "V is not in the range [0, 12.00]. Please specify a different voltage.")

      else:
         try:
            bus = SMBus(1)
         except:
            e = sys.exc_info()[1]
            self.sendError("PSController/setVoltage: Error getting I2C bus " + str(e))

         try:
            bus.write_byte(multiplexAddr, self.multiplexCh)
         except:
            e = sys.exc_info()[1]
            self.sendError("PSController/setVoltage: Error changing multiplexer channel " + str(e))

         time.sleep(0.1)

         try:
            voltage *= 100
            vAsInt = int(voltage)
            high = (vAsInt & 0xFF00) >> 8
            low = vAsInt & 0x00FF
            bus.write_byte_data(self.address[ps_num], VOLTAGE_SET_REGISTER, low)
            bus.write_byte_data(self.address[ps_num], VOLTAGE_SET_REGISTER+1, high)
         except:
            e = sys.exc_info()[1]
            self.sendError("PSController/setVoltage: Error writing to set register on ps " + str(ps_num) +  " " + str(e))

         time.sleep(0.1)

         try:
            regVal = bus.read_byte_data(self.address[ps_num], CONTROL_REGISTER)
            regVal = regVal | 0b00000100
            bus.write_byte_data(self.address[ps_num], CONTROL_REGISTER, regVal)
         except:
            e = sys.exc_info()[1]
            self.sendError("PSController/setVoltage: Error applying changes to ps " + str(ps_num) +  " " + str(e))

         time.sleep(0.1)

   def setCurrent(self, ps_num, current):
      if current < 0 or current > 48.00 :
         self.sendError("PSController/setCurrent: " + current + "A is not in the range [0, 48.00]. Please specify a different current.")

      else:
         try:
            bus = SMBus(1)
         except:
            e = sys.exc_info()[1]
            self.sendError("PSController/setCurrent: Error getting I2C bus " + str(e))

         try:
            bus.write_byte(multiplexAddr, self.multiplexCh)
         except:
            e = sys.exc_info()[1]
            self.sendError("PSController/setCurrent: Error changing multiplexer channel " + str(e))

         time.sleep(0.1)

         try:
            current *= 100
            iAsInt = int(current)
            high = (iAsInt & 0xFF00) >> 8
            low = iAsInt & 0x00FF
            bus.write_byte_data(self.address[ps_num], CURRENT_SET_REGISTER, low)
            bus.write_byte_data(self.address[ps_num], CURRENT_SET_REGISTER+1, high)
         except:
            e = sys.exc_info()[1]
            self.sendError("PSController/setCurrent: Error writing to set register on ps " + str(ps_num) + " " + str(e))

         time.sleep(0.1)

         try:
            regVal = bus.read_byte_data(self.address[ps_num], CONTROL_REGISTER)
            regVal = regVal | 0b00000100
            bus.write_byte_data(self.address[ps_num], CONTROL_REGISTER, regVal)
         except:
            e = sys.exc_info()[1]
            self.sendError("PSController/setCurrent: Error applying changes to ps " + str(ps_num) + " " + str(e))

         time.sleep(0.1)

   def sendError(self, str):
      msg = String()
      msg.data = str
      self.errorPublisher.publish(msg)

def main(args=None):
   rclpy.init(args=args)
   ps_controller = PowerSupplyController()
   try:
      rclpy.spin(ps_controller)
   except KeyboardInterrupt:
      ps_controller.turnOff()
   finally:
      ps_controller.destroy_node()
      rclpy.shutdown()

if __name__ == '__main__':
   main()
