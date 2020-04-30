import datetime
import utility
import data
import math
class ability:
    def __init__(self, name, id, player,targetId,canvas,startTime=0.0, castTime= 0.0):
        self.name = name
        self.id = id
        self.player = player
        self.castTime = castTime
        self.targetId = targetId
        self.canvas = canvas
        self.startTime = startTime
        self.endTime = None
        self.aoe = False
        self.show = True
        self.timeToShow = castTime
        if(startTime != 0):
            self.startTimedt = utility.strToDateTime(self.startTime)
            self.castTimeDelta = datetime.timedelta(seconds=castTime)
            self.endTime = self.startTimedt + self.castTimeDelta
        if(player.NPC):
            if(self.castTime > 0):
                if id in ['4D66']:
                #if id =='4D66':
                    self.createCleave(39,45,270)
                elif id in ['4DB7']:
                    self.createCleave(58,45,270)
                elif id in ['4DC3']:
                    self.show = False
                    self.timeToShow = 5
                    self.createCleave(58,45,270)
    def longLeft(self, time):
        if(self.endTime == None):
            return 0
        else:
            temptime = (self.endTime-time)
            percent = temptime/self.castTimeDelta
            if self.timeToShow>temptime.seconds:
                self.showAOE()
            if(percent >=0):
                return percent
            else:
                if data.log:
                    print("error ability percent is :", percent, "is", self.name,"finishing")
                self.player.stopCasting()
                return 0
    def createCleave(self, size,start,extent):
        self.aoe = True
        self.x, self.y = utility.ScaleLoc(self.player.x,self.player.y)
        self.lSize = size
        self.size = self.lSize*data.scale
        self.pie = self.canvas.create_arc(self.x-self.size/2,self.y-self.size/2,self.x+self.size/2,self.y+self.size/2, start=math.degrees(self.player.rot-1.5) + start,extent=extent, fill="yellow")
        self.canvas.tag_lower(self.pie)
        if not self.show:
            self.hideAOE()
    def updateAOE(self):
        if(self.aoe):
            self.x, self.y = utility.ScaleLoc(self.player.x,self.player.y)
            self.size = self.lSize*data.scale
            self.canvas.coords(self.pie,self.x-self.size/2,self.y-self.size/2,self.x+self.size/2,self.y+self.size/2)
    def clear(self):
        if(self.aoe):
            self.canvas.delete(self.pie)
    def showAOE(self):
        self.canvas.itemconfigure(self.pie,state='normal')
    def hideAOE(self):
        self.canvas.itemconfigure(self.pie,state='hidden')
