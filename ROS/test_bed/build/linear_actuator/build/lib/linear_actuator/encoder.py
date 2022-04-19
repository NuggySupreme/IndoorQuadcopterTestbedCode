import RPi.GPIO as GPIO
import time

class Encoder:
   def __init__(self, sig1, sig2, callback=None):
      self.sig1Pin = sig1
      self.sig2Pin = sig2
      self.value = 0
      self.state = '00'
      self.direction = None
      self.callback = callback
      GPIO.setup(self.sig1Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
      GPIO.setup(self.sig2Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
      GPIO.add_event_detect(self.sig1Pin, GPIO.BOTH, callback=self.transitionOccurred)
      GPIO.add_event_detect(self.sig2Pin, GPIO.BOTH, callback=self.transitionOccurred)

   def transitionOccurred(self, channel):
      s1 = GPIO.input(self.sig1Pin)
      s2 = GPIO.input(self.sig2Pin)
      newState = "{}{}".format(s1, s2)

      #R = extending
      #L = retracting
      if self.state == "00": #Resting
         if newState == "01":
             self.direction = "E" #extending
         elif newState == "10":
             self.direction = "R" #retracting

      elif self.state == "01": #sig2 leading so extending
         if newState == "11":
            self.direction = "E"
         elif newState == "00": #went in reverse
            if self.direction == "R":
               self.value -= 1
               if self.callback is not None:
                  self.callback(self.value, self.direction)

      elif self.state == "10": #sig1 leading so retracting
         if newState == "11":
            self.direction = "R"
         elif newState == "00":
            if self.direction == "E":
               self.value += 1
               if self.callback is not None:
                  self.callback(self.value, self.direction)

      else: #self.state == "11"
         if newState == "01": #sig1 leading so retracting
            self.direction = "R"
         elif newState == "10": #sig2 leading so extending
            self.direction = "E"
         elif newState == "00": #skipped but direction is good
            if self.direction == "R":
               self.value -= 1
               if self.callback is not None:
                  self.callback(self.value, self.direction)
            elif self.direction == "E":
               self.value += 1
               if self.callback is not None:
                  self.callback(self.value, self.direction)

      self.state = newState

   def getValue(self):
         return self.value

def encoder_callback(value, direction):
   print(str(direction) + ": " + str(value))

def main():
   GPIO.setwarnings(False)
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(22, GPIO.OUT)
   GPIO.setup(23, GPIO.OUT)

   encoder = Encoder(20, 21)

   #23 high retract
   try:
      GPIO.output(23, GPIO.HIGH)
      GPIO.output(22, GPIO.LOW)
      time.sleep(37)
      GPIO.output(23, GPIO.LOW)
      while True:
         encoder.value = 0
         print("22 high")
         GPIO.output(23, GPIO.LOW)
         GPIO.output(22, GPIO.HIGH)

         stop = False
         while not stop:
            if encoder.getValue() >= 4200:
               GPIO.output(22, GPIO.LOW)
               GPIO.output(23, GPIO.LOW)
               stop = True
               print("stop set to true")
            time.sleep(0.02)
         print(encoder.direction + ": " + str(encoder.value))

         maxCount = encoder.value
         time.sleep(5)

         stop = False
         print("23 high")
         GPIO.output(22, GPIO.LOW)
         GPIO.output(23, GPIO.HIGH)

         while not stop:
            if encoder.getValue() <= maxCount / 2:
               GPIO.output(22, GPIO.LOW)
               GPIO.output(23, GPIO.LOW)
               stop = True
               print("stop set to true")
            time.sleep(0.02)
         print(encoder.direction + ": " + str(encoder.value))
         time.sleep(5)

         GPIO.output(23, GPIO.HIGH)
         time.sleep(15)
         GPIO.output(23, GPIO.LOW)
         time.sleep(5)

   except KeyboardInterrupt:
      GPIO.output(22, GPIO.LOW)
      GPIO.output(23, GPIO.LOW)

if __name__ == '__main__':
   main()
