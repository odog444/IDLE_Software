# This code will function as the pseudocode for the safe mode

# Waiting for sensors to detect the retraction of all digging subsystems
# Call sensor reading function
sensor_retract = 1 # Insert needed function for sensor reading
while sensor_retract == 1:
    sensor_retract = 0 # sensor_retract_func(I2C protocal)

# Check for subsystem retraction
diggingsub = 1 # again using the sensors to detect whether these subsystems are retracted
anchoringsub = 1
def retractanchor():
    print("This function will serve to retract the anchoring subsystem")
def retractdigger():
    print("This function will serve to retract the digging subsystem")
if diggingsub == 1 & anchoringsub == 1:
    retractanchor()
    retractdigger()
else:
    #continue
    print("All subsystems have been retracted!")

def communicate():
    print("This function will serve to communicate with the Ground System")

communicate()
    