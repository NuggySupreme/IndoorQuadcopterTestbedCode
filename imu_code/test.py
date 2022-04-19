#!/usr/bin/env python3
import smbus
from time import sleep

PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47

def MPU_Init():
   #write to sample rate register
   bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

   #write to power management register
   bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

   #write to configuration register
   bus.write_byte_data(Device_Address, CONFIG, 0)

   #write to Gyro configuration register
   bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

   #write to interrupt enable register
   bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
   #Accelero and Gyro value are 16-bit
   high = bus.read_byte_data(Device_Address, addr)
   low = bus.read_byte_data(Device_Address, addr+1)

   #concatenate higher and lower value
   value = ((high << 8) | low)

   if(value > 32768):
      value = value - 65536
   return value

bus = smbus.SMBus(1)
Device_Address = 0x68

MPU_Init()

print("Reading Gyroscope and Accelerometer data")

while True:

   acc_x = read_raw_data(ACCEL_XOUT_H)
   acc_y = read_raw_data(ACCEL_YOUT_H)
   acc_z = read_raw_data(ACCEL_ZOUT_H)

   gyro_x = read_raw_data(GYRO_XOUT_H)
   gyro_y = read_raw_data(GYRO_YOUT_H)
   gyro_z = read_raw_data(GYRO_ZOUT_H)

   Ax = acc_x/16384.0
   Ay = acc_y/16384.0
   Az = acc_z/16384.0

   Gx = gyro_x/131.0
   Gy = gyro_y/131.0
   Gz = gyro_z/131.0

   print("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+"/s", "\tGz=%.2f" %Gz, u'\u00b0'+"/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay,"\tAz=%.2f" %Az)
   sleep(1)

