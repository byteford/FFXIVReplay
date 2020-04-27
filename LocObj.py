import data
class LocObj:
    def __init__(self,canvas, color, x, y, name, id,hp,maxHp, mana, maxMana ):
        self.canvas = canvas
        self.id = id
        self.size = 5
        self.icon = canvas.create_oval(0,0,self.size,self.size,fill=color)
        self.label = canvas.create_text(0,0,text=name)
        self.name = name
        self.move(x,y)
        self.maxHp = maxHp
        self.hp = hp
        self.maxMana = maxMana
        self.mana = mana
        #if(data.log):
        print(id,": Created: ", self.name, " at: ", self.x," : ", self.y)
    def __del__(self):
        self.canvas.delete(self.icon)
        self.canvas.delete(self.label)
    def draw(self):
        pass
    def move(self,x,y):
        self.x = x
        self.y = y
        scaledx = ((data.playerOffset[0]-self.x)* data.scale) + data.center[0]
        scaledy = ((data.playerOffset[1]-self.y)*data.scale) + data.center[1]
        self.canvas.coords(self.icon, scaledx, scaledy,scaledx + self.size,scaledy+self.size)
        self.canvas.coords(self.label, scaledx, scaledy)
        if(data.log):
            print("move: ", self.name, "to: ",scaledx," : ", scaledy, "act: " ,x," : ",y)
        pass
    def resetLoc(self):
        self.move(self.x,self.y)
    def hide(self):
        self.canvas.itemconfigure(self.icon,state='hidden')
        self.canvas.itemconfigure(self.label,state='hidden')
    def show(self):
        self.canvas.itemconfigure(self.icon,state='normal')
        self.canvas.itemconfigure(self.label,state='normal')
    def updateStats(self,hp,maxHp, mana, maxMana ):
        self.maxHp = maxHp
        self.hp = hp
        self.maxMana = maxMana
        self.mana = mana
