import data
class cam:
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