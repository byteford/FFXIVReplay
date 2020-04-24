import tkinter as tk
import data
class UI:
    def nextClick(self,event):
        self.fileProc.readNextLine()
    def contClick(self, event):
        data.go = True
        self.fileProc.readNextLine()
    def InClick(self, event):
        data.scale = data.scale*2
        self.play.resetCam()
        self.play.resetMove()
    def outClick(self, event):
        data.scale = data.scale/2
        self.play.resetCam()
        self.play.resetMove()
    def speedUpClick(self, event):
        data.playSpeed = data.playSpeed/2
        print(data.playSpeed)
    def speedDownClick(self, event):
        data.playSpeed = data.playSpeed*2
        print(data.playSpeed)
    def loadFile(self, event):
        data.fileName = tk.filedialog.askopenfilename()
        self.loadZone()
    def upClick(self, event):
        self.play.moveCam(0,1)
    def downClick(self, event):
        self.play.moveCam(0,-1)
    def leftClick(self, event):
        self.play.moveCam(1,0)
    def rightClick(self, event):
        self.play.moveCam(-1,0)
    def pauseClick(self, event):
        data.go = False
    def toggleLogClick(self,event):
        data.log = not data.log
        print("Log set to: ", data.log)
    
    def loadZone(self):
        def popupMenuCallBack(*args):
            self.fileProc.setLineToRead(int(ZoneStart[int(self.popupVar.get().split('|')[0])]))
            print("202",ZoneStart)
        log = open(data.fileName, "r",encoding="utf-8")
        ZoneStart = []
        self.popupMenu['menu'].delete(0,'end')
        line = "start"
        lineNum = 0
        num = 0
        while line[0] != data.EOF:
            line = log.readline()
            lineNum = lineNum + 1
            line = line.split('|')
            if(line[0] == data.ChangeZone):
                self.popupMenu['menu'].add_command(label=str(num)+ "|"+line[3], command=tk._setit(self.popupVar,str(num)+ "|"+line[3]))
                ZoneStart.append(lineNum)
                if(data.log):
                    print("change Zone")
                num = num + 1
            #print(line)
        if(data.log):
            print(ZoneStart)
        if(data.trace != None):
            self.popupVar.trace_vdelete("w", data.trace)
        data.trace = self.popupVar.trace("w",popupMenuCallBack)
    def setupButtons(self):

        self.parentFrame = tk.Frame(self.root)
        self.parentFrame.grid(row=1,column=0)
        self.midFrame = tk.Frame(self.parentFrame)
        self.midFrame.grid(row=0,column=1)
        self.buttonFrame = tk.Frame(self.parentFrame)
        self.buttonFrame.grid(row=0,column=0)

        self.arrowFrame = tk.Frame(self.parentFrame)
        self.arrowFrame.grid(row=0,column=2)

        self.buttonFrame.grid_columnconfigure(0,weight=1)
        self.arrowFrame.grid_columnconfigure(0,weight=1)
        self.nextBtn = tk.Button(self.buttonFrame, text='Next')
        self.contBtn = tk.Button(self.buttonFrame, text="Continue")
        self.zoomInBtn = tk.Button(self.buttonFrame, text='In')
        self.zoomOutBtn = tk.Button(self.buttonFrame, text="out")
        self.speedUpBtn = tk.Button(self.buttonFrame, text='+')
        self.speedDownBtn = tk.Button(self.buttonFrame, text="-")
        self.pauseBtn = tk.Button(self.buttonFrame, text="pause")
        self.toggleLogBtn = tk.Button(self.buttonFrame, text="ToggleLog")
        self.nextBtn.grid(row=0, column=1, sticky="ew")
        self.contBtn.grid(row=0, column=2, sticky="ew")
        self.zoomInBtn.grid(row=1, column=1, sticky="ew")
        self.zoomOutBtn.grid(row=1, column=2, sticky="ew")
        self.speedUpBtn.grid(row=2, column=1, sticky="ew")
        self.speedDownBtn.grid(row=2, column=2, sticky="ew")
        self.pauseBtn.grid(row=3, column=1, sticky="ew")
        self.toggleLogBtn.grid(row=3,column=2, sticky="ew")
        self.nextBtn.bind('<Button-1>', self.nextClick)
        self.contBtn.bind('<Button-1>', self.contClick)
        self.zoomInBtn.bind('<Button-1>', self.InClick)
        self.zoomOutBtn.bind('<Button-1>', self.outClick)
        self.speedUpBtn.bind('<Button-1>', self.speedUpClick)
        self.speedDownBtn.bind('<Button-1>', self.speedDownClick)
        self.pauseBtn.bind('<Button-1>', self.pauseClick)
        self.toggleLogBtn.bind('<Button-1>', self.toggleLogClick)
        self.upBtn= tk.Button(self.arrowFrame, text='up')
        self.downBtn= tk.Button(self.arrowFrame, text='down')
        self.leftBtn= tk.Button(self.arrowFrame, text='left')
        self.rightBtn= tk.Button(self.arrowFrame, text='right')
        self.upBtn.grid(row=0, column=1, sticky="ew")
        self.downBtn.grid(row=0, column=2, sticky="ew")
        self.leftBtn.grid(row=1, column=1, sticky="ew")
        self.rightBtn.grid(row=1, column=2, sticky="ew")

        self.upBtn.bind('<Button-1>', self.upClick)
        self.downBtn.bind('<Button-1>', self.downClick)
        self.leftBtn.bind('<Button-1>', self.leftClick)
        self.rightBtn.bind('<Button-1>', self.rightClick)


        self.popupVar = tk.StringVar(None)
        self.popupVar.set('Choose Zone')
        self.choises = [2,3,1]
        self.popupMenu = tk.OptionMenu(self.midFrame,self.popupVar,*self.choises)
        self.popupMenu.grid(row=0,column=0)

        self.LoadFileBtn = tk.Button(self.midFrame, text="Load File")
        self.LoadFileBtn.grid(row=1,column=0)
        self.LoadFileBtn.bind('<Button-1>', self.loadFile)
        self.loadZone()
    def setUpSidePannel(self):
        self.sidePannelFrame = tk.Frame(self.root)
        self.sidePannelFrame.grid(row=0,column=2)
        self.cast = tk.Label(self.sidePannelFrame, text="im a casting")
        self.cast.pack(side="top")
        return
    def addPlayer(self, player):
        print("add: ", player, " to the ui")
        return
    def clearPlayers(self):
        return
    def __init__(self, root, play, fileProc):
        self.root = root
        self.play = play
        self.fileProc = fileProc
        self.setupButtons()
        self.setUpSidePannel()
        