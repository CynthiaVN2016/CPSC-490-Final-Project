from psonic import *
import serial

# ser = serial.Serial('/dev/ttyUSB0', 9600)
ser = serial.Serial('/dev/tty.SLAB_USBtoUART', 9600)
s = [0]
print("Starting while loop\n")
marioPattern = [6, 6, 6, 4, 6, 8, 1]
pattern = []

def PlayMario():
	notes = [C5,  G4,   E4,   A4,   B4,  Bb4,   A4,  G4,  E5,   G5,  A5,    F5,   G5,   E5,  C5, D5, B4]
	time =  [0.5, 0.5, 0.5, 0.35, 0.35, 0.15, 0.25, .25, .25, 0.25, 0.35, 0.15, 0.35, 0.35, 0.15, 0.15, 0.15]
	for i in range(0, len(notes)):
		play(notes[i], amp=0.25)
		sleep(time[i])

while True:
	read_serial = ord(ser.read(1).decode())
	print(read_serial)
	# s[0] = str(int (ser.readline(), 16))
	# print s[0]
	if (read_serial == 1):
		play(G4)
	elif (read_serial == 2):
		play(A4)
	elif (read_serial == 3):
		play(B4)
	elif (read_serial == 4):
		play(C5)
	elif (read_serial == 5):
		play(D5)
	elif (read_serial == 6):
		play(E5)
	elif (read_serial == 7):
		play(F5)
	elif (read_serial == 8):
		play(G5)
	elif (read_serial == 9):
		play(A5)

	print(len(pattern))
	if (len(pattern) > 6):
		pattern.pop(0)
	pattern.append(read_serial)
	print(pattern)

	if (pattern == marioPattern):
		sleep(0.5)
		PlayMario()


