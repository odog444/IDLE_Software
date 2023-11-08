# This code is a pseudocode for the eventual sleep mode script that will be used in our senior project lunar digger
# Author: Nicholas Boggess
# Last Edited: 11/6/2023

# Waiting for dig command:
sleep_mode = 1
while sleep_mode == 1:
    print("Enter 'dig' to continue...")
    keyword = input()
    if keyword == "dig":
        sleep_mode = 0
    else:
        sleep_mode = 1

# Waiting for all systems to retract:
# Will need to use the sensor data to make this work once pseudocode is done

systems_delpoyed = 1  # this will be fed the sensor data and will turn to 0 once everything is retracted
while systems_delpoyed == 1:
    print("Enter 'sleep' to sleep...") # for testing purposes
    sd = input()  # for testing purposes
    if sd == 1:
        sleep_mode = 0
    elif sd == "sleep":
        sleep_mode = 1
        systems_delpoyed = 0
        print("Sleep mode has been initiated!")



