from MODES import DIGCLASS, SAFECLASS, STOPCLASS, SLEEPCLASS, COMMONFUNCS, MODERECEPTION, SENSORDATA
import socket

serverAddress = ('172.20.10.7', 2244)
buffer = 2048
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ModeReception = MODERECEPTION(serverAddress, buffer, UDPClient)
SensorData = SENSORDATA(serverAddress, buffer, UDPClient)
commonFunc = COMMONFUNCS(serverAddress, buffer, UDPClient)
DIGMaster = DIGCLASS(serverAddress, buffer, UDPClient)
SAFEMaster = SAFECLASS(serverAddress, buffer, UDPClient)
STOPMaster = STOPCLASS(serverAddress, buffer, UDPClient)
SLEEPMaster = SLEEPCLASS(serverAddress, buffer, UDPClient)
