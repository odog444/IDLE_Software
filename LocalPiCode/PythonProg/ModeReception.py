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
import socket
from threading import Thread

print('Server is working and listening...')

#Initialize
try:
    ser = serial.Serial('/dev/ttyACM0',115200, timeout = 1.0) # MUST HAVE SAME BAUD RATE AS IN ARDUINO CODE!!!
except:
    ser = serial.Serial('/dev/ttyACM1',115200, timeout = 1.0)

    
ser.setDTR(False)
time.sleep(1)
ser.flushInput()
ser.setDTR(True)

buffer = 2048
ServerPort = 2244
ServerIP = '172.20.10.7'
PSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # using UDP
PSock.bind((ServerIP,ServerPort))
ser.reset_input_buffer()

global command

def cliSer():
    print("Communicating with GS ")
    while True:
        command,address = PSock.recvfrom(buffer) # waiting unit Pi connects with client (laptop)
        command = command.decode('utf-8') + '\n'
        try:
            ser.write(command.encode('utf-8'))
        except Exception as error:
            print(f"Serial write failed with exception {error}")
        print(command)
        time.sleep(0.01)
        
        
def senDat():
    print("Serial is working!")
    
    while True:
        # Receiving data
        if ser.in_waiting > 0: # returns the number of bytes recieved
            if(ser.in_waiting > buffer):
                print("BUFFER OVERFLOW, resetting...")
                ser.reset_input_buffer()
            line = ser.readline().decode('utf-8').rstrip()
            print(f"From serial: {line}")
        time.sleep(0.01)


func1 = threading.Thread(target=cliSer, daemon=True)
func2 = threading.Thread(target=senDat, daemon=True)


func1.start()
func2.start()

# buffSize = 2000
# ServerPort = 2224
# ServerIP = '172.20.10.7'
# bytesSending = func2.encode('utf-8')
# PSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # using UDP
# PSock.bind((ServerIP,ServerPort))
# message,address = PSock.recvfrom(buffSize) # waiting unit Pi connects with client
# message = message.decode('utf-8')
# PSock.sendto(bytesSending,address)


