import commonFunctions
import time


def SleepMode():
    if(commonFunctions.systemCheck()):
        Sleep()
    else:
        commonFunctions.enterSafeMode()
        
        return



def Sleep():
    

    diggerMotorOn = True # Placeholder
    # check whether drum is spinning
    if(diggerMotorOn == True):

        # turn off drum
        commonFunctions.stopDrum()

    # raise drum
    commonFunctions.raiseDrum()

    print("IDLE will await further commands")
    
    return
    

print("Sleep Mode Entered")
