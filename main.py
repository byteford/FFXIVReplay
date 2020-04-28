import tkinter as tk
import tkinter.filedialog
import linecache
import time
import data
from LocObj import LocObj
from FileProc import FileProc
from UI import UI
from cam import cam
from tkinter import ttk
from map import map

root = tk.Tk()
root.resizable(0,0)
root.wm_attributes("-topmost",1)
width = 500
height = 700
data.center = [width/2, height/2]


style = tkinter.ttk.Style()
style.theme_use('clam')
style.configure("green.Horizontal.TProgressbar", background='green')
style.configure("blue.Horizontal.TProgressbar",  background='blue')




#canvas.create_oval(data.center[0],data.center[1],data.center[0]+10,data.center[1]+10,fill='green')

ui = UI(root)
camra = cam(ui)
_map = map(root,width,height, camra, ui)
FP = FileProc(_map, ui)
data.go = FP.readNextLine()
try:
    while 1:
        root.update_idletasks()
        root.update()
        if(data.go):
            data.go = FP.readNextLine()
        _map.resetMove()
        ui.update()
            # next.mainloop()
        time.sleep(data.playSpeed)

except tk.TclError:
    print("application closed")
