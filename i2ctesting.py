import smbus2
from smbus2 import SMBus
import os
import time


chNum = 0

multiplexAddr = 0x70 #I2C address of multiplexer

ON = 0b10000001
OFF = 0b10000000

CONTROL_REGISTER = 0x7C
VOLTAGE_SET_REGISTER = 0x70
CURRENT_SET_REGISTER = 0x72
VOLTAGE_READ_REGISTER = 0x60
CURRENT_READ_REGISTER = 0x62
psAddrs = [0b1010000, 0b1010001, 0b1010010, 0b1010011] #power supply I2C addresses equates to 0x50-0x53
psStatus = [False, False, False, False] #tells if power supply is on or not
channel = 2 ** chNum #multiplexer channel the power supplies are on

with SMBus(1) as bus:
	bus.write_byte(multiplexAddr, channel)
	time.sleep(0.5)
	os.system("i2cdetect -y 1")
	print("S1")

	for addr in psAddrs:
		bus.write_byte_data(addr,CONTROL_REGISTER,OFF)


	time.sleep(5)
	bus.write_byte(multiplexAddr, channel)


	for addr in psAddrs:

		voltage = 12.00
		current = 60.00

		voltage *= 100
		vAsInt = int(voltage)
		high = (vAsInt & 0xFF00) >> 8
		low = vAsInt & 0x00FF
		bus.write_byte_data(addr, VOLTAGE_SET_REGISTER, low)
		bus.write_byte_data(addr, VOLTAGE_SET_REGISTER+1, high)
		time.sleep(0.1)
		regVal = bus.read_byte_data(addr, CONTROL_REGISTER)
		regVal = regVal | 0b00000100
		bus.write_byte_data(addr, CONTROL_REGISTER, regVal)
		time.sleep(0.1)

		current *= 100
		iAsInt = int(current)
		high = (iAsInt & 0xFF00) >> 8
		low = iAsInt & 0x00FF
		bus.write_byte_data(addr, CURRENT_SET_REGISTER, low)
		bus.write_byte_data(addr, CURRENT_SET_REGISTER+1, high)
		time.sleep(0.1)
		regVal = bus.read_byte_data(addr, CONTROL_REGISTER)
		regVal = regVal | 0b00000100
		bus.write_byte_data(addr, CONTROL_REGISTER, regVal)
		time.sleep(0.1)
		bus.write_byte_data(addr, CONTROL_REGISTER, ON)

	bus.write_byte(multiplexAddr, 2 ** 3)
	time.sleep(.5)
	os.system("i2cdetect -y 1")
	bus.write_byte(multiplexAddr, channel)
