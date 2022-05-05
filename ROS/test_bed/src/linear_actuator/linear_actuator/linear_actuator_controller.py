import rclpy
from rclpy.node import Node
from bed_messages.msg import PSControl
from bed_messages.msg import TableAngle
from std_msgs.msg import String
from smbus2 import SMBus
import sys
import RPi.GPIO as GPIO
import time
import math

from .encoder import Encoder

#GPIO pins 5 and 6 are open if this makes connecting things easier
EXTEND = [17, 22, 8] #R_PWM (orange) for each cable
RETRACT = [27, 23, 25] #LPWM (dark blue)
SIG1 = [20, 19] #light blue/brown
SIG2 = [21, 26] #yellow/green

class LinearActuatorController(Node):
   def __init__(self):
      super().__init__('la_controller')
      self.multiplexCh = 0x80 #multiplexer channel
      self.controlSubscriber = self.create_subscription(TableAngle, 'la_control_messages', self.lacontrol_callback, 10)
      self.angleSubscriber = self.create_subscription(TableAngle, 'table_angle', self.gyro_callback, 10)
      self.errorPublisher = self.create_publisher(String, 'error_messages', 20)
      self.encoder0 = Encoder(SIG1[0], SIG2[0])
      self.encoder1 = Encoder(SIG1[1], SIG2[1])

      self.curPitch = 0.00
      self.curRoll = 0.00
      self.targetPitch = 0.00
      self.targetRoll = 0.00

      self.movements = 0
      self.zeroed = False

      print("Configuring pins")
      GPIO.setmode(GPIO.BCM)
      for i in range(3):
         GPIO.setup(EXTEND[i], GPIO.OUT)
         GPIO.setup(RETRACT[i], GPIO.OUT)
      self.stopAll()
      print("Stopped")

   def gyro_callback(self, msg):
      self.curPitch = msg.pitch
      self.curRoll = msg.roll

   def lacontrol_callback(self, msg):
      if msg.roll <= 30.00 :
         self.targetRoll = msg.roll
      if msg.pitch <= 30.00:
         self.targetPitch = msg.pitch

      self.move()

   def zeroOut(self):
      print("starting zeroing process")

      self.zeroed = False

      print("retracting table")
      self.retract(0) #fully retract table
      self.retract(1)
      self.retract(2)
      time.sleep(40)

      self.stopAll()
      self.encoder0.resetCount()
      self.encoder1.resetCount()
      time.sleep(5)

      print("fully extending")
      self.extend(0) #fully extend table
      self.extend(1)
      self.extend(2)

      stop = [False, False] #change
      while not stop[0] or not stop[1]:
         if self.encoder0.getValue() >= 4200 and not stop[0]:
            self.stop(0)
            stop[0] = True
            print("stopped 0")
         if self.encoder1.getValue() >= 4200 and not stop[1]:
            self.stop(1)
            self.stop(2)
            stop[1] = True
            print("stopped 1 and 2")

         time.sleep(0.02)

      print("figured out max count")
      maxCount = [self.encoder0.getValue(), self.encoder1.getValue()]
      time.sleep(5)
      print("retracting to max count")
      self.retract(0)
      self.retract(1)
      self.retract(2)

      stop = [False, False]
      while not stop[0] or not stop[1]:
         if self.encoder0.getValue() <= maxCount[0] / 2 and not stop[0]:
            self.stop(0)
            stop[0] = True
            print("stopped 0")
         if self.encoder1.getValue() <= maxCount[1] / 2 and not stop[1]:
            self.stop(1)
            self.stop(2)
            stop[1] = True
            print("stopped 1 and 2")

         time.sleep(0.05)

      self.stopAll()
      print("zeroed")
      self.zeroed = True

   def move(self):
      moveX = True
      moveY = True

      while moveX or moveY:
         if abs(self.curPitch - self.targetPitch) > 0.5: #if pitch is outside of tolerance
            if self.curPitch < self.targetPitch: #move table in +y direction
               self.extend(0)
               self.retract(1)
               self.retract(2)
            elif self.curPitch > self.targetPitch: #move table in -y direction
               self.retract(0)
               self.extend(1)
               self.extend(2)
         else: #done moving in the y direction
            self.stopAll()
            moveY = False

         if abs(self.curRoll - self.targetRoll) > 0.5: #if roll is outside of tolerance
            if self.curRoll < self.targetRoll: #move table in +x direction
               self.retract(1)
               self.extend(2)
            elif self.curRoll > self.targetRoll: #move table in -x direction
               self.extend(1)
               self.retract(2)
         else: #done moving in the x direction
            self.stopAll()
            moveX = False
      self.stopAll() #make sure table is not moving
      print("Done moving")

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

   def stopAll(self):
      for i in range(3):
         try:
            GPIO.output(RETRACT[i], GPIO.LOW)
            GPIO.output(EXTEND[i], GPIO.LOW)
         except:
            e = sys.exc_info()[1]
            self.sendError("LAController/stopAll: Error stopping linear actuator " + str(i) + " " +  str(e))

   def stop(self, la_num):
      try:
         GPIO.output(RETRACT[la_num], GPIO.LOW)
         GPIO.output(EXTEND[la_num], GPIO.LOW)
      except:
         e = sys.exc_info()[1]
         self.sendError("LAController/stop: Error stopping linear actuator " + str(la_num) + " " + str(e))

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

   try:
      #turnOnPowerSupply(1, 12.00, 48.00)
      print("attempting to zero out")
      la_controller.zeroOut()
      print("done zeroing")

   except KeyboardInterrupt:
      la_controller.stopAll()
   finally:
      la_controller.stopAll()
      GPIO.cleanup()

if __name__ == '__main__':
   main()
