import commonFunctions
import sleepMode
import digMode
import stopMode
import safeMode


# Init file on Raspberry Pi will jump into the main function after it has been run, which should have established wifi connection
def receiveInput():
    # Receive input from Gui
    pass # Placeholder

# Main
def main():
    sleepMode.SleepMode()

    while True:
        commonFunctions.enterSafeMode()
        receiveInput()

