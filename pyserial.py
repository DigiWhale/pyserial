import serial

ser=serial.Serial('/dev/serial0',115200, timeout = 10)
readedText = ser.read(100).decode('utf-8')
print(readedText)
ser.close()