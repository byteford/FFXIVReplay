import tkinter as tk
import tkinter.filedialog
import linecache
import time
import data
from LocObj import LocObj
from Players import players
def nextClick(event):
    readNextLine()
def contClick(event):
    global go
    go = True
    readNextLine()
def InClick(event):
    data.scale = data.scale*2
    play.resetCam()
    play.resetMove()
def outClick(event):
    data.scale = data.scale/2
    play.resetCam()
    play.resetMove()
def speedUpClick(event):
    data.playSpeed = data.playSpeed/2
    print(data.playSpeed)
def speedDownClick(event):
    data.playSpeed = data.playSpeed*2
    print(data.playSpeed)
def loadFile(event):
    data.fileName = tk.filedialog.askopenfilename()
    loadZone()
def upClick(event):
    play.moveCam(0,1)
def downClick(event):
    play.moveCam(0,-1)
def leftClick(event):
    play.moveCam(1,0)
def rightClick(event):
    play.moveCam(-1,0)
def pauseClick(event):
    global go
    go = False
def toggleLogClick(event):
    data.log = not data.log
    print("Log set to: ", data.log)
def readNextLine():
    #line = log.readline()
    data.lineToRead = data.lineToRead + 1
    line = linecache.getline(data.fileName,data.lineToRead)
    line = line.split('|')
    return processLine(line)
def setLineToRead(lineNum):
    data.lineToRead = lineNum
    print("47",data.lineToRead)
    play.clearObjs()
    return
def processLine(procLine):
    try:
        id = procLine[0]
        if(data.log):
            print(procLine)
        if(data.log):
            print(procLine)
        if id in data.notUse:
            #readNextLine()
            return True
        if id == data.ChangeZone:
            if(data.log):
                print("moved to: ",procLine[3])
            play.clearObjs()
            #readNextLine()
            return False
        if id == data.ChangePrimaryPlayer:
            #readNextLine()
            return True
        if id == data.AddCombatant:
            
            if(procLine[12] != '44' ):  
                temp = play.addObj(procLine[2],procLine[3],float(procLine[17]),float(procLine[18]),float(procLine[19]),float(procLine[20]))
                if(procLine[10] == '11540' or procLine[10] == '11541'): # Furor adds that start hidden 
                    temp.hide()
            #readNextLine()
            return True
        if id == data.NetworkUpdateHP:
            play.moveObj(procLine[2].lower(),float(procLine[10]),float(procLine[11]),float(procLine[12]),float(procLine[13]))
            #readNextLine()
            return True
        if id== data.NetworkStatusEffects:
            play.moveObj(procLine[2].lower(),float(procLine[11]),float(procLine[12]),float(procLine[13]),float(procLine[14]))
            #readNextLine()
            return True
        if id == data.RemoveCombatant:
            play.removeObj(procLine[2])
            #readNextLine()
            return True
        if id == data.NetworkAbility: #can move target
            play.moveObj(procLine[2].lower(),float(procLine[40]),float(procLine[41]),float(procLine[42]),float(procLine[43]))
            if(procLine[2] != procLine[3]):
                play.moveObj(procLine[6].lower(),float(procLine[30]),float(procLine[31]),float(procLine[32]),float(procLine[33]))
            return True
        if id == data.NetworkAOEAbility:
            play.moveObj(procLine[2].lower(),float(procLine[40]),float(procLine[41]),float(procLine[42]),float(procLine[43]))
            if(procLine[2] != procLine[3]):
                play.moveObj(procLine[6].lower(),float(procLine[30]),float(procLine[31]),float(procLine[32]),float(procLine[33]))
            return True
        if id == data.NetworkDoT:
            play.moveObj(procLine[2].lower(),float(procLine[13]),float(procLine[14]),float(procLine[15]),float(procLine[16]))
            return True
        if id == data.NetworkEffectResult:
            play.moveObj(procLine[2].lower,float(procLine[11]),float(procLine[12]),float(procLine[13]),float(procLine[14]))
            return True
        if id == data.NetworkNameToggle:
            print(procLine[2].lower())
            temp = play.getObj(procLine[2].lower())
            if(bool(int(procLine[6]))):
                temp.show()
            else:
                temp.hide()
            
            return True
        if id == data.EOF:
            print("END OF FILE")
            return False
    except:
        if(data.log):
            print(procLine)
        return True
    print(procLine)
    print("NEW LINE")



