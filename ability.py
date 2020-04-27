import datetime
class ability:
    def __init__(self, name, id, player,targetId,startTime=0, castTime= 0):
        self.name = name
        self.id = id
        self.player = player
        self.castTime = castTime
        self.targetId = targetId
        self.startTime = startTime
        if(startTime != 0):
            self.startTime = self.startTime.replace("0000","000").replace("T", " ").split("+")[0]
            print(self.startTime, " ", castTime)