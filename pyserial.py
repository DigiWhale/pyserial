import serial

ser=serial.Serial('/dev/ttyAMA0',115200)
readedText = ser.readline()
print(readedText)
ser.close()