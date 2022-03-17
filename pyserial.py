# Importing Libraries

import serial
import time
L=figures
arduino = serial.Serial(port='/dev/cu.usbmodem14101', baudrate=9600, timeout=.1)
def write_read(x):
    #arduino.write(str(x).encode())
    arduino.write(bytes(str(x),'utf-8'))
    #print(bytes(x,'utf-8'))
    time.sleep(0.05)
    data = arduino.readline().decode('utf-8')
    return data

write_read("0")   #Le premier nombre est toujours ignoré par arduino

for i in range(len(L)):
    value = write_read(L[i][0])
    print(value)
    value2 = write_read(L[i][1])
    print(value2)
    value3 = write_read(L[i][2])
    print(value3)
    while int(float(value)) != int(float(L[i][0])) or int(float(value2)) != int(float(L[i][1])) :
        print("La valeur envoyée ne correspond pas")
        arduino.write(bytes("n", 'utf-8'))
        value = write_read(L[i][0])
        value2 = write_read(L[i][1])
        value3 = write_read(L[i][2])




