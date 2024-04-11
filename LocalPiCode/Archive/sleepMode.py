import commonFunctions
import time


def SleepMode():
    if(commonFunctions.systemCheck()):
        Sleep()
    else:
        commonFunctions.enterSafeMode()
        
        return



def Sleep():
    
    # check whether drum is spinning
    motorThrottle = UDPClient.recvfrom(buffer)[0].decode('utf-8')
    motorThrottle = int(motorThrottle)
    if(motorThrottle != 0): #If motorThrottle is not 0, the motor is running and must be stopped
        # turn off drum
        commonFunctions.stopDrum()

    # raise drum
    commonFunctions.raiseDrum()

    # Power off any components? If so, how?

    print("IDLE will await further commands")
    
    return
    

#print("Sleep Mode Entered")
