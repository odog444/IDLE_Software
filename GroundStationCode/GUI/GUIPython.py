# This will be the code for the live data visualisation and GUI that has all the buttons!
# Using: Tkinter
# Root: the base GUI box/platform thing that everything shows up on
# Frame: basically just sub-roots that can have data visuallisation or other similar things on them
# Wigets: Buttons and stuff like that seen on the frames
import threading
import time
import csv
import socket
from tkinter import *
from tkinter import ttk
from faker import Faker
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from itertools import count
#from tkmacosx import Button
import pandas as pd

# Initializing variables for timer
pause = True 
startNow = time.time()
ElapsedTime = 0
timerup = 900

# initializing variables for motor
v = 0 


class RootGUI:
    def __init__(self):
        self.root = Tk()  # initialising root
        self.root.title("IDLE GUI Bruh")
        self.root.geometry("1440x820")
        self.root.resizable(True,True)
        self.root.config(bg="black")
        #self.root.columnconfigure(0, weight=1)
        #self.root.rowconfigure(0,weight=1)
        #sizegrip = ttk.Sizegrip(self.root)
        #sizegrip.grid(row=1, sticky=SE)

# Building Frame:


class BUTTONS():
    def __init__(self, root, buffer, UDPClient, serverAddress):
        self.root = root
        self.buffer = buffer
        self.UDPClient = UDPClient
        self.serverAddress = serverAddress
        self.commanddig = 'Dig Pressed!'
        self.commanddig = self.commanddig.encode('utf-8')
        self.commandsafe = 'Safe Pressed!'
        self.commandsafe = self.commandsafe.encode('utf-8')
        self.commandstop = 'Stop Pressed!'
        self.commandstop = self.commandstop.encode('utf-8')
        self.commandsleep = 'Sleep Pressed!'
        self.commandsleep = self.commandsleep.encode('utf-8')
        self.frame = LabelFrame(root, text="Mode Commands", padx=25, pady=25, fg = "white", bg="black")
        self.DIG = Button(self.frame, text="DIG", bg="grey", width=15, command=self.digcheck)
        self.SAFE = Button(self.frame, text="SAFE", bg="grey", width=15, command=self.safecheck)
        self.SLEEP = Button(self.frame, text="SLEEP", bg="red", width=15, command=self.sleepcheck)
        self.STOP = Button(self.frame, text="STOP", bg="grey", width=15, command=self.stopcheck)

        # self.OpenButton()
        self.publish2()

    def digcheck(self):
        self.DIG.configure(bg = "red")
        self.SAFE.configure(bg = "grey")
        self.SLEEP.configure(bg = "grey")
        self.STOP.configure(bg = "grey")
        print("Dig Pressed")
        self.UDPClient.sendto(self.commanddig, self.serverAddress)

        global pause
        global startNow
        global ElapsedTime             

        if ElapsedTime >= timerup:  # If 1 cycle is already completed, this will restart Dig Mode
            ElapsedTime = 0

        else:
            pass

        pause = False
        startNow = time.time()
        UpdateElapsedTime()
        RUNNING_TIMER

    def safecheck(self):
        self.DIG.configure(bg = "grey")
        self.SAFE.configure(bg = "red")
        self.SLEEP.configure(bg = "grey")
        self.STOP.configure(bg = "grey")
        print("Safe Pressed")
        command = "Safe Mode"
        self.UDPClient.sendto(self.commandsafe, self.serverAddress)

    def sleepcheck(self):
        self.DIG.configure(bg = "grey")
        self.SAFE.configure(bg = "grey")
        self.SLEEP.configure(bg = "red")
        self.STOP.configure(bg = "grey")
        print("Sleep Pressed")
        command = "Sleep Mode"
        self.UDPClient.sendto(self.commandsleep, self.serverAddress)

    def stopcheck(self):
        self.DIG.configure(bg = "grey")
        self.SAFE.configure(bg = "grey")
        self.SLEEP.configure(bg = "grey")
        self.STOP.configure(bg = "red")
        print("Stop Pressed")
        self.UDPClient.sendto(self.commandstop, self.serverAddress)

        global pause

        pause = True
    
        # Check elapsed time
        if ElapsedTime < timerup:
            UpdateElapsedTime()        
            print("Dig Cycle paused. System is in Stop Mode") 
        elif ElapsedTime >= timerup:
            print("15-minute dig cycle has been completed. Retracting all systems.") 

    def publish2(self):
        self.frame.grid(row=0, column=0)
        self.DIG.grid(column=1, row=1)
        self.SAFE.grid(column=2, row=1)
        self.SLEEP.grid(column=3, row=1)
        self.STOP.grid(column=4, row=1)


