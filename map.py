import tkinter as tk
import data
from Players import players
from ZoneData import ZoneData
class map:
    def __init__(self, root, width, height, camra, ui):
        self.root = root
        self.camra = camra
        self.ui = ui
        self.canvas = tk.Canvas(root, width=width,height=height, bd=0, highlightthickness=0)
        self.canvas.grid(row=0,column=1)
        self.canvas.create_line(data.center[0] -5,data.center[1],data.center[0]+5,data.center[1])
        self.canvas.create_line(data.center[0] ,data.center[1]-5,data.center[0],data.center[1]+5)
        self.play = players(camra,self.canvas, ui)
        self.zoneData = ZoneData()
    def addObj(self,arr):
        self.play.addObj(arr)
    def moveObj(self,id,x,y,z,rot):
        self.play.moveObj(id,x,y,z,rot)
    def UpdateObjStat(self,id,hp,maxHp,mana,maxMana):
        self.play.UpdateObjStat(id,hp,maxHp,mana,maxMana)
    def removeObj(self,id):
        self.play.removeObj(id)
    def clearObjs(self):
        self.play.clearObjs()
        self.zoneData.clearZone()
    def resetMove(self):
        self.play.resetMove()
        self.zoneData.updateMove()
    def castAbility(self, playerId, abilityName, abilityId,targetId,startTime, castTime):
        self.play.castAbility(playerId,abilityName,abilityId,targetId,startTime,castTime)
    def hitAbility(self,playerId, abilityName, abilityId,targetId):
        self.play.hitAbility(playerId,abilityName,abilityId,targetId)
    def LoadZone(self, arr):
        self.zoneData.load(arr[2],self.canvas)
    def gainBuff(self,playerId, buffName, buffId, targetId, time):
        self.play.gainBuff(playerId,buffName,buffId,targetId, time)
    def removeBuff(self,playerId,buffName,buffId,targetId):
        self.play.removeBuff(playerId,buffName,buffId,targetId)
