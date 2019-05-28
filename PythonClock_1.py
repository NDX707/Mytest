#!/usr/bin/python

import tkinter
from time import strftime

root = tkinter.Tk()
root.title("Digital Clock Using Python")
myClock = tkinter.Label()
myClock['text'] = '21:18:00'
myClock.pack()
myClock['font'] = 'Tahoma 150 bold'

strftime('%H:%M:%S')

def tic():
    myClock['text'] = strftime('%H:%M:%S')

tic()

def tac():
    tic()
    myClock.after(1000, tac)

tac()

#myClock['text']
#myClock['fg'] = 'white'
myClock['fg'] = 'limegreen'
#myClock['bg'] = '#af25f0'
myClock['bg'] = 'black'

root.mainloop()
    
    
