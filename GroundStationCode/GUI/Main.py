# Main code which will call all of the sub-scripts
import threading

from GUIPython import RootGUI, BUTTONS, RUNNING_TIMER, DataProcessing, SlideMotor, SlideLA
# from Data_Load import SerialCtrl

RootMaster = RootGUI()
Button_Maker = BUTTONS(RootMaster.root)
Time_Data = RUNNING_TIMER(RootMaster.root)
Data_Process = DataProcessing(RootMaster.root)
Slide_Motor = SlideMotor(RootMaster.root)
Slide_LA = SlideLA(RootMaster.root)

RootMaster.root.mainloop()
