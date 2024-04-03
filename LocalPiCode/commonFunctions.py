# Use this if you're using a function/chunk of code multiple times throughout your file, 
# or if you think you would find the chunk of code/function useful in other functions

# Imports from site-packages
import sys
import socket
import csv
import keyboard
from multiprocessing import Process
import time
import numpy as np
from faker import Faker
import RPi.GPIO as GPIO

# Local imports from IDLE software
import sleepMode
import stopMode
import digMode
import safeMode

'''
NOTES ON PIN USAGE
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


def systemCheck(): # Check if all sensors have nominal readings and 
    if(not checkSensors()):
        return False
    
    return True # If none of the if statements run, everything is in working order

def enterSafeMode():
    # Maybe needs to run some other stuff, but other than that, it just runs safeMode()
    safeMode.SafeMode()
    return


def checkSensors():
    # Check tilt is in correct range
    # Check motor current draws are reasonable and position readings are nominal
    # Check if within temperature bounds

    # If any of the readings are abnormal, return as false. Otherwise, return as true.
    return True

def stopDrum():
    print("Drum stopped") # Placeholder for stopping drum

def startDrum():
    print("Drum Started") # Placeholder for starting drum spin

def lowerDrum():
    print("Drum Lowered") # Placeholder for lowering drum 

def raiseDrum():
    print("Drum Raised") # Placeholder for raising drum

def moveDrum(delay_converted):
    # Send out of 5v GPIO
    pi_pwm = GPIO.PWM(33,1000)
    pi_pwm.start(0)
    pi_pwm.ChangeDutyCycle(delay_converted/10)


def receiveInput():
    modeToEnter = UDPClient.recvfrom(buffer)[0].decode('utf-8') # recvfrom() returns 2 items, so [0] is to signify to only record 1st item. Hopefully should not cause bugs

    match modeToEnter: # Note: Remember to change print statements to send over to GS as statements to be printed on a console
        case "Sleep Mode":
            print("Sleep Mode entered.")
            sleepMode.SleepMode()
        case "Stop Mode":
            print("Stop Mode entered.")
            stopMode.StopMode() # add timer
        case "Dig Mode":
            print("Dig Mode entered.")
            digMode.DigMode()
        case "Safe Mode":
            print("Safe Mode entered.")
            safeMode.SafeMode()
        case _:
            print("Invalid input, please try from the follwing:\n \
            Sleep Mode\n \
            Stop Mode\n \
            Dig Mode\n \
            Safe Mode")
            receiveInput()


            
