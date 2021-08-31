import serial

ser=serial.Serial('/dev/ttyAMA0',115200, timeout = 10)
readedText = ser.readline()
print(readedText)
ser.close()