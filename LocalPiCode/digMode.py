import commonFunctions
import time
import sleepMode


ElapsedTime = 0 # Placeholder
timerEnd = 15  # 15 minutes/900 seconds



def DigMode():
    # initial health check
    if(commonFunctions.systemCheck()): 
        dig()
    else:
        commonFunctions.enterSafeMode()

    return

def dig():

    # # power on drum
    # commonFunctions.startDrum()

    # # lower drum
    # commonFunctions.lowerDrum()

    # start timer 

    # continuously check sensors and dig timer
    while ElapsedTime <= timerEnd:
        delay_converted = UDPClient.recvfrom(buffer)[0].decode('utf-8')
        commonFunctions.moveDrum(int(delay_converted))

        # Add Linear Actuator comms


        
        if(not commonFunctions.systemCheck()):
            commonFunctions.enterSafeMode()

        
    
    print("Dig cycle complete. Entering sleep mode")

    sleepMode.SleepMode()


    return
