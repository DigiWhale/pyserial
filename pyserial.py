import serial

ser=serial.Serial('/dev/ttyAMA0',115200, timeout = 10)
ser.open()
readedText = ser.read(ser.inWaiting())
print(readedText)
ser.close()