import data
from LocObj import LocObj
from ability import ability
startHidden = {'11540','11541'}
class players:    
    def __init__(self,cam, canvas, UI):
        self.players = []
        self.canvas = canvas
        self.cam = cam
        self.UI = UI
    def addObj(self,arr):#id,name, x,y,z,rot): procLine[2],procLine[3],float(procLine[17]),float(procLine[18]),float(procLine[19]),float(procLine[20])
        id = arr[2].lower()
        name = arr[3]
        x = float(arr[17])
        y = float(arr[18])
        rot = float(arr[20])
        hp = int(arr[11])
        maxHp = int(arr[12])
        mana = int(arr[13])
        maxMana = int(arr[14])
        if(arr[12] != '44' or True):
            if(not self.players):
                self.cam.setCam(x,y)
            if(self.getObj(id) == None):
                if(id.startswith("400")):
                    NPC = True
                    print(arr)
                else:
                    NPC = False
                temp = LocObj(self.canvas, NPC,x,y,rot, name,id,hp,maxHp,mana,maxMana)
                self.players.append(temp)
                self.UI.addPlayer(temp)
                if(arr[10] in startHidden ): # Furor adds that start hidden 
                    temp.hide()
                return temp
        return
    def moveObj(self,id, x,y,z,rot):
        play = self.getObj(id)
        #print(id," : ",play)
        if(play != None):
            play.move(x,y,rot) 
            
        return
    def UpdateObjStat(self,id,hp,maxHp,mana,maxMana ):
        play = self.getObj(id)
        
        if(play != None):
            play.updateStats(hp,maxHp,mana,maxMana)
    def getObj(self,id):
        for p in self.players:
            if p.id == id:
                return p
        return None
    def removeObj(self,id):
        play = self.getObj(id)
        if(play != None):
            self.players.remove(play)
            self.UI.removePlayer(play)
            if(data.log):
                print("Removed: ", id)
        return
    def clearObjs(self):
        self.UI.clearPlayers()
        del self.players[:]
        return
    def resetMove(self):
        for p in self.players:
            p.resetLoc()
    def castAbility(self, playerId, abilityName, abilityId,targetId,startTime, castTime):
        play = self.getObj(playerId)
        abil = ability(abilityName,abilityId,self.getObj(playerId), targetId,startTime=startTime, castTime=castTime)
        play.startCasting(abil)
        self.UI.startCast(abil)
    def hitAbility(self,playerId, abilityName, abilityId,targetId):
        play = self.getObj(playerId)
        if(play.isCasting(abilityId)):
            play.stopCasting()
            self.UI.stopCast(play)
            return
        self.UI.hitCast(ability(abilityName,abilityId,play, targetId))

