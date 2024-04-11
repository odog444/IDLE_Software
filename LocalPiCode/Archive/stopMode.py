
import commonFunctions
import sleepMode

#ElapsedTime = 0 # Placeholder
timerEnd = 900 # 15 minutes/900 seconds

def StopMode(): 

    # Stop drum
    commonFunctions.stopDrum()

    # Checking elapsed dig time
    ElapsedTime = UDPClient.recvfrom(buffer)[0].decode('utf-8')
    ElapsedTime = int(ElapsedTime)
    # Check elapsed time
    if ElapsedTime < timerEnd:      
        # Should this be sent to GS?
        print("Dig Cycle paused. System is in Stop Mode") 
    elif ElapsedTime >= timerEnd:
        print("15-minute dig cycle has been completed. Retracting all systems.") 
        #sleepMode.SleepMode()





