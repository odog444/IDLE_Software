# This code will take the UDP command of the FOUR Modes for the digger and implement them.
# One button in the GUI will command each of the Modes and will be recieved by this code!

import smbus
from time import sleep
import socket
import time
import os
import shutil
import subprocess
import RPi.GPIO as GPIO
import random
from git import Repo
import serial
import serial.tools.list_ports
import csv
import threading
from threading import Thread

print('Server is working and listening...')

def cliSer():
    
    buffer = 1024
    ServerPort = 2222
    ServerIP = '172.20.10.7'
    PSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # using UDP

    PSock.bind((ServerIP,ServerPort))
    done = False
    
    while not done:
            command,address = PSock.recvfrom(buffer) # waiting unit Pi connects with client (laptop)
            command = command.decode('utf-8')
            print(command)
            print('Client Address: ', address[0])
            #time.sleep(0.01) #recieving data
            time.sleep(1) # sending data 

# 
# class CustThread(Thread):
#     def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
#         Thread.__init__(self, group, target, name, args, kwargs)
#         self._returnVal = None
#         
#     def run(self):
#         if self._target is not None:
#             self._returnVal = self._target(*self._args, **self._kwargs)
#             
#     def join(self):
#         Thread.join(self)
#         return self._returnVal
        


def senDat():
    
    ser = serial.Serial('/dev/ttyACM0',9600, timeout = 1.0) # MUST HAVE SAME BAUD RATE AS IN ARDUINO CODE!!!
    ser.setDTR(False)
    time.sleep(1)
    ser.flushInput()
    ser.setDTR(True)

    ser.reset_input_buffer()
    print("Serial is working!")
    acc_values = []
    temp_values = []
    pos_count = 0
    buffSize = 2048
    ServerPort = 2224
    ServerIP = '172.20.10.7'
    
    PSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # using UDP
    PSock.bind((ServerIP,ServerPort))
    
#     try:
    while True:
        # Receiving data
        if ser.in_waiting > 0: # returns the number of bytes recieved
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            
            bytesSending = line.encode('utf-8')

            message,address = PSock.recvfrom(buffSize) # waiting unit Pi connects with client
            PSock.sendto(bytesSending,address)

#     except KeyboardInterrupt: # ctrl c to stop
#         print("Close Serial Communication")
#         ser.close()
        
func1 = threading.Thread(target=cliSer, daemon=True)
func2 = threading.Thread(target=senDat, daemon=True)
# func2 = CustThread(target=senDat)

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

