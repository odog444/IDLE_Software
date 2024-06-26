# converts throttle setting from -1 to 1 to the associated motor signal pulse range 
# right now it just outputs the microsecond delay and pulse range based on the throttle from -1 to 1


throttle = float(input("Input a number from -1 to 1: "))

# full reverse p <= 500 (throttle <= -1)
# prop reverse 500 < p < 1490 (-1 < throttle < -0.01
# neutral 1490 <= p <= 1510 (-0.01 <= throttle <= 0.01)
# prop forward 1510 < p < 2500 (0.01 < throttle < 1)
# full forward p <= 2500 (throttle >= 1)

min = 500
max = 2500

delay = (throttle + 1)*(max - min)/2 + 500


if delay < 0:
    print("Throttle is outside of range, corresponding microsecond delay is < 0")
    range = False

elif delay <= min:
    print("range = full reverse")
    range = True

elif min < delay < 1490:
    print("range = prop. reverse")
    range = True

elif 1490 <= delay <= 1510:
    print("range = neutral")
    range = True

elif 1510 < delay < 2500:
    print("range = prop. forward")
    range = True

else:
    print("range = full forward")
    range = True

if range == True:
    print("delay is %.2f microseconds" %delay)

