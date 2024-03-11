# This will be the code for the live data visualisation and GUI that has all the buttons!
# Using: Tkinter
# Root: the base GUI box/platform thing that everything shows up on
# Frame: basically just sub-roots that can have data visuallisation or other similar things on them
# Wigets: Buttons and stuff like that seen on the frames
import threading
import time
import csv
from tkinter import *
from tkinter import ttk
from faker import Faker
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from itertools import count
import pandas as pd

class RootGUI:
    def __init__(self):
        self.root = Tk()  # initialising root
        self.root.title("IDLE GUI Bruh")
        self.root.geometry("1440x820")
        self.root.resizable(True,True)
        self.root.config(bg="black")
        # self.root.columnconfigure(0, weight=1)
        # self.root.rowconfigure(0,weight=1)
        # sizegrip = ttk.Sizegrip(self.root)
        # sizegrip.grid(row=1, sticky=SE)

# Building Frame:

class BUTTONS():
    def __init__(self, root):
        self.root = root
        self.frame = LabelFrame(root, text="Mode Commands", padx=25, pady=25, bg="black")
        self.DIG = Button(self.frame, text="DIG", bg="grey", width=15, command=self.digcheck)
        self.SAFE = Button(self.frame, text="SAFE", bg="grey", width=15, command=self.safecheck)
        self.SLEEP = Button(self.frame, text="SLEEP", bg="grey", width=15, command=self.sleepcheck)
        self.STOP = Button(self.frame, text="STOP", bg="red", width=15, command=self.stopcheck)

        # self.OpenButton()
        self.publish2()

    def digcheck(self):
        print("Dig Pressed")

    def safecheck(self):
        print("Safe Pressed")

    def sleepcheck(self):
        print("Sleep Pressed")

    def stopcheck(self):
        print("Stop Pressed")


    def publish2(self):
        self.frame.grid(row=0, column=0)
        self.DIG.grid(column=1, row=1)
        self.SAFE.grid(column=2, row=1)
        self.SLEEP.grid(column=3, row=1)
        self.STOP.grid(column=4, row=1)

class RUNNING_TIMER:
    def __init__(self, root):
        self.start_time = time.time()
        self.root = root
        self.frame4 = LabelFrame(root, text="Live Time", padx=25, pady=25, bg="black")
        self.time_passed = Label(root, text="", font=("Helvectica", 37), bg="black")
        self.threading = False

        self.updatetime()
        self.publish3()

    def updatetime(self):
        self.start_time2 = time.time()
        self.current_time = int(self.start_time2 - self.start_time)
        # print(self.current_time)
        sec = ""
        if self.current_time < 60:
            if self.current_time < 10:
                sec = ("0" + str(self.current_time))
            elif self.current_time >= 10:
                sec = str(self.current_time)
        elif self.current_time >= 60:
            sec_entire = self.current_time
            minsec = sec_entire/60
            minsecmin = int(minsec)
            secval = int((minsec - minsecmin)*60)
            if secval < 10:
                sec = ("0" + str(secval))
            elif secval >= 10:
                sec = str(secval)

        min = int(self.current_time/60)
        self.time_passed.config(text=str(min) + ":" + sec)
        self.time_passed.after(10, self.updatetime)

    def publish3(self):
        self.frame4.grid(row=1, column=1, sticky=N)
        self.time_passed.grid()

class DataProcessing:
    def __init__(self, root):
        self.start_time = time.time()
        self.root = root
        self.fig, self.ax = plt.subplots()
        self.frame5 = LabelFrame(root, text="Live Plot", padx=1, pady=1)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame5)
        self.rows = []
        self.figs = []
        self.current_time = []

        self.t1 = threading.Thread(target=self.live_dat, daemon=True)
        self.t2 = threading.Thread(target=self.readFile, daemon=True)
        self.t1.start()
        self.t2.start()

        self.publish5()

    def readFile(self):
        rows = []
        while self.threading:
            with open('DATA_FAKE_YIKES2.csv', 'r') as csv_file_test:
                data_csv = csv.reader(csv_file_test)
                self.timepassed = time.time()
                self.current_time = self.timepassed - self.start_time
                for line in data_csv:
                    # self.ax.
                    rows.append(line[0])
                    self.rows = rows[-1]
                    self.ax.scatter(self.rows,self.rows)
                    self.canvas.draw()

                time.sleep(3)


    def publish5(self):
        self.frame5.grid(row=3, column=0, sticky=NE)
        self.canvas.get_tk_widget().grid()

    def live_dat(self):
        self.threading = True
        acc_axes = ["X", "Y", "Z"]
        with open('DATA_FAKE_YIKES.csv', 'w') as csv_file:
            write_file = csv.DictWriter(csv_file, fieldnames=acc_axes)
            write_file.writeheader()
        while self.threading:
            try:
                # time_current = time.time()
                # self.time_passed = time_current - start_time
                fake_data = Faker()
                self.DATA_FAKE = [int(fake_data.latitude()), int(fake_data.latitude()), int(fake_data.latitude())]
                # self.print_dat = float(self.DATA_FAKE[0])
                with open('DATA_FAKE_YIKES2.csv', 'a') as csv_file:
                    write_file = csv.DictWriter(csv_file, fieldnames=acc_axes)
                    dat = {
                        "X": self.DATA_FAKE[0],
                        "Y": self.DATA_FAKE[1],
                        "Z": self.DATA_FAKE[2]
                    }
                    write_file.writerow(dat)
                time.sleep(3)

            except:
                pass





if __name__ == "__main__":
    RootGUI()
    BUTTONS()
    RUNNING_TIMER()
    DataProcessing()



























