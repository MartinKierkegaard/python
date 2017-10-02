import smbus
bus = smbus.SMBus(1)
print("Read from analog to digital converter")
print("Ctrl+c to stop")
# the converter has 4 channels you can choose 
#00x0, lys
#00x1, analog input
#00x2, temp
#00x3, potentiometer 
#choose to read from onboard light sensor / 0
#bus.write_byte(0x48, 0x00)
#choose to read from onboard potentiometer

bus.write_byte(0x48, 0x03)
reading=bus.read_byte(0x48)


# set last read data....
last_reading = -1
# do forever...
while (True):
#read analog
	reading=bus.read_byte(0x48)
	if (abs(last_reading - reading) > 2):
		bus.write_byte(0x48, 0x00)
		reading0=bus.read_byte(0x48)	
		# print data
		print(reading)
		print(reading0)
		# store data as last data
		last_reading = reading


