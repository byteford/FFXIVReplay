import tkinter as tk
import data
class ZoneData(list):
    def __init__(self):
        self.append(ZoneRect('38b',100,100,100,100))
        #self.append(ZoneCircle('38d',18,4,39))
        self.append(ZoneCircle('38d',119,119,39))
        self.currentzone = None
    def load(self,id, canvas):
        for z in self:
            if id == z.id:
                self.currentzone = z
                z.makeShape(canvas)
    def updateMove(self):
        if(self.currentzone):
            self.currentzone.updateMove()
        pass
    def clearZone(self):
        if(self.currentzone):
            self.currentzone.clear()
class Zone():
    def __init__(self, id,x,y,height=0,width=0,rad=0):
        self.id = id
        self.x =x
        self.y = y
        self.height = height
        self.width = width
        self.rad = rad
        self.shape = None
        self.canvas = None
    def makeShape(self,canvas):
        return
    def updateMove(self,x,y):
        return
    def clear(self):
        return
class ZoneRect(Zone):
    def __init__(self, id,x,y,width,height):
        super(ZoneRect,self).__init__(id,x,y,height,width,0)
    def makeShape(self, canvas):
        self.canvas = canvas
        self.shape = canvas.create_rectangle(self.x,self.y,self.x+self.width,self.y+self.height)
        pass
class ZoneCircle(Zone):
    def __init__(self,id,x,y,rad):
        super(ZoneCircle,self).__init__(id,x,y,0,0,rad)
    def makeShape(self,canvas):
        self.canvas = canvas
        x = ((data.playerOffset[0]-self.x)* data.scale) + data.center[0]
        y = ((data.playerOffset[1]-self.y)*data.scale) + data.center[1]
        #x = data.center[0]-self.x
        #y = data.center[1]-self.y
        self.shape = canvas.create_oval(x,y,x+self.rad*data.scale,y+self.rad*data.scale)
    def updateMove(self):
        x = ((data.playerOffset[0]-self.x)* data.scale) + data.center[0]
        y = ((data.playerOffset[1]-self.y)*data.scale) + data.center[1]
        #print(x,y)
        self.canvas.coords(self.shape,x,y,x+self.rad*data.scale,y+self.rad*data.scale)
    def clear(self):
        self.canvas.delete(self.shape)