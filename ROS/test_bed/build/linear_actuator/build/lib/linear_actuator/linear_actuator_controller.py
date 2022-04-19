import rclpy
from rclpy.node import Node
from bed_messages.msg import PSControl
from std_msgs.msg import String
from smbus2 import SMBus
import sys
import RPi.GPIO as GPIO
import time
import math

from encoder import Encoder

multiplexAddr = 0x77

EXTEND = [22, 19, 26]
RETRACT = [23, 16, 20]

class LinearActuatorController(Node):
   def __init__(self):
      super().__init__('la_controller')
      self.multiplexCh = 0x80 #multiplexer channel
      self.controlSubscriber = self.create_subscription(TableAngle, 'la_control_messages', self.lacontrol_callback, 10)
      self.angleSubscriber = self.create_subscription(TableAngle, 'table_angle', self.gyro_callback, 10)
      self.errorPublisher = self.create_publisher(String, 'error_messages', 20)
      self.curPitch = 0.00
      self.curRoll = 0.00
      self.targetPitch = 0.00
      self.targetRoll = 0.00
      self.count = 0

      self.movements = 0
      self.zeroed = False

      print("Configuring pins")
      GPIO.setmode(GPIO.BCM)
      for i in range(3):
         GPIO.setup(EXTEND[i], GPIO.OUT)
         GPIO.setup(RETRACT[i], GPIO.OUT)
      self.stop()

   def setCount(self, value):
      self.count = value

   def gyro_callback(self, msg):
      self.curPitch = msg.pitch
      self.curRoll = msg.roll

   def lacontrol_callback(self, msg):
      if msg.roll <= 30.00 :
         self.targetRoll = msg.roll
      if msg.pitch <= 30.00:
         self.targetPitch = msg.pitch

      if self.movements >= 10:
         self.zeroOut()
      if self.zeroed == True:
         self.move()

   def zeroOut():
      self.zeroed = False

      self.retract(0) #fully retract table
      #self.retract(1)
      #self.retract(2)
      time.sleep(15)
      self.stop()
      self.count = 0

      time.sleep(0.5)

      self.extend(0) #fully extend table
      #self.extend(1)
      #self.extend(2)
      time.sleep(15)
      self.stop()
      maxCount = self.count

      self.retract(0)
      self.retract(1)
      self.retract(2)

      while self.count > maxCount / 2: #retract to halfway point
         time.sleep(0.05)

      self.stop()
      self.zeroed = True

   def extend(self, la_num):
      try:
         GPIO.output(EXTEND[la_num], GPIO.HIGH)
         GPIO.output(RETRACT[la_num], GPIO.LOW)
      except:
         e = sys.exc_info()[1]
         self.sendError("LAController/extend: Error extending linear actuator " + str(la_num) + " " + str(e))

   def retract(self, la_num):
      try:
         GPIO.output(RETRACT[la_num], GPIO.HIGH)
         GPIO.output(EXTEND[la_num], GPIO.LOW)
      except:
         e = sys.exc_info()[1]
         self.sendError("LAController/retract: Error retracting linear actuator " + str(la_num) + " " + str(e))

   def stop(self):
      for i in range(3):
         try:
            GPIO.output(RETRACT[i], GPIO.LOW)
            GPIO.output(EXTEND[i], GPIO.LOW)
         except:
            e = sys.exc_info()[1]
            self.sendError("LAController/stop: Error stopping linear actuator " + str(i) + " " +  str(e))

   def move(self):
      self.movements += 1

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
   encoder_test = Encoder()

   try:
      #turnOnPowerSupply(1, 12.00, 48.00)
      la_controller.zeroOut()
   except KeyboardInterrupt:
      la_controller.stop()
   finally:
      la_controller.stop()
      GPIO.cleanup()

if __name__ == '__main__':
   main()
