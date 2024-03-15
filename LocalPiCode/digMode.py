import commonFunctions
import sleepMode

timer = 0   # Placeholder
timerEnd = 15  # Placeholder

def DigMode():
    # initial health check
    if(commonFunctions.systemCheck()): 
        dig()
    else:
        commonFunctions.enterSafeMode()

    return

def dig():
    
    # power on drum
    commonFunctions.startDrum()

    # lower drum
    commonFunctions.lowerDrum()

    # start timer 

    # continuously check sensors and dig timer
    while timer <= timerEnd:
        if(not commonFunctions.systemCheck()):
            commonFunctions.enterSafeMode()

        
    
    print("Dig cycle complete. Entering sleep mode")

    sleepMode.SleepMode()


    return

