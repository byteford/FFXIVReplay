import datetime
import utility
class ability:
    def __init__(self, name, id, player,targetId,startTime=0, castTime= 0):
        self.name = name
        self.id = id
        self.player = player
        self.castTime = castTime
        self.targetId = targetId
        self.startTime = startTime
        self.endTime = None
        if(startTime != 0):
            self.startTimedt = utility.strToDateTime(self.startTime)
            self.castTimeDelta = datetime.timedelta(seconds=float(castTime))
            self.endTime = self.startTimedt + self.castTimeDelta
    def longLeft(self, time):
        if(self.endTime == None):
            return 0
        else:
            temptime = (self.endTime-time)
            percent = temptime/self.castTimeDelta
            if(percent >=0):
                return percent
            else:
                print("error ability percent is :", percent, "is", self.name,"finishing")
                return 0
