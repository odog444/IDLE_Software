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


# Function for checking if wifi is connected so that auto-run on boot will work:
def checkIfWifiConnected(IP, Port, PSocket):
    try:
        PSocket.bind((IP,Port)) # binding the IP and port, the two (()) are important idk why lol
    except:
        print("Waiting for Wifi")
    else:
        return True
        
#Clear out local folder with IDLE code, then clone fresh copy of github repo
try:
     shutil.rmtree('/home/idle/IDLE_software')
except:
     print("IDLE_software folder is empty, continuting to clone github repo")
 
Repo.clone_from("https://github.com/Rootbryce/IDLE_Software.git", "/home/idle/IDLE_software")

# Initialize GPIO pins on Pi
'''
NOTES ON PIN USAGE
Sensors:
    Current/Motor
    Temperature
    Tilt

Linear Actuator:
    Arduino:
        PWM: pin 9
        pin1: 8
        Pin2: 7
        Pin3: 6
        Read in: 5 from Pi pin 32

    Pi:
        PWM: pin 32

Drum motor:
    Arduino:
        Output drum: pin 3
        PWM input: 10
    
    Pi:
        PWM GPIO 13: pin 33
'''
LinPWMPin = 32
DrumPWMPin = 33


GPIO.setmode(GPIO.BOARD)
GPIO.setup(LinPWMPin, GPIO.OUT) # Linear Actuator control
GPIO.setup(DrumPWMPin, GPIO.OUT) # Drum motor control


# GPIO.setup(8, GPIO.OUT)
# GPIO.setup(7, GPIO.OUT)
# GPIO.setup(6, GPIO.IN)




# Run main.py file