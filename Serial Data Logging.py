import serial
serialport = serial.Serial("/dev/ttyUSB0", 9600, timeout=0.5)
#serialport.write("What you want to send")
while True:
    response = serialport.readlines(None)
    
    for str in response:
        print(str)
    #if (len(response) == 0):
    #    print("Empty.")
    #else:
    #    print (response)
    
