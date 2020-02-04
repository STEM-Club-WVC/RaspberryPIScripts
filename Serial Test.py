import serial
serialport = serial.Serial("/dev/ttyUSB0", 9600, timeout=0.5)
#serialport.write("What you want to send")
while True:
    response = serialport.readlines(None)
    print (response)