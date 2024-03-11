import socket
import csv
from datetime import datetime
import scipy.interpolate as si
from scipy.interpolate import interp1d
from scipy.signal import lfilter, savgol_filter
from scipy import signal
import time
import numpy as np
from faker import Faker

# class DataMaster():
#     def __init__(self):
#         # The plan here is to initialize the data which will then be used to manage the imported data across all of the code
#