class RUNNING_TIMER():  
    
    def __init__(self, root): 
        self.start_time = time.time()
        self.root = root
        self.frame4 = LabelFrame(root, text="Live Time", padx=25, pady=25, fg= "white", bg="black")
        self.time_passed = Label(root, text="", font=("Helvectica", 37), fg= "white", bg="black")
        self.threading = FALSE

    
        self.updatetime()
        self.publish3()
        

    def updatetime(self):
        global pause
        global ElapsedTime
        self.start_time2 = time.time()
        self.current_time = int(self.start_time2 - startNow + ElapsedTime)
        sec = ""
        if self.current_time < timerup:
            min = int(self.current_time/60)
            sec_entire = self.current_time
            minsec = sec_entire/60
            minsecmin = int(minsec)
            sec = int((minsec - minsecmin)*60)
        elif self.current_time == timerup:
            pause = True
            UpdateElapsedTime()
        elif self.current_time > timerup:
            min = int(timerup/60)
            sec = int(0)
            
     

        if pause == False:
            self.time_passed.config(text = "{m:02d} : {s:02d}".format(m=min,s=sec), fg = "white", bg = "black")
            self.time_passed.after(100, self.updatetime)
        elif pause == True:
            min = int(ElapsedTime/60)
            sec_entire = ElapsedTime
            minsec = sec_entire/60
            minsecmin = int(minsec)
            sec = int((minsec - minsecmin)*60)
            self.time_passed.config(text = "{m:02d} : {s:02d}".format(m=min,s=sec), fg = "red", bg = "black")
            self.time_passed.after(100, self.updatetime)
    

    def publish3(self):
        self.frame4.grid(row=1, column=1, sticky=N)
        self.time_passed.grid()

    

class DataProcessing:
    def __init__(self, root, buffer, UDPClient, serverAddress):
        self.start_time = time.time()
        self.root = root
        self.buffer = buffer
        self.UDPClient = UDPClient
        self.serverAddress = serverAddress
        self.fig, self.ax = plt.subplots()
        self.frame5 = LabelFrame(root, text="Live Plot", padx=1, pady=1)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame5)
        # self.rows = []
        # self.figs = []
        # self.current_time = []

        self.threading = True
        pos_count = 0
        msgfCli = 'Client'
        bytes2send = msgfCli.encode('utf-8')
        while True:
            UDPClient.settimeout(5)
            #time.sleep(0.)

            try:
                UDPClient.sendto(bytes2send, serverAddress)
                data, address = UDPClient.recvfrom(buffer)
                line = data.decode('utf-8')
                # print(line)
                # if line == "Temp:":
                #     continue
                # elif line == "Acceleration":
                #     continue
                # else:
                pos_count += 1
                if (pos_count % 2) == 0:
                    acc_values = [float(x) for x in line.split(',')]
                    print(acc_values)
                else:
                    temp_values = [float(x) for x in line.split(',')]
                    print(temp_values)

            except socket.timeout:
                print("Timeout Error")
                break

        # self.t1 = threading.Thread(target=self.live_dat, daemon=True)
        # self.t2 = threading.Thread(target=self.readFile, daemon=True)
        # self.t1.start()
        # self.t2.start()

        self.publish5()

    # def readFile(self):
    #     rows = []
    #     while self.threading:
    #         with open('DATA_FAKE_YIKES2.csv', 'r') as csv_file_test:
    #             data_csv = csv.reader(csv_file_test)
    #             self.timepassed = time.time()
    #             self.current_time = self.timepassed - self.start_time
    #             for line in data_csv:
    #                 # self.ax.
    #                 rows.append(line)
    #                 self.rows = rows[-1]
    #                 self.ax.scatter(self.rows,self.rows)
    #                 self.canvas.draw()
    #                 #print(self.rows)
    #
    #             time.sleep(3)


    def publish5(self):
        self.frame5.grid(row=3, column=0, sticky=NE)
        self.canvas.get_tk_widget().grid()


    # def live_dat(self):
        # self.threading = True
        # pos_count = 0
        # msgfCli = 'Client'
        # bytes2send = msgfCli.encode('utf-8')
        # serverAddress = ('172.20.10.7', 2224)
        # buffer = 2048
        # UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # while True:
        #     UDPClient.settimeout(5)
        #     try:
        #         UDPClient.sendto(bytes2send, serverAddress)
        #         data, address = UDPClient.recvfrom(buffer)
        #         line = data.decode('utf-8')
        #         # print(line)
        #         # if line == "Temp:":
        #         #     continue
        #         # elif line == "Acceleration":
        #         #     continue
        #         # else:
        #         pos_count += 1
        #         if (pos_count % 2) == 0:
        #             acc_values = [float(x) for x in line.split(',')]
        #             print(acc_values)
        #         else:
        #             temp_values = [float(x) for x in line.split(',')]
        #             print(temp_values)
        #     except socket.timeout:
        #         print("Timeout Error")
        #         break


        # self.threading = True
        # acc_axes = ["X", "Y", "Z"]
        # with open('DATA_FAKE_YIKES.csv', 'w') as csv_file:
        #     write_file = csv.DictWriter(csv_file, fieldnames=acc_axes)
        #     write_file.writeheader()
        # while self.threading:
        #     try:
        #         # time_current = time.time()
        #         # self.time_passed = time_current - start_time
        #         fake_data = Faker()
        #         self.DATA_FAKE = [int(fake_data.latitude()), int(fake_data.latitude()), int(fake_data.latitude())]
        #         # self.print_dat = float(self.DATA_FAKE[0])
        #         with open('DATA_FAKE_YIKES2.csv', 'a') as csv_file:
        #             write_file = csv.DictWriter(csv_file, fieldnames=acc_axes)
        #             dat = {
        #                 "X": self.DATA_FAKE[0],
        #                 "Y": self.DATA_FAKE[1],
        #                 "Z": self.DATA_FAKE[2]
        #             }
        #             write_file.writerow(dat)
        #         time.sleep(3)
        #
        #     except:
        #         pass

