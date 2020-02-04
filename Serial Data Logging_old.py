filename="myFile.txt"
datafile=open(filename, 'a')
while True:
    data = ser.readline()
    datafile.write(data)
    print(data);

datafile.close()
ser.close()