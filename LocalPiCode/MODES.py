import time
import sys
import socket
import csv
import keyboard
from multiprocessing import Process
import time
import serial
import serial.tools.list_ports
import threading
import numpy as np
from faker import Faker
# import RPi.GPIO as GPIO

print('Server is working and listening...')

#Initialize
try:
    ser = serial.Serial('/dev/ttyACM0',115200, timeout = 1.0) # MUST HAVE SAME BAUD RATE AS IN ARDUINO CODE!!!
except:
    print("Could not connect to ttyACM0, trying ttyACM1...")
    try:
        ser = serial.Serial('/dev/ttyACM1',115200, timeout = 1.0)
    except:
        print("Cannot connect to serial, closing program...")
        exit()


    
ser.setDTR(False)
time.sleep(1)
ser.flushInput()
ser.setDTR(True)
ser.reset_input_buffer()

# global command

timerEnd = 900     # 900s/15min


class DIGCLASS:
    def __init__(self,serverAddress, buffer, UDPClient):
        self.addy = serverAddress
        self.buff = buffer
        self.UDPCli = UDPClient

    def DigMode(self):
        # initial health check
        if (COMMONFUNCS.systemCheck(self)):
            self.dig()
        else:
            COMMONFUNCS.enterSafeMode(self)

        return

    def dig(self):

        # GUI sends motor control and linear actuator commands already...do those need to be implemented here?

        # Pulling Elapsed time from GUI (sent in GUI code when Start Timer button is pressed)
        self.ElapsedTime = UDPClient.recvfrom(buffer)[0].decode('utf-8')
        self.ElapsedTime = int(self.ElapsedTime)
        self.startNow = time.time()
        self.timer = 0 #starting at 0 seconds

        # continuously check sensors and dig timer
        # Time will count from 0 to remaining time calculated by (15 minutes (900 seconds) - Elapsed Time)
        while self.timer < (timerEnd-self.ElapsedTime):
            
            if (not COMMONFUNCS.systemCheck()):
                COMMONFUNCS.enterSafeMode(self)
        
            self.timer = int(time.time() - self.startNow)
        
            
        # Send this to GS?
        print("Dig cycle complete. Entering sleep mode")

        # Autonomously enters sleep mode when digging ends 
        SLEEPCLASS.SleepMode(self)

        return

class SAFECLASS:
    def __init__(self,serverAddress, buffer, UDPClient):
        self.addy = serverAddress
        self.buff = buffer
        self.UDPCli = UDPClient
        self.SafeMode()

    def SafeMode(self):

        # Safe can be commanded or autonomously entered...?


        # turn off drum
        COMMONFUNCS.stopDrum(self)

        # Alert GS that system has entered safe mode and request system recovery 



class SLEEPCLASS:
    def __init__(self,serverAddress, buffer, UDPClient):
        self.addy = serverAddress
        self.buff = buffer
        self.UDPCli = UDPClient
        self.SleepMode()

    def SleepMode(self):
        if not False:  # if (COMMONFUNCS.systemCheck(self)):
            self.sleep()
        # else:
        #     COMMONFUNCS.enterSafeMode(self)
        #     return

    def sleep(self):

        # turn off drum
        COMMONFUNCS.stopDrum(self)

        # raise drum
        COMMONFUNCS.raiseDrum(self)

        # Change this later to send message to GS 
        print("System is in Sleep Mode. IDLE will await further commands")

        return



class STOPCLASS:
    def __init__(self,serverAddress, buffer, UDPClient):
         # Receiving elapsed dig time (sent in GUI code when Stop is pressed)
         self.addy = serverAddress
         self.buff = buffer
         self.UDPCli = UDPClient
         #self.ElapsedTime = UDPClient.recvfrom(buffer)[0].decode('utf-8')
         #self.ElapsedTime = int(self.ElapsedTime)

         self.StopMode()

    def StopMode(self):

        # Stop drum
        COMMONFUNCS.stopDrum(self)
        # Send command to Arduino?
    
        # Check elapsed time
        # if self.ElapsedTime < timerEnd:
        #     # Should this message be sent to the GS?
        #     print("Dig Cycle paused. System is in Stop Mode")
        # elif self.ElapsedTime >= timerEnd:
        #     # Should this message be sent to the GS?
        #     print("15-minute dig cycle has been completed. Retracting all systems.")
        #     SLEEPCLASS.SleepMode()


