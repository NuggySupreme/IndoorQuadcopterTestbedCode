import smbus
class Fan: #object for fan regulator IC
    def __init__(self, address, max_rpm = 4000): #initialization
        self.bus = smbus.SMBus(0)
        self.address = address #I2C address for fan
        self.max_rpm = max_rpm #Maximum safe rpm for fan
        self.target_rpm = 0 #Target RPM for fan to spin at
        self.current_rpm = 0 #Current RPM read from the tachometer
        self.K_SCALE = 4
        self.SPEED_REG = 0x00
        self.CONFIG_REG = 0x02
        self.GPIO_REG = 0x04
        self.TACH_REG_0 = 0x0C
        
        #write 0x2A to configuration register (register 2) for MAX6651
        #write 0x2A to GPIO definition register (register 4)

        self.bus.write_byte_data(address, CONFIG_REG, 0x2A)
        self.bus.write_byte_data(address, GPIO_REG, 0x2A)
        self.bus.write_byte_data(address, SPEED_REG, 0xFF)
        
    def set_speed(self, rpm): 
        if rpm > self.max_rpm:
           self.target_rpm = max_rpm
           print(str(rpm) + "is too high of a setting for fan speed. Speed set to " + str(self.max_rpm));
        elif rpm <= self.max_rpm and rpm > 0: #safeguard against negative rpm
           self.target_rpm = rpm
        else: #rpm is negative
            print("Invalid setting for rpm")
            return

        power_state = self.bus.read_byte_data(address, CONFIG_REG)
        if power_state != 0x2A :
            self.bus.write_byte_data(address, CONFIG_REG, 0x2A)
        t_tach = 1 / (2 * self.target_rpm)#period of tachometer on chip
        k_tach = int(t_tach * self.K_SCALE * 254000 / 128 - 1) #calculate speed register value
        print(k_tach) #send k_tach to IC chip
        
        self.bus.write_byte_data(address, SPEED_REG, k_tach)
        
    def stop(self):
        self.target_rpm = 0
        self.bus.write_byte_data(address, CONFIG_REG, 0x1A) #software shutdown so fan speed is 0
        
    def get_speed(self):
        return self.current_rpm #should probably be reading the current speed of the fan\

    def read_speed(self):
        self.current_rpm = self.bus.read_byte_data(address, TACH_REG_0) #update every 1s for accurate count
        
