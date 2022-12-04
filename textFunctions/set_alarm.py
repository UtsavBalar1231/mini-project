import tkinter as tk
from tkinter import ttk
import datetime as dt
import time
from threading import *
import winsound as ws


# Alarm function to play sound
def alarm(setAlarmTimer):
    while True:
        time.sleep(1)
        actualTime = dt.datetime.now()
        currentTime = actualTime.strftime("%H : %M : %S")
        the_message = "Current Time: " + str(currentTime)
        print(the_message)
        if currentTime == setAlarmTimer:
            print("Alarm Ringing")
            for i in range(5):
                ws.Beep(1000, 1000)
            break
        elif currentTime > setAlarmTimer:
            break


# Get the alarm time from the user
def getAlarmTime():
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"
    alarm(alarmSetTime)


# Create thread to run alarm function
def setAlarm():
    alarmThread = Thread(target=getAlarmTime)
    alarmThread.start()


# GUI
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x200")
root.resizable(False, False)

timeFrame = ttk.LabelFrame(root, text="Set Time")
timeFrame.pack(padx=20, pady=20)

hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()

hourEntry = ttk.Entry(timeFrame, width=3,
                      textvariable=hour, font=("Arial", 18, ""))
hourEntry.grid(row=0, column=0)

minuteEntry = ttk.Entry(
    timeFrame, width=3, textvariable=minute, font=("Arial", 18, ""))
minuteEntry.grid(row=0, column=1)

secondEntry = ttk.Entry(
    timeFrame, width=3, textvariable=second, font=("Arial", 18, ""))
secondEntry.grid(row=0, column=2)

hourEntry.insert(0, "00")
minuteEntry.insert(0, "00")
secondEntry.insert(0, "00")

setAlarmButton = ttk.Button(root, text="Set Alarm", command=setAlarm)
setAlarmButton.pack(pady=20)

# Show current time
currentTime = dt.datetime.now()
currentTime = "Current Time: " + currentTime.strftime("%H : %M : %S")
currentTimeLabel = ttk.Label(root, text=currentTime)
currentTimeLabel.pack()


# update current time every second
def update_time():
    currentTime = dt.datetime.now()
    currentTime = "Current Time: " + currentTime.strftime("%H : %M : %S")
    currentTimeLabel.configure(text=currentTime)
    root.after(1000, update_time)


# start the update_time function
root.after(1000, update_time)


# run the main loop
root.mainloop()
