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

# Local imports from IDLE software
import sleepMode
import safeMode
import digMode
import safeMode

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
    pass # Placeholder for stopping drum

def startDrum():
    pass # Placeholder for starting drum spin

def lowerDrum():
    pass # Placeholder for lowering drum 

def raiseDrum():
    pass # Placeholder for raising drum

def receiveInput():
    modeToEnter = UDPClient.recvfrom(buffer)[0].decode('utf-8') # recvfrom() returns 2 items, so [0] is to signify to only record 1st item. Hopefully should not cause bugs

    match modeToEnter: # Note: Remember to change print statements to send over to GS as statements to be printed on a console
        case "Sleep Mode":
            print("Sleep Mode entered.")
            sleepmode.SleepMode()
        case "Stop Mode":
            print("Stop Mode entered.")
            stopMode.StopMode()
        case "Dig Mode":
            print("Dig Mode entered.")
            digMode.DigMode()
        case "Safe Mode":
            print("Safe Mode entered.")
            safeMode.SafeMode()
        case _:
            print("Invalid input, please try from the follwing:\n \
            Sleep Mode \
            Stop Mode \
            Dig Mode \
            Safe Mode")
            receiveInput()
            
