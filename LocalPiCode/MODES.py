import time
import sleepMode
import sys
import socket
import csv
import keyboard
from multiprocessing import Process
import time
import numpy as np
from faker import Faker
import RPi.GPIO as GPIO


class DIGCLASS:
    def __init__(self):
        self.ElapsedTime = 0  # Placeholder
        self.timerEnd = 15  # 15 minutes/900 seconds

    def DigMode(self):
        # initial health check
        if (commonFunctions.systemCheck()):
            dig()
        else:
            commonFunctions.enterSafeMode()

        return

    def dig(self):

        # # power on drum
        # commonFunctions.startDrum()

        # # lower drum
        # commonFunctions.lowerDrum()

        # start timer

        # continuously check sensors and dig timer
        while self.ElapsedTime <= self.timerEnd:
            delay_converted = UDPClient.recvfrom(buffer)[0].decode('utf-8')
            commonFunctions.moveDrum(int(delay_converted))

            # Add Linear Actuator comms
            actuatorDirection = UDPClient.recvfrom(buffer)[0].decode('utf-8')
            commonFunctions.moveLinearActuator(actuatorDirection)

            if (not commonFunctions.systemCheck()):
                commonFunctions.enterSafeMode()

        print("Dig cycle complete. Entering sleep mode")

        sleepMode.SleepMode()

        return

class SAFECLASS:
    def __init__(self):
        pass
    def SafeMode(diggerMotorOn):
        # check whether drum is spinning
        if (diggerMotorOn == True):
            # turn off drum
            commonFunctions.stopDrum()

        print("Safe Mode entered. System recovery required")

class SLEEPCLASS:
    def __init__(self):
        pass

    def SleepMode(self):
        if (commonFunctions.systemCheck()):
            Sleep()
        else:
            commonFunctions.enterSafeMode()

            return

    def Sleep(self):

        # check whether drum is spinning
        diggerMotorOn = UDPClient.recvfrom(buffer)[0].decode('utf-8')
        diggerMotorOn = int(diggerMotorOn)
        if (diggerMotorOn != 0):
            # turn off drum
            commonFunctions.stopDrum()

        # raise drum
        commonFunctions.raiseDrum()

        print("IDLE will await further commands")

        return

    print("Sleep Mode Entered")


class STOPCLASS:
    def __init__(self):
        self.timerEnd = 900 # 15 minutes/900 seconds

    # Stop drum
    def StopMode(self):

        # Stop drum
        commonFunctions.stopDrum()

        # Checking elapsed dig time
        ElapsedTime = UDPClient.recvfrom(buffer)[0].decode('utf-8')
        ElapsedTime = int(ElapsedTime)
        # Check elapsed time
        if ElapsedTime < timerEnd:
            print("Dig Cycle paused. System is in Stop Mode")
        elif ElapsedTime >= timerEnd:
            print("15-minute dig cycle has been completed. Retracting all systems.")
            sleepMode.SleepMode()

class COMMONFUNCS:
    def __init__(self):
        pass

    def systemCheck(self):  # Check if all sensors have nominal readings and
        if (not checkSensors()):
            return False

        return True  # If none of the if statements run, everything is in working order

    def enterSafeMode(self):
        # Maybe needs to run some other stuff, but other than that, it just runs safeMode()
        safeMode.SafeMode()
        return

    def checkSensors(self):
        # Check tilt is in correct range
        # Check motor current draws are reasonable and position readings are nominal
        # Check if within temperature bounds

        # If any of the readings are abnormal, return as false. Otherwise, return as true.
        return True

    def stopDrum(self):  # Is this code right??
        # pi_pwm = GPIO.PWM(33,1000)
        # pi_pwm.start(0)
        # pi_pwm.ChangeDutyCycle(50)
        pass
        # use Pi code

    # def startDrum():
    #     print("Drum Started") # Placeholder for starting drum spin

    # def lowerDrum():
    #     print("Drum Lowered") # Placeholder for lowering drum

    def raiseDrum(self):
        # use Pi code

        # print("Drum Raised") # Placeholder for raising drum
        pass

    def moveDrum(self, delay_converted):
        # Send out of 5v GPIO
        pi_pwm = GPIO.PWM(33, 1000)
        pi_pwm.start(0)
        pi_pwm.ChangeDutyCycle(delay_converted / 10)

        # Use Pi code
        pass

    def moveLinearActuator(self, actuatorDirection):
        # Insert Pi code

        pass

    def receiveInput(self):
        modeToEnter = UDPClient.recvfrom(buffer)[0].decode(
            'utf-8')  # recvfrom() returns 2 items, so [0] is to signify to only record 1st item. Hopefully should not cause bugs

        match modeToEnter:  # Note: Remember to change print statements to send over to GS as statements to be printed on a console
            case "Sleep Mode":
                print("Sleep Mode entered.")
                sleepMode.SleepMode()
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
                Sleep Mode\n \
                Stop Mode\n \
                Dig Mode\n \
                Safe Mode")
                receiveInput()



if __name__ == "__main__":
    DIGCLASS()
    SAFECLASS()
    SLEEPCLASS()
    STOPCLASS()
    COMMONFUNCS()



