import RPi.GPIO as GPIO
import time

EXTEND = 23 #22
RETRACT = 22 #23

print("Configuring Pins")
GPIO.setmode(GPIO.BCM)
GPIO.setup(EXTEND, GPIO.OUT)
GPIO.setup(RETRACT, GPIO.OUT)

GPIO.output(EXTEND, GPIO.LOW)
GPIO.output(RETRACT, GPIO.LOW)

print("RETRACTING")
GPIO.output(RETRACT, GPIO.HIGH)
GPIO.output(EXTEND, GPIO.LOW)

print("WAITING")
time.sleep(20)

print("STOPPING")
GPIO.output(EXTEND, GPIO.LOW)
GPIO.output(RETRACT, GPIO.LOW)

print("ENDING")
GPIO.cleanup()
