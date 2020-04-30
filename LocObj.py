import data
import math
import utility
class LocObj:
    def __init__(self,canvas, NPC, x, y,rot, name, id,hp,maxHp, mana, maxMana ):
        self.canvas = canvas
        self.id = id
        self.size = 5
        self.NPC = NPC
        self.icon = canvas.create_oval(0,0,self.size,self.size,fill= ("red" if NPC else "green"))
        self.lookline = canvas.create_line(0,0,1,1)
        self.label = canvas.create_text(0,0,text=name)
        self.name = name
        self.move(x,y,rot)
        self.maxHp = maxHp
        self.hp = hp
        self.maxMana = maxMana
        self.mana = mana
        self.casting = False
        self.ability = None
        self.buffs = []
        #if(data.log):
        print(id,": Created: ", self.name, " at: ", self.x," : ", self.y)
    def __del__(self):
        self.canvas.delete(self.icon)
        self.canvas.delete(self.label)
        self.canvas.delete(self.lookline)
    def draw(self):
        pass
    def move(self,x,y,rot):
        self.x = x
        self.y = y
        self.rot = rot
        scaledx, scaledy = utility.ScaleLoc(self.x, self.y)
        #scaledx = ((data.playerOffset[0]-self.x)* data.scale) + data.center[0]
        #scaledy = ((data.playerOffset[1]-self.y)*data.scale) + data.center[1]
        self.canvas.coords(self.icon, scaledx-self.size/2, scaledy-self.size/2,scaledx + self.size/2,scaledy+self.size/2)
        self.canvas.coords(self.label, scaledx, scaledy)
        self.canvas.coords(self.lookline,scaledx,scaledy,scaledx+math.cos(rot-1.5)*10,scaledy+math.sin(rot-1.5)*10)
        pass
    def resetLoc(self):
        self.move(self.x,self.y,self.rot)
        if self.casting:
            self.ability.updateAOE()
    def hide(self):
        self.canvas.itemconfigure(self.icon,state='hidden')
        self.canvas.itemconfigure(self.label,state='hidden')
        self.canvas.itemconfigure(self.lookline,state='hidden')
    def show(self):
        self.canvas.itemconfigure(self.icon,state='normal')
        self.canvas.itemconfigure(self.label,state='normal')
        self.canvas.itemconfigure(self.lookline,state='normal')
    def updateStats(self,hp,maxHp, mana, maxMana ):
        self.maxHp = maxHp
        self.hp = hp
        self.maxMana = maxMana
        self.mana = mana
    def startCasting(self,ability):
        self.casting = True
        self.ability = ability
    def isCasting(self, abilityID):
        return self.casting and abilityID == self.ability.id
    def stopCasting(self):
        if self.casting:
            self.ability.clear()
        self.casting = False
        self.ability = None
    def addBuff(self, buff):
        self.buffs.append(buff)
        return buff
    def getBuff(self,buffID):
        for b in self.buffs:
            if b.ID == buffID:
                return b
        return None
    def removeBuff(self,buffID):
        temp = self.getBuff(buffID)
        self.buffs.remove(temp)
        return temp