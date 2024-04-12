import smbus
from time import sleep
import socket
import time
import sys
import os
import shutil
import subprocess
import RPi.GPIO as GPIO
import random
import git
from git import Repo
#import MAIN_COMMON.py as mainFile


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
    print("Pulling from origin...")
    repo = git.Repo('/home/idle/software/IDLE_software')
    repo.remotes.origin.pull()
    print("Done!")
except:
    repo.git.stash()
    repo.remotes.origin.pull()
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


# Run main.py file

