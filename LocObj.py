import data
class LocObj:
    def __init__(self,canvas, color, x, y, name, id):
        self.canvas = canvas
        self.id = id
        self.size = 15
        self.icon = canvas.create_oval(10,10,25,25,fill=color)
        self.label = canvas.create_text(10,10,text=name)
        self.name = name
        self.move(x,y)
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