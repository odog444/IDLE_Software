import commonFunctions
import time


def SleepMode():
    if(systemCheck()):
        Sleep()
    else:
        enterSafeMode()
        
        return



def Sleep(diggerMotorOn):
    
    if(diggerMotorOn == True):
        # Pi tells Arduino to turn off drum motor
        diggerMotorOn = False
    
    RaiseDrum()
    
    return
    
    
def RaiseDrum():
    
    i = 0 # number of attempts
    j = 0 # number of centimeters
    
    #Arduino runs Raise Drum Function outlined in Sleep Mode flowchart
 
    #Pi receives either "successful" or "unsuccessful" from Arduino
    #if __name__ == '__main__':
    #ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    #ser.reset_input_buffer()
    #while True:
    #    if ser.in_waiting > 0:
    #        line = ser.readline().decode('utf-8').rstrip()
    #    
    #        if(line == "Successful"):
    #            print('\n Drum was raised successfully. IDLE will await further commands \n')
                
    #        else:
    #            print('\n Error: Drum was unable to raise successfully. Entering Safe Mode. \n')
    #            enterSafeMode()
 
    return