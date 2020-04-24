NetworkEffectResult = '37' #Hex 25
NetworkStatusEffects = '38' #Hex 26
NetworkUpdateHP = '39' #Hex 27
NetworkAbility = '21' #Hex 15
NetworkAOEAbility = '22' #Hex 16 same info as NetworkAbility
NetworkDoT = '24' #Hex 18
NetworkNameToggle = '34' #Hex 22 work out if nameplate is visible
ChangeZone = '01' #Hex 01 - use to work out what zone are in
ChangePrimaryPlayer = '02' # Hex 02  - use to work out name of YOU
AddCombatant = '03' #Hex 03 - called when ever a new object is added to the scene
RemoveCombatant = '04' #Hex 04 - called when ever a Object is removed from scene
EOF = ''
notUse = ['00', '11','12','20','23','25','26','27','29','30','31','33','35','36','249','250','251','253'] 
#33 is used for misc zone commands inc wipes
#34 can be used to see if a mob is targetable
#35 network teather
#36 limit break count up

#playerOffset = [100, -258] # x,y
playerOffset = [100, 100] # x,y
LookPos = [100,100]
scale = 10
log = False
center = [0,0]
fileName = "log.log"
lineToRead = 0
playSpeed = 0.01
trace = None
go = False