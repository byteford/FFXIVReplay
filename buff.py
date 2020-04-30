class buff:
    def __init__(self, ID, name, time, player):
        self.ID = ID
        self.name = name
        self.time = time
        self.player = player
    def addUI(self, buffLbl):
        self.buffLbl = buffLbl