root = tk.Tk()
root.resizable(0,0)
root.wm_attributes("-topmost",1)
width = 1000
height = 500
data.center = [width/2, height/2]
canvas = tk.Canvas(root, width=width,height=height, bd=0, highlightthickness=0)
canvas.pack()

canvas.create_oval(data.center[0],data.center[1],data.center[0]+10,data.center[1]+10,fill='green')

play = players(canvas)


buttonFrame = tk.Frame(root)
buttonFrame.pack(side="right", fill="x")

arrowFrame = tk.Frame(root)
arrowFrame.pack(side="left", fill="x")

buttonFrame.grid_columnconfigure(0,weight=1)
arrowFrame.grid_columnconfigure(0,weight=1)
nextBtn = tk.Button(buttonFrame, text='Next')
contBtn = tk.Button(buttonFrame, text="Continue")
zoomInBtn = tk.Button(buttonFrame, text='In')
zoomOutBtn = tk.Button(buttonFrame, text="out")
speedUpBtn = tk.Button(buttonFrame, text='+')
speedDownBtn = tk.Button(buttonFrame, text="-")
pauseBtn = tk.Button(buttonFrame, text="pause")
toggleLogBtn = tk.Button(buttonFrame, text="ToggleLog")
nextBtn.grid(row=0, column=1, sticky="ew")
contBtn.grid(row=0, column=2, sticky="ew")
zoomInBtn.grid(row=1, column=1, sticky="ew")
zoomOutBtn.grid(row=1, column=2, sticky="ew")
speedUpBtn.grid(row=2, column=1, sticky="ew")
speedDownBtn.grid(row=2, column=2, sticky="ew")
pauseBtn.grid(row=3, column=1, sticky="ew")
toggleLogBtn.grid(row=3,column=2, sticky="ew")
nextBtn.bind('<Button-1>', nextClick)
contBtn.bind('<Button-1>', contClick)
zoomInBtn.bind('<Button-1>', InClick)
zoomOutBtn.bind('<Button-1>', outClick)
speedUpBtn.bind('<Button-1>', speedUpClick)
speedDownBtn.bind('<Button-1>', speedDownClick)
pauseBtn.bind('<Button-1>', pauseClick)
toggleLogBtn.bind('<Button-1>', toggleLogClick)
upBtn= tk.Button(arrowFrame, text='up')
downBtn= tk.Button(arrowFrame, text='down')
leftBtn= tk.Button(arrowFrame, text='left')
rightBtn= tk.Button(arrowFrame, text='right')
upBtn.grid(row=0, column=1, sticky="ew")
downBtn.grid(row=0, column=2, sticky="ew")
leftBtn.grid(row=1, column=1, sticky="ew")
rightBtn.grid(row=1, column=2, sticky="ew")

upBtn.bind('<Button-1>', upClick)
downBtn.bind('<Button-1>', downClick)
leftBtn.bind('<Button-1>', leftClick)
rightBtn.bind('<Button-1>', rightClick)


popupVar = tk.StringVar(None)
popupVar.set('Choose Zone')
choises = [2,3,1]
popupMenu = tk.OptionMenu(None,popupVar,*choises)
popupMenu.pack()

LoadFileBtn = tk.Button(None, text="Load File")
LoadFileBtn.pack()
LoadFileBtn.bind('<Button-1>', loadFile)



def loadZone():
    def popupMenuCallBack(*args):
        setLineToRead(int(ZoneStart[int(popupVar.get().split('|')[0])]))
        print("202",ZoneStart)
    log = open(data.fileName, "r",encoding="utf-8")
    ZoneStart = []
    popupMenu['menu'].delete(0,'end')
    line = "start"
    lineNum = 0
    num = 0
    while line[0] != data.EOF:
        line = log.readline()
        lineNum = lineNum + 1
        line = line.split('|')
        if(line[0] == data.ChangeZone):
            popupMenu['menu'].add_command(label=str(num)+ "|"+line[3], command=tk._setit(popupVar,str(num)+ "|"+line[3]))
            ZoneStart.append(lineNum)
            if(data.log):
                print("change Zone")
            num = num + 1
        #print(line)
    if(data.log):
        print(ZoneStart)
    if(data.trace != None):
        popupVar.trace_vdelete("w", data.trace)
    data.trace = popupVar.trace("w",popupMenuCallBack)
loadZone()


global go
go = readNextLine()


while 1:
    root.update_idletasks()
    root.update()
    if(go):
        go = readNextLine()
   # next.mainloop()
    
    time.sleep(data.playSpeed)