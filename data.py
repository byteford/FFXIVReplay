NetworkEffectResult = '37' #Hex 25
NetworkStatusEffects = '38' #Hex 26
NetworkUpdateHP = '39' #Hex 27
NetworkStartsCasting = '20' #Hex 14
NetworkAbility = '21' #Hex 15
NetworkAOEAbility = '22' #Hex 16 same info as NetworkAbility
NetworkDoT = '24' #Hex 18
NetworkNameToggle = '34' #Hex 22 work out if nameplate is visible
ChangeZone = '01' #Hex 01 - use to work out what zone are in
ChangePrimaryPlayer = '02' # Hex 02  - use to work out name of YOU
AddCombatant = '03' #Hex 03 - called when ever a new object is added to the scene
RemoveCombatant = '04' #Hex 04 - called when ever a Object is removed from scene
NetworkBuff = '26' #Hex 1A - called when someone gets a buff
NetworkBuffRemove = '30' #Hex 1E -called when someone looses a buf
NetworkCancelAbility = '23' #Hex 17 - Netowork cancel ability
NetworkGauge = '31' #Hex 1F - Player Job gauge infomation
LimitBreak = '36' #Hex 24 - limit break count up
EOF = ''
notify= '00'
notUse = ['11','12','25','27','29','33','35','249','250','251','253'] 
#11 Hex B - Lists Party ids
#12 Hex C - Players stats
#25 Hex 19 - NetworkDeath - when omeone dies
#27 Hex 1B- NetworkTargetIcon (headMarkers) [6] = '0060' e8s drop markers '0057' spread?
#33 Hex 21 - Network6D is used for misc zone commands inc wipes 40000001 = lock out in seconds, 80000004 = tockout time adjuct
#34 can be used to see if a mob is targetable
#35 network teather

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
zoneID = 0
