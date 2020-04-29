import datetime
import utility
import data
class ability:
    def __init__(self, name, id, player,targetId,canvas,startTime=0, castTime= 0):

        self.name = name
        self.id = id
        self.player = player
        self.castTime = castTime
        self.targetId = targetId
        self.canvas = canvas
        self.startTime = startTime
        self.endTime = None
        self.aoe = False
        if(startTime != 0):
            self.startTimedt = utility.strToDateTime(self.startTime)
            self.castTimeDelta = datetime.timedelta(seconds=float(castTime))
            self.endTime = self.startTimedt + self.castTimeDelta
            print("endtimeSetUP")
        if(player.NPC):
            if id in ['4D66']:
                print("makeing")
            #if id =='4D66':
                self.createAOE()
            print(player.id,name, id)
    def longLeft(self, time):
        if(self.endTime == None):
            return 0
        else:
            temptime = (self.endTime-time)
            percent = temptime/self.castTimeDelta
            if(percent >=0):
                return percent
            else:
                print("error ability percent is :", percent, "is", self.name,"finishing")
                return 0
    def createAOE(self):
        self.aoe = True
        print(self.player.x,self.player.y)
        self.x, self.y = utility.ScaleLoc(self.player.x,self.player.y)
        self.size = 39*data.scale
        print(self.x,self.y,self.x+39*data.scale,self.y+39*data.scale)
        self.pie = self.canvas.create_arc(self.x,self.y,self.x+39*data.scale,self.y+39*data.scale, start=135,extent=270, fill="yellow")
    def updateAOE(self):
        if(self.aoe):
            self.x, self.y = utility.ScaleLoc(self.player.x,self.player.y)
            self.size = 39*data.scale
            self.canvas.coords(self.pie,self.x-self.size/2,self.y-self.size/2,self.x+self.size/2,self.y+self.size/2)
    
