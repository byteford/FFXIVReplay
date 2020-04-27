class ability:
    def __init__(self, name, id, player,targetId,startTime=0, castTime= 0):
        self.name = name
        self.id = id
        self.player = player
        self.castTime = castTime
        self.targetId = targetId
        self.startTime = startTime
        print(startTime, " ", castTime)