class COMMONFUNCS:
    def __init__(self,serverAddress, buffer, UDPClient):
        self.ServerIP, self.ServerPort = serverAddress
        #self.addy = serverAddress
        self.buff = buffer
        self.UDPCli = UDPClient
        self.line = '1'
        ser.setDTR(False)
        time.sleep(1)
        ser.flushInput()
        ser.setDTR(True)
        ser.reset._input_buffer()
        print("Serial is working!")


    def systemCheck(self):  # Check if all sensors have nominal readings and
        if (not self.checkSensors()):
            return False

        return True  # If none of the if statements run, everything is in working order

    def enterSafeMode(self):
        # Maybe needs to run some other stuff, but other than that, it just runs safeMode()
        SAFECLASS.SafeMode(self)
        return

    def checkSensors(self):
        # Check tilt is in correct range
        # Check motor current draws are reasonable and position readings are nominal
        # Check if within temperature bounds

        # If any of the readings are abnormal, return as false. Otherwise, return as true.
        return True

    def stopDrum(self):
        for i in range (10):  
            command = str(500) + '\n'
            time.sleep(0.05)
        # Send command to Arduino, where 500 gets converted to a 1500 usecond delay in the Arduino code 
    

    def raiseDrum(self):
        command = ('UP\n')
        time.sleep(5)
        command = ('NONE\n')
        # Send command to Arduino?


    def receiveInput(self):
        modeToEnter = self.UDPCli.recvfrom(self.buff)[0].decode('utf-8')  
        # recvfrom() returns 2 items, so [0] is to signify to only record 1st item. Hopefully should not cause bugs

        if modeToEnter == "Sleep Mode":
            # Note: Remember to change print statements to send over to GS as statements to be printed on a console
                print("Sleep Mode entered.")
                SLEEPCLASS.SleepMode()
        elif modeToEnter ==  "Stop Mode":
                print("Stop Mode entered.")
                STOPCLASS.StopMode()
        elif modeToEnter == "Dig Mode":
                print("Dig Mode entered.")
                DIGCLASS.DigMode()
        elif modeToEnter == "Safe Mode":
                print("Safe Mode entered.")
                SAFECLASS.SafeMode()
        else:
                print("Invalid input, please try from the follwing:\n \
                Sleep Mode\n \
                Stop Mode\n \
                Dig Mode\n \
                Safe Mode")
                self.receiveInput()




class MODERECEPTION:
    def __init__(self,serverAddress, buffer, UDPClient):
        self.ServerIP, self.ServerPort = serverAddress
        self.buff = buffer
        self.UDPCli = UDPClient
        self.ser = ser
        
        self.ser.setDTR(False)
        time.sleep(1)
        self.ser.flushInput()
        self.ser.setDTR(True)

        self.receiveComm = threading.Thread(target=self.cliSer, daemon=True)
        self.sendComm = threading.Thread(target=self.senDat, daemon=True)

        self.receiveComm.start()
        self.sendComm.start()
    
    
    def cliSer(self):
        print("Communicating with GS ")
        while True:
            command = self.UDPCli.recvfrom(self.buff) # waiting unit Pi connects with client (laptop)
            command = command.decode('utf-8') + '\n'
            try:
                self.ser.write(command.encode('utf-8'))
            except Exception as error:
                print(f"Serial write failed with exception {error}")
            #print(command)
            time.sleep(0.01)
    

    # Inserting ModeReception.py for consolidation:
        
    def senDat(self):
        print("Serial is working!")

        while True:
            # Receiving data
            if self.ser.in_waiting > 0: # returns the number of bytes recieved
                if(self.ser.in_waiting > buffer):
                    print("BUFFER OVERFLOW, resetting...")
                    self.ser.reset_input_buffer()
                line = self.ser.readline().decode('utf-8').rstrip()
                print(f"From serial: {line}")
            time.sleep(0.1)


class SENSORDATA:
    def __init__(self,serverAddress, buffer, UDPClient):
        self.ServerIP, self.ServerPort = serverAddress
        self.buff = buffer
        self.UDPCli = UDPClient
        self.line = '1'
        self.ser = ser

        self.sensors = threading.Thread(target=self.sensorData, daemon=True)
        self.sensors.start()



    def sensorData(self):
        self.ser.reset._input_buffer()
        print("Serial is working!")

        self.bytesSending = self.line.encode('utf-8')
        print('Server is up and listening...')
        self.message, self.address = self.UDPCli.recvfrom(self.buff) # waiting until Pi connects with client
        self.message = self.message.decode('utf-8')

        while not False:
            # Receiving data
            if self.ser.in_waiting > 0: # returns the number of bytes received
                time.sleep(0.3)
                if(self.ser.in_waiting > self.buff):
                    print('BUFFER OVERFLOW')
                    self.ser.reset_input_buffer()
                else: 
                    self.line = self.ser.readline().decode('utf-8').rstrip()
                    print(self.line)
                    self.bytesSending = self.line.encode('utf-8')
                    self.UDPCli.sendto(self.bytesSending,self.address)


if __name__ == "__main__":
    MODERECEPTION()
    SENSORDATA()
    DIGCLASS()
    SAFECLASS()
    SLEEPCLASS()
    STOPCLASS()
    COMMONFUNCS()




