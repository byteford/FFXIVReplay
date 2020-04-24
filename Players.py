import data
from LocObj import LocObj
class players:
    def __init__(self, canvas):
        self.players = []
        self.canvas = canvas
    def addObj(self,id,name, x,y,z,rot):
        if(not self.players):
            self.setCam(x,y)
        if(self.getObj(id) == None):
            temp = LocObj(self.canvas, 'red',x,y, name,id)
            self.players.append(temp)
            return temp
        return
    def moveObj(self,id, x,y,z,rot):
        play = self.getObj(id)
        #print(id," : ",play)
        if(play != None):
            play.move(x,y) 
            
        return
    def getObj(self,id):
        for p in self.players:
            if p.id == id:
                return p
        return None
    def removeObj(self,id):
        play = self.getObj(id)
        if(play != None):
            self.players.remove(play)
            if(data.log):
                print("Removed: ", id)
        return
    def clearObjs(self):
        del self.players[:]
        return
    def resetMove(self):
        for p in self.players:
            p.resetLoc()
    def setCam(self,x,y):
        if(data.log):
                print("cam set to ",x ," : ", y)
        data.LookPos = [x,y]
        #data.playerOffset = [(data.center[0]+ x)*data.scale,(data.center[1] +y)*data.scale]
        data.playerOffset = [x,y]
        return
    def resetCam(self):
        self.setCam(data.LookPos[0],data.LookPos[1])
    def moveCam(self, x,y):
        self.setCam(data.LookPos[0]+x,data.LookPos[1]+y)
        self.resetMove()