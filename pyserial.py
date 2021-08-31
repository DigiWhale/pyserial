import serial

ser=serial.Serial('/dev/serial0',115200, timeout = 10)
readedText = ser.read(ser.inWaiting())
print(readedText)
ser.close()