class SlideMotor():
    def __init__(self, root, buffer, UDPClient, serverAddress):
        self.root = root
        self.buffer = buffer
        self.UDPClient = UDPClient
        self.serverAddress = serverAddress
        self.commandmotorspeed = '---'
        self.commandmotorspeed = self.commandmotorspeed.encode('utf-8')
        self.frame6 = LabelFrame(root, text = "Motor Throttle = 0 ", padx=25, pady=25, fg= "white", bg="black")
        self.frame7 = Label(root, text = "Delay = --- microseconds", padx=15, pady=15, fg= "white", bg="black")
        self.frame8 = Label(root, text = "Motor range = ---", padx=15, pady=15, fg= "white", bg="black")
        self.motor = Scale(self.frame6, from_=-100, to=100, orient=HORIZONTAL, length=600, showvalue=0, tickinterval=10, resolution=1, command=self.motorspeed)
        # CHANGES MADE STARTING HERE:
        # self.motor.bind("<Button-1>", self.sendnone)
        # self.motor.bind("<ButtonRelease-1>", self.sendmotorspeed)


        self.motor.pack()
   
        self.publish6()

    def motorspeed(self,v):
    #def motorspeed(self):
       # global v
        self.frame6.config(text = "Motor Throttle (%) = " + v, fg= "white", bg = "black")
        
        min = 500       #calculating microsecond delay displayed on GUI
        max = 2500      
        
        throttle = float(v)
        delay = int((throttle + 100)*(max - min)/200 + 500)
        #print("Motor delay: " + str(delay))
        delay_converted = int((throttle + 100)*5) # This value (between 0 and 1000) is sent to the Pi

        if delay <= min:
            range = "full reverse"
        elif min < delay < 1490:
            range = "prop. reverse"
        elif 1490 <= delay <= 1510:
            range = "neutral"
        elif 1510 < delay < 2500:
            range = "prop. forward"
        else:
            range = "full forward"

        #self.UDPClient.sendto(delay_converted, self.serverAddress)
        delay_converted = str(delay_converted) 
        #print("Converted delay: " + delay_converted)
        self.delay_converted = delay_converted.encode('utf-8')
        self.UDPClient.sendto(self.delay_converted, self.serverAddress)
        self.frame7.config(text = "Delay = " + str(delay)  + " microseconds", font=("Helvectica", 10), fg= "white", bg = "black")
        self.frame8.config(text = "Motor range = " + range, font=("Helvectica", 10), fg= "white", bg = "black")
    
        
    

    # def sendnone(self,x):
    #     self.commandmotorspeed = 'NONE\n'
    #     self.commandmotorspeed = self.commandmotorspeed.encode('utf-8')
    #     self.UDPClient.sendto(self.commandmotorspeed, self.serverAddress)
    #     print(self.commandmotorspeed)


    # def sendmotorspeed(self,x):
    #      global v
    #      v_str = str(v)   
    #      self.commandmotorspeed = v_str
    #      self.commandmotorspeed = self.commandmotorspeed.encode('utf-8')
    #      self.UDPClient.sendto(self.commandmotorspeed, self.serverAddress)
    #      print(self.commandmotorspeed)
    

    def publish6(self):
        self.frame6.grid(row=2, column=4, sticky=N)
        self.frame7.grid(row=0, column=4, sticky=N)
        self.frame8.grid(row=1, column=4, sticky=N)
        self.motor.grid()


