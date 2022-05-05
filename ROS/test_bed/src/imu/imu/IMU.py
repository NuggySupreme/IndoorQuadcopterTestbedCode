#Connections
#MPU6050 - Raspberry pi
#VCC - 5V  (2 or 4 Board)
#GND - GND (6 - Board)
#SCL - SCL (5 - Board)
#SDA - SDA (3 - Board)

from bed_messages.msg import TableAngle
from .ExtendedKalman import ExtendedKalmanAngle
import smbus2
from smbus2 import SMBus
import time
import math
import numpy
import os
import rclpy
from rclpy.node import Node
ExtkalmanXY = ExtendedKalmanAngle()
kalAngleXY = numpy.array([[0],
                          [0]])
roll = 0
pitch = 0


#Got imu covariance by running 1000 iterations while imu is at rest
imu_Gyro_3x3_covariance = [[.00000012456766, .00000009187997, -.0000000640087827],
                          [.0000000981799756, .00000028781697, -.00000007894519],
                          [-.00000006400878, -.000000078945198, .000000132980758]]
imu_ACC_3x3_covariance = [[.0036716648, .0000768178241, .000120457226],
                          [.000076817824, .0010703847, .00000585599712],
                          [.000120457226, .00000585599712, .00489186089]]

#Process Covarince is estimated by a [2x2] diagonal convariance matrix in which our variance is the time step ^2
#see later in the code to see that
Process_covariance_estimation = numpy.array([[.0001, .000001],      #this is just a place holder, should be calc each time
                                             [.000001,.00001]])


#For getting text file/graphing of my roll and pitch values.
rollandpitch_track = 0



#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43		#gyro data comes out in dps
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47
Device_Address = 0x68   # MPU6050 device address
bus = SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
multiplexAddr = 0x70

#Read the gyro and acceleromater values from MPU6050

class IMU(Node):
   def __init__(self):
      super().__init__('imu_node')
      self.angPub = self.create_publisher(TableAngle, 'imu_angle', 10)

   def pub(self, r, p):
      msg = TableAngle()
      msg.roll = r
      msg.pitch = p
      self.angPub.publish(msg)

def MPU_Init():
    # write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

    # Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

    # Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)

    # Write to Gyro configuration register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

    # Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)


def read_raw_data(addr):
    # Accelero and Gyro value are 16-bit
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr + 1)

    # concatenate higher and lower value
    value = ((high << 8) | low)

    # to get signed value from mpu6050
    if (value > 32768):
        value = value - 65536
    return value

'''all the above is basic code to get our data from the IMU and bus up and running'''

