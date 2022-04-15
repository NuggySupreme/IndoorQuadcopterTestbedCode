import rclpy
from rclpy.node import Node
from bed_messages.msg import PSControl
from std_msgs.msg import String
from smbus2 import SMBus
import sys
import RPi.GPIO as GPIO
import time
import math

multiplexAddr = 0x77

EXTEND = 27
RETRACT = 17

class LinearActuatorController(Node):
   def __init__(self):
      super().__init__('la_controller')
      self.multiplexCh = 0x80 #multiplexer channel
      self.angleSubscriber = self.create_subscription(LAControl, 'la_control_messages', self.lacontrol_callback, 10)
      self.errorPublisher = self.create_publisher(String, 'error_messages', 20)
      self.pitchAngle = 0.00
      self.rollAngle = 0.00
      self.rotated_coords = [0.00, 0.00, 0.00]
      self.table_coords = [0.00, 0.00, 3.00]
      self.base_coords = [0.00, 0.00, 0.00]

      GPIO.setmode(GPIO.BCM)
      GPIO.setup(EXTEND, GPIO.OUT)
      GPIO.setup(RETRACT, GPIO.OUT)
      self.stop()

   def lacontrol_callback(self, msg):
      roll = math.radians(msg.rollAngle)
      pitch = math.radians(msg.pitchAngle)

      self.rotated_coords[0] = 0
   def extend(self):
      try:
         GPIO.output(EXTEND, GPIO.HIGH)
         GPIO.output(RETRACT, GPIO.LOW)
      except:
         e = sys.exc_info()[1]
         self.sendError("LAController/extend: Error extending linear actuator " + str(e))

   def retract(self):
      try:
         GPIO.output(RETRACT, GPIO.HIGH)
         GPIO.output(EXTEND, GPIO.LOW)
      except:
         e = sys.exc_info()[1]
         self.sendError("LAController/retract: Error retracting linear actuator " + str(e))

   def stop(self):
      try:
         GPIO.output(RETRACT, GPIO.LOW)
         GPIO.output(EXTEND, GPIO.LOW)
      except:
         e = sys.exc_info()[1]
         self.sendError("LAController/stop: Error stopping linear actuator " + str(e))

   def sendError(self, str):
      msg = String()
      msg.data = str
      print(msg.data)
      self.errorPublisher.publish(msg)

   def turnOnPowerSupply(self, ps, volt, curr):
      pub = self.create_publisher(PSControl, 'ps_control_messages', 10)
      msg = PSControl()
      msg.ps_num = ps
      msg.voltage = volt
      msg.current = curr
      pub.publish(msg)

def main(args=None):
   rclpy.init(args=args)
   la_controller = LinearActuatorController()
   while True:
      try:
         la_controller.extend()
         time.sleep(5)
         la_controller.retract()
         time.sleep(5)
      except:
         break;

   la_controller.stop()
   GPIO.cleanup()

if __name__ == '__main__':
   main()
