import tkinter as tk
from tkinter.ttk import Progressbar
class UIPlayerList():
    def __init__(self, root):
        self.list = []
        self.root = root

    def addPlayer(self,player):
        self.list.append(UIPlayer(self.root, player))
    def removePlayer(self, player):
        print("remove")
        self.list.remove(player)
    def clearPlayers(self):
        del self.list[:]
    def update(self):
        for p in self.list:
            p.update()
class UIPlayer():
    def __init__(self, root, player):
        self.player = player
        self.root = root
        self.playerFrame = tk.Frame(self.root)
        self.playerFrame.pack()
        self.playerLbl = tk.Label(self.playerFrame,text=player.name)
        self.playerLbl.pack(side="left")
        self.stats = tk.Frame(self.playerFrame)
        self.stats.pack()
        self.hp = Progressbar(self.stats, maximum=player.maxHp, value=player.hp)
        self.hp.pack()
        self.mana = Progressbar(self.stats, maximum=player.maxMana, value=player.mana)
        self.mana.pack()
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