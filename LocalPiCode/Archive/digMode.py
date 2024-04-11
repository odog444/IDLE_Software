import commonFunctions
import time
import sleepMode


class DIGCLASS:
    def __init__(self):
        self.ElapsedTime = 0  # Placeholder
        self.timerEnd = 15  # 15 minutes/900 seconds


    def DigMode(self):
        # initial health check
        if(commonFunctions.systemCheck()):
            dig()
        else:
            commonFunctions.enterSafeMode()

        return

    def dig(self):

        # input = UDPClient.recvfrom(buffer)[0].decode('utf-8')

        # if (input.startswith("Motor Throttle:")):
        #     delay_converted = input
        # elif(input.startswith("Elapsed Time:")):

        # Only need this if we are checking the time
        # ElapsedTime = UDPClient.recvfrom(buffer)[0].decode('utf-8') # Placeholder
        # ElapsedTime = int(ElapsedTime)


        # continuously check sensors and dig timer
        #while self.ElapsedTime <= self.timerEnd:

        delay_converted = UDPClient.recvfrom(buffer)[0].decode('utf-8')
        commonFunctions.moveDrum(int(delay_converted))

        # Add Linear Actuator comms
        actuatorDirection = UDPClient.recvfrom(buffer)[0].decode('utf-8')
        commonFunctions.moveLinearActuator(actuatorDirection)

        while True:




            if(not commonFunctions.systemCheck()):
                commonFunctions.enterSafeMode()



       # print("Dig cycle complete. Entering sleep mode")

       #sleepMode.SleepMode()


        return
