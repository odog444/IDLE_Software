import socket
import csv
import keyboard
from multiprocessing import Process
import time
import numpy as np
from faker import Faker

def data_loop():
    acc_axes = ["X", "Y", "Z"]
    timer_col = ["time"]
    start_time = time.time()

    with open('DATA_FAKE_YIKES.csv', 'w') as csv_file:
        write_file = csv.DictWriter(csv_file, fieldnames=acc_axes)
        write_file.writeheader()

    with open('TIMER.csv', 'w') as csv_file2:
        write_file2 = csv.DictWriter(csv_file2, fieldnames=timer_col)
        write_file2.writeheader()
    while True:
        time_current = time.time()
        TIMER = time_current-start_time

        fake_data = Faker()
        DATA_FAKE = [int(fake_data.latitude()), int(fake_data.latitude()), int(fake_data.latitude())]
        # print(DATA_FAKE)
        with open('DATA_FAKE_YIKES.csv', 'a') as csv_file:
            write_file = csv.DictWriter(csv_file, fieldnames=acc_axes)
            dat = {
                "X": DATA_FAKE[0],
                "Y": DATA_FAKE[1],
                "Z": DATA_FAKE[2]
            }
            write_file.writerow(dat)
            print(dat)

        with open('TIMER.csv', 'a') as csv_file2:
            write_file2 = csv.DictWriter(csv_file2, fieldnames=timer_col)
            dat2 = {
                "time": TIMER
            }
            write_file2.writerow(dat2)






def data_loop(serverAddress, buffer, UDPClient, command):
    acc_axes = ["X", "Y", "Z"]
    with open('data.csv', 'w') as csv_file:
        write_file = csv.DictWriter(csv_file, fieldnames=acc_axes)
        write_file.writeheader()
    while True:
        data, address = UDPClient.recvfrom(buffer)
        data = data.decode('utf-8')
        data = list(map(float, data.split(',')))
        # print(data)
        with open('data.csv', 'a') as csv_file:
            write_file = csv.DictWriter(csv_file, fieldnames=acc_axes)
            dat = {
                "X": data[0],
                "Y": data[1],
                "Z": data[2]
            }
            write_file.writerow(dat)
            print(dat)

if __name__ == '__main__':
    # client/server setup:
    serverAddress = ('172.20.10.7', 2222)
    buffer = 1024
    UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    command = input('Enter Start to Load Data: ')
    command = command.encode('utf-8')
    UDPClient.sendto(command, serverAddress)
    pro = Process(target=data_loop(serverAddress, buffer, UDPClient, command))

    data_loop()






























