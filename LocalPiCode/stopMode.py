
import commonFunctions
import sleepMode

def StopMode(timer): # "timer" might be a parameter we want to pull in from a clock somewhere else in the code, e.g. digMode or some other place where stopMode gets called, hence its place as a parameter
    # Init variables for later use
    timerEnd = 15 # 15 minutes

    # Stop drum
    commonFunctions.stopDrum()

    # Checking elapsed dig time
    if timer >= timerEnd: # Greater-than-or-equal to to cover cases greater than 15 minutes
        print("15-minute dig cycle has been completed. Retracting all systems.") # Alert GS that cycle is completed
        sleepMode.SleepMode()
    else:
        commonFunctions.receiveInput()
