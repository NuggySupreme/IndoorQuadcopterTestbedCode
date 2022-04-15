import rclpy
from rclpy.node import Node

from bed_messages.msg import PSControl
from smbus2 import SMBus
import time
import os

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
      self.subscription = self.create_subscription(PSControl, 'ps_control_messages', self.listener_callback, 10)
      self.subscription
      self.address = [0b1010000, 0b1010001, 0b1010010, 0b1010011]

      self.turnOff()
      time.sleep(5)
#      self.turnOn()
#      time.sleep(5)
#      self.turnOff()

#      self.setVoltage(self.address[3], 12.00)
      #setCurrent(self.address[3], 2.00)

   def listener_callback(self, msg):
      self.setVoltage(msg.fan_num, msg.voltage)

   def turnOff(self):
      #for i in range(4):
      #   bus.write_byte_data(self.address[i], CONTROL_REGISTER, OFF)
      bus = SMBus(1)
      time.sleep(5)
      bus.write_byte(0x77, 0x80)
      time.sleep(1)
      os.system("i2cdetect -y 1")
      time.sleep(1)
      bus.write_byte_data(self.address[3], CONTROL_REGISTER, OFF)
      time.sleep(1)

   def turnOn(self):
      #for i in range(4):
      #   bus.write_byte_data(self.address[i], CONTROL_REGISTER, ON)
      self.bus.write_byte(0x77, 0x80)
      time.sleep(1)
      self.bus.write_byte_data(self.address[3], CONTROL_REGISTER, ON)
      time.sleep(1)

   def setVoltage(self, ps_num, voltage):
      if voltage < 0 or voltage > 12.00 :
         print("The voltage specified is not in the range [0, 12.00]. Please specify a different voltage.")
      else:
         voltage *= 100
         vAsInt = int(voltage)
         high = (vAsInt & 0xFF00) >> 8
         low = vAsInt & 0x00FF
         print("High: %d, Low: %d" % (high, low))

def main(args=None):
   rclpy.init(args=args)
   ps_controller = PowerSupplyController()
   rclpy.spin(ps_controller)
   ps_controller.destroy_node()
   rclpy.shutdown()

if __name__ == '__main__':
   main()
