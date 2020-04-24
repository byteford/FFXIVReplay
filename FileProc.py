import data
import linecache
class FileProc:
    def __init__(self, play):
        self.play = play
    def readNextLine(self):
        #line = log.readline()
        data.lineToRead = data.lineToRead + 1
        line = linecache.getline(data.fileName,data.lineToRead)
        line = line.split('|')
        return self.processLine(line)
    def setLineToRead(self, lineNum):
        data.lineToRead = lineNum
        print("47",data.lineToRead)
        self.play.clearObjs()
        return
    def processLine(self, procLine):
        try:
            id = procLine[0]
            if(data.log):
                print(procLine)
            if(data.log):
                print(procLine)
            if id in data.notUse:
                #readNextLine()
                return True
            if id == data.ChangeZone:
                if(data.log):
                    print("moved to: ",procLine[3])
                self.play.clearObjs()
                #readNextLine()
                return False
            if id == data.ChangePrimaryPlayer:
                #readNextLine()
                return True
            if id == data.AddCombatant:
                
                if(procLine[12] != '44' ):  
                    temp = self.play.addObj(procLine[2],procLine[3],float(procLine[17]),float(procLine[18]),float(procLine[19]),float(procLine[20]))
                    if(procLine[10] == '11540' or procLine[10] == '11541'): # Furor adds that start hidden 
                        temp.hide()
                #readNextLine()
                return True
            if id == data.NetworkUpdateHP:
                self.play.moveObj(procLine[2].lower(),float(procLine[10]),float(procLine[11]),float(procLine[12]),float(procLine[13]))
                #readNextLine()
                return True
            if id== data.NetworkStatusEffects:
                self.play.moveObj(procLine[2].lower(),float(procLine[11]),float(procLine[12]),float(procLine[13]),float(procLine[14]))
                #readNextLine()
                return True
            if id == data.RemoveCombatant:
                self.play.removeObj(procLine[2])
                #readNextLine()
                return True
            if id == data.NetworkAbility: #can move target
                self.play.moveObj(procLine[2].lower(),float(procLine[40]),float(procLine[41]),float(procLine[42]),float(procLine[43]))
                if(procLine[2] != procLine[3]):
                    self.play.moveObj(procLine[6].lower(),float(procLine[30]),float(procLine[31]),float(procLine[32]),float(procLine[33]))
                return True
            if id == data.NetworkAOEAbility:
                self.play.moveObj(procLine[2].lower(),float(procLine[40]),float(procLine[41]),float(procLine[42]),float(procLine[43]))
                if(procLine[2] != procLine[3]):
                    self.play.moveObj(procLine[6].lower(),float(procLine[30]),float(procLine[31]),float(procLine[32]),float(procLine[33]))
                return True
            if id == data.NetworkDoT:
                self.play.moveObj(procLine[2].lower(),float(procLine[13]),float(procLine[14]),float(procLine[15]),float(procLine[16]))
                return True
            if id == data.NetworkEffectResult:
                self.play.moveObj(procLine[2].lower,float(procLine[11]),float(procLine[12]),float(procLine[13]),float(procLine[14]))
                return True
            if id == data.NetworkNameToggle:
                print(procLine[2].lower())
                temp = self.play.getObj(procLine[2].lower())
                if(bool(int(procLine[6]))):
                    temp.show()
                else:
                    temp.hide()
                
                return True
            if id == data.EOF:
                print("END OF FILE")
                return False
        except:
            if(data.log):
                print(procLine)
            return True
        print(procLine)
        print("NEW LINE")
