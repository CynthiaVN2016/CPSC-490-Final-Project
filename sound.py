from psonic import *
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
s = [0]
print("Starting while loop\n")
while True:
	read_serial = ser.read(1).decode()
	print(read_serial)
	# s[0] = str(int (ser.readline(), 16))
	# print s[0]
	# int ascii = ord(read_serial[0])
	if (ord(read_serial[0]) == 36):
		play(70)
	elif (ord(read_serial[0]) == 39):
		play(80)
	else:
		play(60)
