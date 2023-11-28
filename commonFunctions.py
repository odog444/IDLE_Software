# Use this if you're using a function/chunk of code multiple times throughout your file, 
# or if you think you would find the chunk of code/function useful in other functions

def systemCheck(): # Check if all sensors have nominal readings and 
    if(not checkSensors()):
        return False
    
    return True # If none of the if statements run, everything is in working order

def enterSafeMode():
    # Maybe needs to run some other stuff, but other than that, it just runs safeMode()
    safeMode()
    return

def checkSensors():
    # Check tilt is in correct range
    # Check motor current draws are reasonable and position readings are nominal
    # Check if within temperature bounds
    return