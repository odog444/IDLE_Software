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
    diggerMotorOn = UDPClient.recvfrom(buffer)[0].decode('utf-8')
    diggerMotorOn = int(diggerMotorOn)
    if(diggerMotorOn != 0):
        # turn off drum
        commonFunctions.stopDrum()

    # raise drum
    commonFunctions.raiseDrum()

    print("IDLE will await further commands")
    
    return
    

print("Sleep Mode Entered")