class ButtonsLA():
    def __init__(self, root, buffer, UDPClient, serverAddress):
        self.root = root
        self.buffer = buffer
        self.UDPClient = UDPClient
        self.serverAddress = serverAddress
        self.commandLinearActuator = 'No Command\n'
        self.commandLinearActuator = self.commandLinearActuator.encode('utf-8')
        self.frame9 = LabelFrame(root, text = "Linear Actuator Control", padx=25, pady=25, fg= "white", bg="black")
        #self.upButton = Button(self.frame9, text="UP", repeatdelay = 1, repeatinterval= 1, bg="grey", width=10,height=10, command=self.up)
        #self.downButton = Button(self.frame9, text="DOWN", repeatdelay = 1, repeatinterval= 1, bg="grey", width=10,height=10, command=self.down)
        
        #CHANGES START HERE:
        #self.upButton = Button(self.frame9, text="UP", repeatdelay = 1, repeatinterval= 1, bg="grey", width=10,height=10)# command=self.up)
        self.upButton = Button(self.frame9, text="UP", bg="grey", width=10,height=10)# , command=self.up)
        self.upButton.bind('<Button-1>', self.up)
        self.upButton.bind('<ButtonRelease-1>', self.stop)
        #self.downButton = Button(self.frame9, text="DOWN", repeatdelay = 1, repeatinterval= 1, bg="grey", width=10,height=10)# command=self.down)
        self.downButton = Button(self.frame9, text="DOWN", bg="grey", width=10,height=10)#, command=self.down)
        self.downButton.bind('<Button-1>', self.down)
        self.downButton.bind('<ButtonRelease-1>', self.stop)
        # time.sleep(0.1)

        self.publish7()
        #self.commandLinearActuator = 'No Command\n'
    
    def up(self,x):  
        self.commandLinearActuator = 'UP\n'
        print(self.commandLinearActuator)
        self.commandLinearActuator = self.commandLinearActuator.encode('utf-8')
        self.UDPClient.sendto(self.commandLinearActuator, self.serverAddress)
        #self.upButton.after(1000,self.up(x))
            
        
    def down(self,x):
        self.commandLinearActuator = 'DOWN\n'
        print(self.commandLinearActuator)
        self.commandLinearActuator = self.commandLinearActuator.encode('utf-8')
        self.UDPClient.sendto(self.commandLinearActuator, self.serverAddress)
        #self.downButton.after(1000,self.down(x))

    # AND HERE:
    def stop(self,x):
        self.commandLinearActuator = 'NONE\n'
        print(self.commandLinearActuator)
        self.commandLinearActuator = self.commandLinearActuator.encode('utf-8')
        self.UDPClient.sendto(self.commandLinearActuator, self.serverAddress)


    def publish7(self):
        self.frame9.grid(row=3, column=3, sticky=N)
        self.upButton.grid(row=4, column=3, sticky=N)
        self.downButton.grid(row=4, column=4, sticky=N)


def UpdateElapsedTime():
    global ElapsedTime
    ElapsedTime = int(time.time() - startNow + ElapsedTime)
    



if __name__ == "__main__":
    RootGUI()
    BUTTONS()
    RUNNING_TIMER()
    SlideMotor()
    ButtonsLA()