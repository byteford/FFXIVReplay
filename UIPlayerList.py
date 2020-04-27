import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter.ttk import Style
class UIPlayerList():
    def __init__(self, Lroot,Rroot):
        self.list = []
        self.Lroot = Lroot
        self.Rroot = Rroot
    def updateTime(self, time):
        for p in self.list:
            p.updateCastTime(time)
    def addNPC(self, player):
        self.list.append(UIPlayer(self.Rroot, player))
    def addPlayer(self,player):
        self.list.append(UIPlayer(self.Lroot, player))
    def removePlayer(self, player):
        self.list.remove(self.getPlayerUI(player))
    def clearPlayers(self):
        del self.list[:]
    def update(self):
        for p in self.list:
            p.update()
    def getPlayerUI(self, player):
        for p in self.list:
            if(p.player.id == player.id):
                return p
        return None
    def startCast(self, ability):
        self.getPlayerUI(ability.player).startCast(ability)
        return
    def hitCast(self,ability):
        self.getPlayerUI(ability.player).hitCast(ability)
    def stopCast(self, player):
        
        self.getPlayerUI(player).stopCast()
class UIPlayer():
    def __init__(self, root, player):
        self.ability = None
        self.player = player
        self.root = root
        self.playerFrame = tk.Frame(self.root)
        self.playerFrame.pack()
        self.playerLbl = tk.Label(self.playerFrame,text=player.name)
        self.playerLbl.pack(side="top")
        self.stats = tk.Frame(self.playerFrame)
        self.stats.pack()
        self.hp = Progressbar(self.stats,style="green.Horizontal.TProgressbar", maximum=player.maxHp, value=player.hp)
        self.hp.pack(side="left")
        self.mana = Progressbar(self.stats,style="blue.Horizontal.TProgressbar", maximum=player.maxMana, value=player.mana)
        self.mana.pack()
        self.castFrame = tk.Frame(self.playerFrame)
        self.castFrame.pack()
        self.castText = tk.StringVar()
        self.castText.set("cast")
        self.castLable = tk.Label(self.castFrame, textvariable=self.castText)
        self.castLable.pack(side="left")
        self.castBar = Progressbar(self.castFrame,maximum=100, value = 50)
        self.castBar.pack()
    def startCast(self, ability):
        self.ability = ability
        self.castBar['value'] = 0
        self.castText.set(ability.name) 
    def hitCast(self, ability):
        if(ability.name != "Attack"):
            self.ability = ability
            self.castText.set(ability.name) 
    def stopCast(self):
        self.ability = None
        self.castBar['value'] = 100
        pass
    def update(self):
        self.hp['value'] = self.player.hp
        self.mana['value'] = self.player.mana
    def getId(self):
        return self.player.id
    def __del__(self):
        self.mana.destroy()
        self.hp.destroy()
        self.stats.destroy()
        self.playerLbl.destroy()
        self.playerFrame.destroy()
    def updateCastTime(self,time):
        if(self.ability != None):
            self.castBar['value']=100-(self.ability.longLeft(time)*100)