def main(args=None):
   IMUCovariance = True      #set to False if the different covariances of the imu sensor noise are not found
   RestrictPitch = True
   ErrorCovariance = False
   radToDeg = 57.2957786

   os.system("i2cdetect -y 1")
   MPU_Init()

   rclpy.init()
   imu = IMU()
   print("------starting up------")
   time.sleep(5)

   #Read Accelerometer raw value
   accX = read_raw_data(ACCEL_XOUT_H)
   accY = read_raw_data(ACCEL_YOUT_H)
   accZ = read_raw_data(ACCEL_ZOUT_H)

   # Full scale range +/- 250 degree/C as per sensitivity scale factor
   Ax = (accX / 16384.0) -.0096337    #offset
   Ay = (accY / 16384.0) +.0014383
   Az = (accZ / 16384.0) +.033654

   #comment restricPitch out to restrict roll to +- 90 instead
   if RestrictPitch == True:									#eqn 25 and 26 for getting roll and pitch angles
      roll = math.atan2(Ay,Az) #* radToDeg  -- keep in rad
      pitch = math.atan(-Ax / math.sqrt((Ay ** 2) + (Az ** 2))) #* radToDeg  keeping in rad
   else:
      roll = math.atan(Ay/math.sqrt((Ax**2)+(Az**2))) #* radToDeg --keep in rad
      pitch = math.atan2(-Ax,Az) #* radToDeg -- keep in rad

   ExtkalmanXY.setRoll(roll)		#to E_Kalman class class
   ExtkalmanXY.setPitch(pitch)

   #used lated for gettting error covariance matrix p
   hundredstatevals = numpy.array([[roll],
                               [pitch]])

   '''above is getting the roll and pitch from our imu and setting angles/classes up ''' 

   '''below is main code for running algrotihim'''
   timer = time.time()
   data_tracker = 0
   cov_n = 0
   error_n = 0
   while True:     #run for 30 seconds
      #Read Accelerometer raw value
      accX = read_raw_data(ACCEL_XOUT_H)
      accY = read_raw_data(ACCEL_YOUT_H)
      accZ = read_raw_data(ACCEL_ZOUT_H)

      #Read Gyroscope raw value
      gyroX = read_raw_data(GYRO_XOUT_H)
      gyroY = read_raw_data(GYRO_YOUT_H)
      gyroZ = read_raw_data(GYRO_ZOUT_H)

      # Full scale range +/- 250 degree/C as per sensitivity scale factor
      Ax = (accX/16384.0) - .0096337  # w/offsets
      Ay = (accY / 16384.0) + .0014383
      Az = (accZ / 16384.0) + .033654

      Gx = (gyroX / 131) - .4337  # w/offsets
      Gy = (gyroY / 131) + .17565
      Gz = (gyroZ / 131) + .11635

      Gx_rad = Gx / radToDeg      #converting deg/s to rad/s
      Gy_rad = Gy / radToDeg       #converting deg/s to rad/s
      Gz_rad = Gz / radToDeg       #converting deg/s to rad/s

      #See if there is any difference with and without this if possible
      Ax_mpersec = Ax * 9.81      #converting G to m/s^2
      Ay_mpersec = Ay * 9.81      #converting G to m/s^2
      Az_mpersec = Az * 9.81      #converting G to m/s^2

      #Gyroscope rad/s readings into array
      Gyro_data = [Gx_rad, Gy_rad, Gz_rad]
      #Accelerometer G readings into array
      Acc_data = [Ax_mpersec, Ay_mpersec, Az_mpersec]


      dt = time.time() - timer
      timer = time.time()

      # calculating roll and pitch eqn 25 & 26
      if (RestrictPitch):
        roll = math.atan2(Ay_mpersec, Az_mpersec)  # * radToDeg  -- keep in rad
        pitch = math.atan(-Ax_mpersec / math.sqrt((Ay_mpersec ** 2) + (Az_mpersec ** 2)))  # * radToDeg  keeping in rad
      else:
        roll = math.atan(Ay_mpersec / math.sqrt((Ax_mpersec ** 2) + (Az_mpersec ** 2)))  # * radToDeg --keep in rad
        pitch = math.atan2(-Ax_mpersec, Az_mpersec)  # * radToDeg -- keep in rad

      if IMUCovariance == False:
         ExtkalmanXY.CovarianceGet(Gyro_data, Acc_data)
         print("covariance need 1000 iteration", cov_n)
         cov_n = cov_n + 1
         if cov_n == 1000:
            IMUCovariance = True
            ExtkalmanXY.CovarianceGet(Gyro_data, Acc_data, True)
            cov_n = cov_n + 1

      elif ErrorCovariance == False:
         print("getting model error covariance matrix, iteration/100 = ", error_n)
         hundredstatevals = numpy.append(hundredstatevals, [[roll],
                                                              [pitch]], axis=1)
         error_n = error_n + 1
         if error_n == 100: #500 calculations of pitch and roll for initial covariance
            ErrorCovariance = True  #we got the error covariance now
            error_n = error_n + 1
            ExtkalmanXY.setP_errorCivaraince(hundredstatevals)
      else:
         kalAngleXY = ExtkalmanXY.Algorithm(Gyro_data,Acc_data,dt)

         print("Angle X(Roll/Phi): ",(kalAngleXY[0][0] * radToDeg), "Angle Y(Pitch/Theta): ",(kalAngleXY[1][0] * radToDeg))
         print("----------------------------------------------------------")

         imu.pub(kalAngleXY[0][0] * radToDeg, kalAngleXY[1][0] * radToDeg)

         time.sleep(0.2)       #waits 5ms
   imu.destroy_node()
   rclpy.shutdown()
if __name__ == '__main__':
   main()
