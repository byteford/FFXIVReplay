from datetime import datetime
import data
def strToDateTime(time):
    tempTime = time.replace("0000","000").replace("T", " ").split("+")[0]
    return datetime.fromisoformat(tempTime)
def ScaleLoc(x,y):
    return ((data.playerOffset[0]-x)* data.scale) + data.center[0], ((data.playerOffset[1]-y)*data.scale) + data.center[1]
