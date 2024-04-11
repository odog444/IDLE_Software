'''
NOTES ON PIN USAGE
Sensors:
    Current/Motor
    Temperature
    Tilt

Linear Actuator:
    Arduino:
        PWM: pin 9
        pin1: 8
        Pin2: 7
        Pin3: 6
        Read in: 5 from Pi pin 32

    Pi:
        PWM: pin 32

Drum motor:
    Arduino:
        Output drum: pin 3
        PWM input: 10
    
    Pi:
        PWM GPIO 13: pin 33
'''

LinPWMPin = 32
DrumPWMPin = 33