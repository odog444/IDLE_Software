# Main code which will call all of the sub-scripts
import socket
import threading
from GUIPython import RootGUI, BUTTONS, RUNNING_TIMER, DataProcessing, SlideMotor, SlideLA

serverAddress = ('172.20.10.7', 2222)
buffer = 1024
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

RootMaster = RootGUI()
Button_Maker = BUTTONS(RootMaster.root, buffer, UDPClient, serverAddress)
Time_Data = RUNNING_TIMER(RootMaster.root)
Data_Process = DataProcessing(RootMaster.root)
Slide_Motor = SlideMotor(RootMaster.root)
Slide_LA = SlideLA(RootMaster.root)

RootMaster.root.mainloop()