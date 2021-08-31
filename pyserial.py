import serial

ser=serial.Serial('/dev/serial0',115200, timeout = 10)
readedText = ser.read(100).decode("ascii")
print(readedText)
ser.close()