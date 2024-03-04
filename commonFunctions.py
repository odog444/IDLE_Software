# Use this if you're using a function/chunk of code multiple times throughout your file, 
# or if you think you would find the chunk of code/function useful in other functions
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
    # Receive input from Gui
    pass # Placeholder