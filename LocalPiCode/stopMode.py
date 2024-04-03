
import commonFunctions
import sleepMode

ElapsedTime = 0 # Placeholder
timerEnd = 15 # 15 minutes/900 seconds

def StopMode(): 

    # Stop drum
    commonFunctions.stopDrum()

    # Checking elapsed dig time
    # Check elapsed time
    if ElapsedTime < timerEnd:      
        print("Dig Cycle paused. System is in Stop Mode") 
    elif ElapsedTime >= timerEnd:
        print("15-minute dig cycle has been completed. Retracting all systems.") 
        sleepMode.SleepMode()
    


