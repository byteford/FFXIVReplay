import tkinter as tk
import tkinter.filedialog
import linecache
import time
import data
from LocObj import LocObj
from Players import players
from FileProc import FileProc
from UI import UI



root = tk.Tk()
root.resizable(0,0)
root.wm_attributes("-topmost",1)
width = 1000
height = 700
data.center = [width/2, height/2]
canvas = tk.Canvas(root, width=width,height=height, bd=0, highlightthickness=0)
canvas.pack()

#canvas.create_oval(data.center[0],data.center[1],data.center[0]+10,data.center[1]+10,fill='green')
canvas.create_line(data.center[0] -5,data.center[1],data.center[0]+5,data.center[1])
canvas.create_line(data.center[0] ,data.center[1]-5,data.center[0],data.center[1]+5)
play = players(canvas)

FP = FileProc(play)

ui = UI(root,play, FP)

data.go
data.go = FP.readNextLine()


while 1:
    root.update_idletasks()
    root.update()
    if(data.go):
        data.go = FP.readNextLine()
   # next.mainloop()
    
    time.sleep(data.playSpeed)