# This code will take the UDP command of the FOUR Modes for the digger and implement them
# One button in the GUI will command each of the Modes and will be recieved by this code

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


class dataInterchange:
    def __init__(self):
        self.buffSize = 1024
        self.ServerPort = 2224
        self.ServerIP = '172.20.10.7'
        self.line = '1'

        #self.func1 = threading.Thread(target=self.cliSer, daemon=True)
        self.func2 = threading.Thread(target=self.senDat, daemon=True)
        self.func2.start()

        #self.func1.start()

    
    #defcliSer(self)




    def senDat(self):
        ser = serial.Serial('/dev/ttyACMO', 9600, timeout = 1.0) #
        ser.setDTR(False)
        ser.flushInput()
        ser.setDTR(True)
        ser.reset._input_buffer()
        print("Serial is working!")

        self.bytesSending = self.line.encode('utf-8')
        self.PSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #using UDP
        self.PSock.bind((self.ServerIP,self.ServerPort))
        print('Server is up and listening...')
        self.message, self.address = self.PSock.recvfrom(self.buffSize) # waiting until Pi connects with client
        self.message = self.message.decode('utf-8')

        while not False:
            # Receiving data
            if ser.in_waiting > 0: # returns the number of bytes received
                time.sleep(0.3)
                if(ser.in_waiting > self.buffSize):
                    print('BUFFER OVERFLOW')
                    ser.reset_input_buffer()
                else: 
                    self.line = ser.readline().decode('utf-8').rstrip()
                    print(self.line)
                    self.bytesSending = self.line.encode('utf-8')
                    self.PSock.sendto(self.bytesSending,self.address)

dataInterchange()









