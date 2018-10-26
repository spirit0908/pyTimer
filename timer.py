#!/usr/bin/python

#import Tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime
#import wiringPi2 as wiringpi
import RPi.GPIO as GPIO

global endTime 
global timer_M
global timer_S
global Timer_val

def quit(*args):
    root.destroy()

def show_time():
    # Get the time remaining until the event
    #    remainder = endTime - datetime.datetime.now()
    # remove the microseconds part
    #    remainder = remainder - datetime.timedelta(microseconds=remainder.microseconds)
    # Show the time left
    #    txt.set(remainder)
   
    # timer_M = 1
    global timer_M
    global timer_S
    global timer_val


    #Read GPIO input pin 40-BCM21-wiringpi29
    myinput = GPIO.input(21) 
    # print(myinput)
    if myinput == 1:
        if timer_S >= 59:
            timer_S = 0
        
            timer_M = timer_M + 1
        else:
            timer_S = timer_S + 1
    #End if myinput == 1
    
    #txt.set(timer_H)
    #txt.set(timerm)
    if timer_M<timer_val:
        var_M = timer_val - timer_M - 1
        var_S = 60-timer_S-1
        
        txt.set("{:02d}:{:02d}".format(var_M, var_S))
    elif timer_M==timer_val and timer_S==0:
        lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="red", background="black")
        lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
        txt.set("Total time \n {:02d}:{:02d}". format(timer_M, timer_S))
    else:
        txt.set("Total time \n {:02d}:{:02d}". format(timer_M, timer_S))
    # Trigger the countdown after 1000ms
    root.after(1000, show_time)


# Use tkinter lib for showing the clock
root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("x", quit)
root.after(1000, show_time)

# Set the end date and time for the countdown
endTime = datetime.datetime(2017, 9, 19, 9, 0, 0)
#endTime = datetime.datetime.now() + datetime.datetime(0, 0, 0, 0, 45, 0)
timer_val = 40
timer_M = 00
timer_S = -1

GPIO.setmode(GPIO.BCM)
#Setup the port 29 as inout (0)
GPIO.setup(21, GPIO.IN)

fnt = font.Font(family='Helvetica', size=60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="green", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
