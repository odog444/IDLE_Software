import commonFunctions

def SafeMode(diggerMotorOn):
    
     # check whether drum is spinning
    if(diggerMotorOn == True):

        # turn off drum
        commonFunctions.stopDrum()


    print("Safe Mode entered. System recovery required")



    return


    