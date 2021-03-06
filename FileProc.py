import data
import linecache
import utility
class FileProc:

    def readNextLine(self):
        #line = log.readline()
        data.lineToRead = data.lineToRead + 1
        line = linecache.getline(data.fileName,data.lineToRead)
        line = line.split('|')
        return self.processLine(line)
    def setLineToRead(self, lineNum):
        data.lineToRead = lineNum
        print("47",data.lineToRead)
        self.map.clearObjs()
        return
    def processLine(self, procLine):
        try:
            id = procLine[0]
            if(id == data.notify):
                return True
            if(id != '00'):
                self.UI.updateTime(utility.strToDateTime(procLine[1]))
            if(data.log):
                print(procLine)

            if id in data.notUse:
                return True
            if id == data.ChangeZone:
                if(data.log):
                    print("moved to: ",procLine[3])
                self.map.clearObjs()
                self.map.LoadZone(procLine)
                return False
            if id == data.ChangePrimaryPlayer:
                return True
            if id == data.AddCombatant:
                self.map.addObj(procLine)
                return True
            if id == data.NetworkUpdateHP:
                self.map.moveObj(procLine[2].lower(),float(procLine[10]),float(procLine[11]),float(procLine[12]),float(procLine[13]))
                #self.play.UpdateObjStat(procLine[2].lower(),float(procLine[4]),float(procLine[5]),float(procLine[6]),float(procLine[7])) // not sure if accurte
                return True
            if id== data.NetworkStatusEffects:
                self.map.moveObj(procLine[2].lower(),float(procLine[11]),float(procLine[12]),float(procLine[13]),float(procLine[14]))
                self.map.UpdateObjStat(procLine[2].lower(),float(procLine[5]),float(procLine[6]),float(procLine[7]),float(procLine[8]))
                return True
            if id == data.RemoveCombatant:
                self.map.removeObj(procLine[2])
                return True
            if id == data.NetworkStartsCasting:
                self.map.castAbility(procLine[2].lower(),procLine[5],procLine[4],procLine[6],procLine[1], procLine[8])
                return True
            if id == data.NetworkAbility: #can move target
                self.map.hitAbility(procLine[2].lower(),procLine[5],procLine[4],procLine[6])
                self.map.moveObj(procLine[2].lower(),float(procLine[40]),float(procLine[41]),float(procLine[42]),float(procLine[43]))
                self.map.UpdateObjStat(procLine[2].lower(),float(procLine[34]),float(procLine[35]),float(procLine[36]),float(procLine[37]))
                if(procLine[2] != procLine[3]):
                    self.map.moveObj(procLine[6].lower(),float(procLine[30]),float(procLine[31]),float(procLine[32]),float(procLine[33]))
                    self.map.UpdateObjStat(procLine[6].lower(),float(procLine[24]),float(procLine[25]),float(procLine[26]),float(procLine[27]))
                return True
            if id == data.NetworkAOEAbility: # next to add end

                self.map.hitAbility(procLine[2].lower(),procLine[5], procLine[4], procLine[6])
                self.map.moveObj(procLine[2].lower(),float(procLine[40]),float(procLine[41]),float(procLine[42]),float(procLine[43]))
                self.map.UpdateObjStat(procLine[2].lower(),float(procLine[34]),float(procLine[35]),float(procLine[36]),float(procLine[37]))
                if(procLine[2] != procLine[3]):
                    self.map.moveObj(procLine[6].lower(),float(procLine[30]),float(procLine[31]),float(procLine[32]),float(procLine[33]))
                    self.map.UpdateObjStat(procLine[6].lower(),float(procLine[24]),float(procLine[25]),float(procLine[26]),float(procLine[27]))
                return True
            if id == data.NetworkDoT:
                self.map.moveObj(procLine[2].lower(),float(procLine[13]),float(procLine[14]),float(procLine[15]),float(procLine[16]))
                self.map.UpdateObjStat(procLine[2].lower(),float(procLine[7]),float(procLine[8]),float(procLine[9]),float(procLine[10]))
                return True
            if id == data.NetworkEffectResult:
                self.map.moveObj(procLine[2].lower,float(procLine[11]),float(procLine[12]),float(procLine[13]),float(procLine[14]))
                self.map.UpdateObjStat(procLine[2].lower(),float(procLine[5]),float(procLine[6]),float(procLine[7]),float(procLine[8]))
                return True
            if id == data.NetworkNameToggle:
                temp = self.map.getObj(procLine[2].lower())
                if(bool(int(procLine[6]))):
                    temp.show()
                else:
                    temp.hide()
                
                return True
            if id == data.NetworkBuff:
                self.map.gainBuff(procLine[5].lower(), procLine[3],procLine[2],procLine[7].lower(),procLine[4]) #9 buff info?
            if id == data.NetworkBuffRemove:
                print(procLine)
                self.map.removeBuff(procLine[5].lower(),procLine[3],procLine[2],procLine[7].lower())
            if id == data.EOF:
                print("END OF FILE")
                return False
        except:
            if(data.log):
                print(procLine)
            return True
        return True
        print(procLine)
        print("NEW LINE")
    def __init__(self, map, UI):
        self.UI = UI
        self.map = map
        self.UI.readLineEvt += self.readNextLine
        self.UI.setReadLineEvt += self.setLineToRead
