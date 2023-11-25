# Bryce
import commonFunctions

def digMode():
    if(systemCheck()): 
        dig()
    else:
        enterSafeMode()

    return

def dig():
    diggerMotor.isOn = True
    while(weightCollected <= 0.5):
        if(not systemCheck()): # Continuously check if system is running nominally while digging
            enterSafeMode()
    diggerMotor.isOn = False