# This code will take the UDP command of the FOUR Modes for the digger and implement them.
# One button in the GUI will command each of the Modes and will be recieved by this code!

import smbus
from time import sleep
import socket
import time
import os
import shutil
import subprocess
import random
from git import Repo
import serial
import serial.tools.list_ports
import csv
import threading
from threading import Thread

def usleep(us):
    startTime = time.time()
    while((time.time() - startTime) * 1e6 > us):
        pass

buffSize = 2048
ServerPort = 2244
ServerIP = '172.20.10.7'


ser = serial.Serial('/dev/ttyACM0',9600, timeout = 1.0, xonxoff = True)
ser.close()
ser.open()
ser.reset_input_buffer()
PSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #using UDP
PSock.bind((ServerIP,ServerPort))
readbackArd = ""

while not False:
    message, address = PSock.recvfrom(buffSize) # waiting until Pi connects with client
    message = message.decode('utf-8') 
    try:
        readbackArd = ser.readline().decode('ascii').rstrip()
    except:
        pass              
    # print("Ard:", readbackArd, "Pi:", message)

    if ser.in_waiting > 0: # returns the number of bytes recieved
        time.sleep(0.01)
#         try: #microsecond delay to match up with drum motor dlay
#             usDelay = int(message)
#             usleep(usDelay)
#         except:
#             pass
        # print(self.ser.in_waiting)
        if(ser.in_waiting > buffSize):
            # print("BUFFER OVERFLOW, resetting...")
            # ser.flush()
            ser.reset_input_buffer()
            ser.reset_output_buffer()
        else:
            ser.reset_input_buffer()
            ser.write((message + '\n').encode('utf-8'))
            print((message + '\n').encode('utf-8'))
            #print(message)
            #readbackArd = ser.read()#.decode('utf-8').rstrip()
            #print(readbackArd)

# class CONTROL:
#     def __init__(self):
#         self.buffSize = 4096
#         self.ServerPort = 2244
#         self.ServerIP = '172.20.10.7'
# 
#         # try:
#         #     ser = serial.Serial('/dev/ttyACM0',115200, timeout = 1.0) # MUST HAVE SAME BAUD RATE AS IN ARDUINO CODE!!!
#         # except:
#         #     ser = serial.Serial('/dev/ttyACM1',115200, timeout = 1.0)
#          
#         self.ser = serial.Serial('/dev/ttyACM0',115200, timeout = 1.0)
#         self.ser.setDTR(False)
#         self.ser.flushInput()
#         self.ser.setDTR(True)
#         # self.ser.reset_input_buffer()
#         self.ser.flush()
#         self.message = ''
#         
#         func1 = threading.Thread(target=self.GetCommand, daemon=True)
#         func2 = threading.Thread(target=self.SendCommand2Ard, daemon=True)
#         
#         func1.start()
#         func2.start()
#         func2.join()
#         print("Serial is working!")
#     def GetCommand(self):
#         while not False:
#                 self.PSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #using UDP
#                 self.PSock.bind((self.ServerIP,self.ServerPort))
#                 self.message, self.address = self.PSock.recvfrom(self.buffSize) # waiting until Pi connects with client
#                 self.message = self.message.decode('utf-8')
#                         
#     def SendCommand2Ard(self):
#         while not False:
#                 if self.ser.in_waiting > 0: # returns the number of bytes recieved
#                     time.sleep(0.3)
#                     # print(self.ser.in_waiting)
#                     if(self.ser.in_waiting > self.buffSize):
#                         print("BUFFER OVERFLOW, resetting...")
#                         self.ser.flush()
#                         # ser.reset_output_buffer()
#                     else:
#                         self.ser.write(self.message.encode('utf-8'))
#                         print(self.message)
#             
#         
# CONTROL()
