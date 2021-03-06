import tkinter as tk
import data
from Event import Event
from UIPlayerList import UIPlayerList
class UI:
    def nextClick(self,event):
        self.readLineEvt()
        #self.fileProc.readNextLine()
    def contClick(self, event):
        data.go = True
        self.readLineEvt()
        #self.fileProc.readNextLine()
    def InClick(self, event):
        data.scale = data.scale*2
        #self.cam.resetCam()
        self.CamResetEvt()
    def outClick(self, event):
        data.scale = data.scale/2
        #self.cam.resetCam()
        self.CamResetEvt()
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
        #self.cam.moveCam(0,1)
        self.moveCamEvt(0,1)
    def downClick(self, event):
        #self.cam.moveCam(0,-1)
        self.moveCamEvt(0,-1)
    def leftClick(self, event):
        #self.cam.moveCam(1,0)
        self.moveCamEvt(1,0)
    def rightClick(self, event):
        #self.cam.moveCam(-1,0)
        self.moveCamEvt(-1,0)
    def pauseClick(self, event):
        data.go = False
    def toggleLogClick(self,event):
        data.log = not data.log
        print("Log set to: ", data.log)
    def loadZone(self):
        def popupMenuCallBack(*args):
            #self.fileProc.setLineToRead(int(ZoneStart[int(self.popupVar.get().split('|')[0])]))
            self.setReadLineEvt(int(ZoneStart[int(self.popupVar.get().split('|')[0])])-1)
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
        self.parentFrame.grid(row=1,column=1)
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
    def onRFrameConfigure(self, event):
        self.Rcanvas.configure(scrollregion=self.Rcanvas.bbox("all"))
        return
    def onLFrameConfigure(self, event):
        self.Lcanvas.configure(scrollregion=self.Lcanvas.bbox("all"))
        return
    def setUpSidePannel(self):
        self.LParentFrame = tk.Frame(self.root)
        self.LParentFrame.grid(row=0,column=0)

        self.Lcanvas = tk.Canvas(self.LParentFrame, width =200,height=500)
        self.LsidePannelFrame = tk.Frame(self.Lcanvas)
        self.Lscrollbar = tk.Scrollbar(self.LParentFrame, command=self.Lcanvas.yview)
        self.Lcanvas.configure(yscrollcommand=self.Lscrollbar.set)
        self.Lscrollbar.pack(side="left", fill="y")
        self.Lcanvas.pack(side="right", fill="both", expand=True)
        self.Lcanvas.create_window((0,0), window=self.LsidePannelFrame, anchor="nw")
        self.LsidePannelFrame.bind("<Configure>",self.onLFrameConfigure)
        self.Lcanvas.configure(scrollregion=self.Lcanvas.bbox("all"))




        self.RParentFrame = tk.Frame(self.root)
        self.RParentFrame.grid(row=0,column=2)

        self.Rcanvas = tk.Canvas(self.RParentFrame, width =200,height=500)
        self.RsidePannelFrame = tk.Frame(self.Rcanvas)
        self.Rscrollbar = tk.Scrollbar(self.RParentFrame, command=self.Rcanvas.yview)
        self.Rcanvas.configure(yscrollcommand=self.Rscrollbar.set)
        self.Rscrollbar.pack(side="right", fill="y")
        self.Rcanvas.pack(side="left", fill="both", expand=True)
        self.Rcanvas.create_window((0,0), window=self.RsidePannelFrame, anchor="nw")
        self.RsidePannelFrame.bind("<Configure>",self.onRFrameConfigure)
        self.Rcanvas.configure(scrollregion=self.Rcanvas.bbox("all"))
        return
    def addPlayer(self, player):
        if(player.NPC):
            self.playerBar.addNPC(player)
        else:
            self.playerBar.addPlayer(player)
        return
    def removePlayer(self,player):
        self.playerBar.removePlayer(player)
        return
    def clearPlayers(self):
        self.playerBar.clearPlayers()
    def update(self):
        self.playerBar.update()
    def startCast(self, ability):
        self.playerBar.startCast(ability)
    def hitCast(self, ability):
        self.playerBar.hitCast(ability)
        return
    def stopCast(self, player):
       
        self.playerBar.stopCast(player)
        return
    def updateTime(self, time):
        self.playerBar.updateTime(time)
    def addBuff(self, buff):
        self.playerBar.addBuff(buff)
    def removeBuff(self, buff):
        self.playerBar.removeBuff(buff)
    def __init__(self, root):
        self.root = root
        #self.cam = cam
        self.setupButtons()
        self.setUpSidePannel()
        self.readLineEvt = Event()
        self.setReadLineEvt = Event()
        self.moveCamEvt = Event()
        self.CamResetEvt = Event()

        self.playerBar = UIPlayerList(self.LsidePannelFrame,self.RsidePannelFrame)
        
        