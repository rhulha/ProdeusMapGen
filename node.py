
class EmapType:
    Player = "Player"
    Zombie = "Zombie"
    ZombieHazmat = "ZombieHazmat"
    Weapon_Shotgun = "Weapon_Shotgun"
    Weapon_SuperShotgun="Weapon_SuperShotgun"

idCounter=0

class Node:
    def __init__(self, type, nodeName, pos="0,0,0", rotation="0,0,0", layer=-1, parent=-1):
        global idCounter
        idCounter += 1
        self.id = idCounter
        self.type = type
        self.nodeName = nodeName
        self.pos = pos
        self.rotation = rotation
        self.layer = layer
        self.parent = parent

    def printNode(self):

#player extra       
#giveFists=True
#slowFadeIn=False
#startNoHud=False
#enableRespawn=False

#pos=74,0,4.75
#nodeName=PlayerStart(Clone)
#}

#
#startTriggered=True
#useEffect=False
#stationary=False
#delayMin=0
#delayMax=0
#invisible=False
#invisibleHealth=50
#pos=84.5,0,15.75
#rotation=0,0,0
#id=238
#layer=-1
#parent=-1
#nodeName=Zombie(Clone)
#}

#Node{
#
#startTriggered=True
##useEffect=False
#stationary=False
#delayMin=0
#delayMax=0
#invisible=False
#invisibleHealth=50
#pos=95,0,5.5

#startSpawned=True
#triggerEverySpawn=True
#triggerEachPlayer=False
#pos=68.25,0,4.5

##startSpawned=True
#triggerEverySpawn=True
#triggerEachPlayer=False
#pos=57.25,0,4
