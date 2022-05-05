#Callen Zimmer Extend Kalman Filter Code Class
#last Updated on 4/30/2022

import numpy
import math

class ExtendedKalmanAngle:
    def __init__(self):

        self.QAngle = 0.001
        self.QBias = 0.003
        self.RMeasure = 0.03
        self.angle = 0.0
        self.Roll = 0.0
        self.Pitch = 0.0
        self.bias = 0.0
        self.rate = 0.0
        self.P=[[0.0,0.0],[0.0,0.0]]        #p is a 2x2 matrix
        self.Gyro_raws_array = []
        self.Acc_raws_array = []
        self.Gyro_Cov = 0
        self.Acc_Cov = 0
        self.first_input = 0

        # Got imu covariance by running 1000 iterations while imu is at rest
        self.imu_Gyro_3x3_covariance = numpy.array([[.00000012456766, .00000009187997, -.0000000640087827],
                                   [.0000000981799756, .00000028781697, -.00000007894519],
                                   [-.00000006400878, -.000000078945198, .000000132980758]])
        self.imu_ACC_3x3_covariance = numpy.array([[.0036716648, .0000768178241, .000120457226],
                                  [.000076817824, .0010703847, .00000585599712],
                                  [.000120457226, .00000585599712, .00489186089]])

        # Process Covarince is estimated by a [2x2] diagonal convariance matrix in which our variance is the time step ^2
        # see later in the code to see that
        self.Process_covariance_estimation = 0

        #This is a variable for our theta and phi/ where Roll (Phi) and Pitch (theta)
        self.Xn_1 = numpy.array([[self.Roll],   #Phi    --roll
                     [self.Pitch]])   #Theta  --pitch

        self.Xn = numpy.array([[self.Roll],  # Phi    --roll
                            [self.Pitch]])  # Theta  --pitch

        self.Pn_1 = numpy.array([[0],
                                [0]])  #ERROR covariance matrix P

        self.Pn =  numpy.array([[.0001, .000001],
                                             [.000001,.00001]])

        self.KalmanGain = numpy.array([[0, 0, 0],       #kalman gain should be 2x3 array
                                        [0, 0, 0]])

        self.I = numpy.identity(2)
        '''def kalman():
        QAngle = 0.001
        QBias = 0.003
        RMeasure = 0.03

        angle = 0.0
        bias = 0.0

        P[0][0] = 0.0
        P[0][1] = 0.0
        P[1][0] = 0.0
        P[1][1] = 0.0'''

    def CovarianceGet(self, Gyro_rate, Acc_rate, ReadytoCalc = False):  #takes the gyro rate data and the accelerometer rating data
        '''Covariance of the sensor noise is calculated based on the imu being level, upright, and static'''
        if ReadytoCalc == False:
            if self.first_input == 0:
                self.first_input = 1
                self.Gyro_raws_array = [Gyro_rate]
                self.Acc_raws_array = [Acc_rate]
            else:
                self.Gyro_raws_array = numpy.append(self.Gyro_raws_array, [Gyro_rate], axis = 0)
                self.Acc_raws_array = numpy.append(self.Acc_raws_array, [Acc_rate], axis = 0)
        elif ReadytoCalc == True:
            self.Gyro_raws_array = self.Gyro_raws_array.T
            self.Acc_raws_array = self.Acc_raws_array.T
            #getting actual covariances matrixes [should be 3x3]
            self.Gyro_Cov = numpy.cov(self.Gyro_raws_array)
            self.Acc_Cov = numpy.cov(self.Acc_raws_array)
            print("Gyro Covariance is = self.Gyro_Cov =", self.Gyro_Cov)
            print("Acc Covariance is = self.Acc_Cov =", self.Acc_Cov)
            self.imu_Gyro_3x3_covariance = self.Gyro_Cov
            self.imu_ACC_3x3_covariance = self.Acc_Cov
        else:
            print("error in covariance get")
        return

    def Algorithm(self,gyro_values,Acc_values,dt):    #get angle is recieving accelerometer calc roll, gyro dps roll, and dt(time difference from last run)

        #this break code dont do
        #self.Xn = numpy.array([[self.Roll],  # Phi    --roll
                               # [self.Pitch]])  # Theta  --pitch

        #process noise model
        self.Process_covariance_estimation = numpy.array([[(dt ** 2), 0],
                                                [0, (dt ** 2)]])

        '''prediction'''
        #step 1
        self.Xn_1 = self.Xn + (dt * self.EurlerratesModel(self.Xn,gyro_values))

        #step 2
        A = self.EulermodelJacobian(self.Xn,gyro_values)
        self.Pn_1 = self.Pn + (dt * (numpy.matmul(A,self.Pn) + numpy.matmul(self.Pn,(A.T)) + self.Process_covariance_estimation))

        '''Correction'''
        #step 3
        C = self.AccelerometerModelJacobian(self.Xn_1, Acc_values)      #note here that we are now using the new predicted Xn-1 for jacobian -- in notes
        R = self.imu_ACC_3x3_covariance

        # self.KalmanGain = self.Pn_1 * C.T * ((C * self.Pn_1 * C.T) + R))^-1     #note using predicted covariance here
        firstpart_Kgain = numpy.matmul(self.Pn_1, (C.T))
        secondpart_Kgain = numpy.matmul(C, self.Pn_1)
        thirdpart_Kgain = numpy.linalg.inv(numpy.matmul(secondpart_Kgain, (C.T)) + R)  # note using predicted covariance here
        self.KalmanGain = numpy.matmul(firstpart_Kgain, thirdpart_Kgain)

        #step 4 -- Xn-1 correction
        #self.Xn_1 = Self.Xn_1 + self.KalmanGain * (y - Accelerometermodel(self.Xn_1,Acc_vales))
        y = numpy.array([[Acc_values[0]],
                         [Acc_values[1]],
                         [Acc_values[2]]])
        Real_minus_prediction = y - self.AccelerometerModel(self.Xn_1,Acc_values)
        self.Xn_1 = self.Xn_1 + numpy.matmul(self.KalmanGain, Real_minus_prediction)

        #step 5 updating covariance
        #self.Pn_1 = (I - K * C) * self.Pn_1
        KtimesC = numpy.matmul(self.KalmanGain,C)
        parrenthesis = (self.I - KtimesC)
        self.Pn_1 = numpy.matmul(parrenthesis, self.Pn_1)       #updating our error covariance 2x2

        #updating values for next iterations
        self.Xn = self.Xn_1
        self.P = self.Pn_1

        #print("error_covariance =", self.Pn_1)

        return self.Xn_1        #gives 2x1 matrix [[roll(phi)],[pitch(theta)]]


    #My Model for the prediction step
    def EurlerratesModel(self, Xn, gyro_values):
        gyro_values = numpy.array([gyro_values])
        transpose = gyro_values.T
        Mapping_matrix = [[1, numpy.sin(Xn[0][0])*numpy.tan(Xn[1][0]), numpy.cos(Xn[0][0])*numpy.tan(Xn[1][0])],
                          [0, numpy.cos(Xn[0][0]), -numpy.sin(Xn[0][0])]]
        self.Eurlerrates = numpy.matmul(Mapping_matrix,transpose)       #+ model noise 2x2 -- no way of currently estimat
        return self.Eurlerrates

    def EulermodelJacobian(self, Xn, gyrorates):
        jacobianofmodel = numpy.array([[((gyrorates[1] * numpy.cos(Xn[0][0]) * numpy.tan(Xn[1][0])) -
                                         (gyrorates[2] * numpy.sin(Xn[0][0]) * numpy.tan(Xn[1][0]))),
                                        ((gyrorates[1] * numpy.sin(Xn[0][0]) * ((1 / (numpy.cos(Xn[1][0]))) ** 2)) +
                                         (gyrorates[2] * numpy.cos(Xn[0][0]) * ((1 / (numpy.cos(Xn[1][0]))) ** 2)))],
                                       [((-gyrorates[1] * numpy.sin(Xn[0][0])) - gyrorates[2] * numpy.cos(Xn[0][0])),
                                        0]])
        return jacobianofmodel

    def AccelerometerModel(self, Xn, Acc_vals): #this is subject to change depending on which model I am using mine
        gravity_normalized = math.sqrt(((Acc_vals[0])**2) + ((Acc_vals[1])**2) + ((Acc_vals[2])**2))
        accel_array = numpy.array([[-numpy.sin(Xn[1][0])],
                                   [numpy.cos(Xn[1][0])*numpy.sin(Xn[0][0])],
                                   [numpy.cos(Xn[1][0])*numpy.cos(Xn[0][0])]])
        accel_model = gravity_normalized * accel_array
        return accel_model

    def AccelerometerModelJacobian(self, Xn, Acc_vals): #also subject to change depending on the model
        gravity_normalized = math.sqrt(Acc_vals[0]**2 + Acc_vals[1]**2 + Acc_vals[2]**2)
        accel_partial = numpy.array([[0, -numpy.cos(Xn[1][0])],
                                     [numpy.cos(Xn[1][0])*numpy.cos(Xn[0][0]), -numpy.sin(Xn[1][0])*numpy.sin(Xn[0][0])],
                                     [numpy.cos(Xn[1][0])*-numpy.sin(Xn[0][0]), -numpy.sin(Xn[1][0])*numpy.cos(Xn[0][0])
                                      ]])
        acc_jackob = gravity_normalized * accel_partial
        return acc_jackob


    def setRoll(self,angle):
        self.Roll = angle
        self.Xn[0][0] = self.Roll

    def setPitch(self,angle):
        self.pitch = angle
        self.Xn[1][0] = self.pitch

    def setP_errorCivaraince(self,mat_of_vals): #takes input of inital roll and pitch calcs
        self.Pn = numpy.cov(mat_of_vals)
        #print("P_errorCovariance initial =", self.Pn)

    def setQAngle(self,QAngle):
        self.QAngle = QAngle

    def setQBias(self,QBias):
        self.QBias = QBias

    def setRMeasure(self,RMeasure):
        self.RMeasure = RMeasure
