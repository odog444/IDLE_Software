# !/usr/bin/env python3

import serial
import serial.tools.list_ports
import time
import csv

ser = serial.Serial('/dev/ttyACM0',9600, timeout = 1.0) # MUST HAVE SAME BAUD RATE AS IN ARDUINO CODE!!!
ser.setDTR(False)
time.sleep(1)
ser.flushInput()
ser.setDTR(True)
# if you don't use the above timeout = 1.0, you will have an infinite timeout possibility
ser.reset_input_buffer()
print("Serial is working!")
acc_values = []
temp_values = []
pos_count = 0
try:
    while True:
        #time.sleep(0.01) #recieving data
        time.sleep(1) # sending data

        # Receiving data
        if ser.in_waiting > 0: # returns the number of bytes recieved
            line = ser.readline().decode('utf-8').rstrip()
            if line == "Temp:":
                print("Temp:")
            elif line == "Acceleration":
                print("Acc:")
            else:
                pos_count += 1
                if (pos_count % 2) == 0:
                    acc_values = [float(x) for x in line.split(',')]
                    acc_values.append(acc_values)
                    print(acc_values)
                else:
                    temp_values = [float(x) for x in line.split(',')]
                    temp_values.append(temp_values)
                    print(temp_values)          
                
#             with open("sens_data.csv", 'w') as file:
#                 csvwrite = csv.writer(file)
#                 csvwrite.writerow(sens_values)
#                 X_acc = sens_values[0]
#                 Y_acc = sens_values[1]
#                 Z_acc = sens_values[2]

        # Sending data
        #print("sending data")
        #ser.write("Hello from Raspberry Pi \n".encode('utf-8'))

        # Bidirectional data
        #print("send message to Arduino")
        #  ser.write("Heyo \n".encode('utf-8'))
        # while ser.in_waiting <= 0:
        #     time.sleep(0.01)
        # rep = ser.readline().decode('utf-8').rstrip()
        # print(rep)
except KeyboardInterrupt: # ctrl c to stop
    print("Close Serial Communication")
    ser.close()
    
# file.close()