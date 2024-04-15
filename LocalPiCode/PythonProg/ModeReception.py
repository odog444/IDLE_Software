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

    if ser.in_waiting > 0: # returns the number of bytes recieved
        time.sleep(0.01)
        if(ser.in_waiting > buffSize):
            ser.reset_input_buffer()
            ser.reset_output_buffer()
        else:
            ser.reset_input_buffer()
            ser.write((message + '\n').encode('utf-8'))
            print((message + '\n').encode('utf-8'))
