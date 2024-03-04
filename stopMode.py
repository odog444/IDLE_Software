# Author: Mackenzie Davis
# Last Edited: 11/8/2023

stop_mode = 1
timer = 12          # this timer will be more sophisticated later- just wanted to test the pseudocode
timer_end = 15

# sensor data and outputs here


while stop_mode == 1:
 print(" Stop mode activated ")

 #check digging timer

 # if 15 minute dig cycle complete
 if timer == timer_end:
  print("15-minute dig cycle has been completed. Retracting all systems.")
  stop_mode = 0
  
 # if dig cycle not complete
 else: 
  time = timer_end - timer
  print("Digging cycle has not been completed. Time remaining:",time,"minutes.")
  print("Enter 'dig' to continue or 'sleep' to end cycle and retract all systems.")
  keyword = input()
  

  if keyword == "dig":
   stop_mode = 0
   print("Returning to Dig Mode") # for testing purposes
   # enter dig mode
  elif keyword == "sleep":
   stop_mode = 0
   print("Entering Sleep Mode. Retracting all systems.") # for testing purposes
   # enter sleep mode
 



  

