import random


class EmapNodeType:
    Player = "Player"
    AutoMap = "AutoMap"
    Light="Light"
    LevelEnd="LevelEnd"

    Weapon_Pistol   = "Weapon_Pistol"
    Weapon_SMG="Weapon_SMG"
    Weapon_Minigun  = "Weapon_Minigun"
    Weapon_Shotgun = "Weapon_Shotgun"
    Weapon_SuperShotgun="Weapon_SuperShotgun"
    Weapon_AutoShotgun="Weapon_AutoShotgun"
    Weapon_ArcRail  = "Weapon_ArcRail"
    Weapon_ChaosCaster  = "Weapon_ChaosCaster"
    Weapon_GrenadeLauncher  = "Weapon_GrenadeLauncher"
    Weapon_RocketLauncher   = "Weapon_RocketLauncher"
    Weapon_PlasmaRifle  = "Weapon_PlasmaRifle"
    Weapon_Plexus   = "Weapon_Plexus"
    Weapon_Mammoth   = "Weapon_Mammoth"

    Armor_Large="Armor_Large"

    Ammo_Bullets_Small="Ammo_Bullets_Small"
    Ammo_Bullets_Large="Ammo_Bullets_Large"
    Ammo_Shells_Small="Ammo_Shells_Small"
    Ammo_Shells_Large="Ammo_Shells_Large"
    Health_Small="Health_Small"

    Zombie = "Zombie"
    ZombieHazmat = "ZombieHazmat"
    ZombieHeavy_Minigun = "ZombieHeavy_Minigun"
    ZombieSniper = "ZombieSniper"
    Soldier_Shotgun = "Soldier_Shotgun"
    Cryomancer = "Cryomancer"
    Harbinger = "Harbinger"
    Phantom = "Phantom"
    Bloater = "Bloater"
    Monster_Crawler = "Monster_Crawler"
    Fiend = "Fiend"
    Monster_Hunter = "Monster_Hunter"
    Lunger = "Lunger"
    SkullFish = "SkullFish"
    Monster_Slayer = "Monster_Slayer"
    VoidReaper = "VoidReaper"

    Monster_SkullFishPro = "Monster_SkullFishPro"
    Monster_FiendPro = "Monster_FiendPro"
    Monster_CrawlerPro = "Monster_CrawlerPro"

    smallMonsterNames = [
        Zombie,
        ZombieHazmat,
        Soldier_Shotgun,
        SkullFish,
        Monster_Crawler,
        Fiend,
    ]
    middleMonsterNames = [
        Lunger,
        ZombieHeavy_Minigun,
        ZombieSniper,
        Bloater,
    ]
    bigMonsterNames = [
        Harbinger,
        Cryomancer,
        Phantom,
        Monster_Hunter,
        Monster_Slayer,
        VoidReaper,
    ]

    def getRandomSmallMonster():
        return random.choice(EmapNodeType.smallMonsterNames)

    def getRandomMiddleMonster():
        return random.choice(EmapNodeType.middleMonsterNames)

    def getRandomBigMonster():
        return random.choice(EmapNodeType.bigMonsterNames)


idCounter=0

class Node:
    def __init__(self, type, pos, extras):
        global idCounter
        idCounter += 1
        self.id = idCounter
        self.type = type
        self.nodeName = type
        self.pos = pos
        self.extras = extras
        self.rotation = "0,0,0"
        self.layer = -1
        self.parent = -1

    def getNodeText(self):
        s = ""
        s+="Node{\n"
        s+=self.type +"\n"
        for extra in self.extras:
            s+=extra + "=" + self.extras[extra] +"\n"
        s+="pos=" + self.pos +"\n"
        s+="rotation=" + self.rotation +"\n"
        
        s+="id=" + str(self.id) +"\n"
        s+="layer=" + str(self.layer) +"\n"
        s+="parent=" + str(self.parent) +"\n"
        s+="nodeName=" + str(self.nodeName) +"\n"
        s+="}\n"
        return s

#player extra       
#giveFists=True
#slowFadeIn=False
#startNoHud=False
#enableRespawn=False

# monster extras
#startTriggered=True
##useEffect=False
#stationary=False
#delayMin=0
#delayMax=0
#invisible=False
#invisibleHealth=50

#Armor_Large
#Ammo_Bullets_Large
#Ammo_Shells_Large
#startSpawned=True
#triggerEverySpawn=True
#triggerEachPlayer=False

#Key_Blue
#Rune
#startSpawned=True
#showGhost=True
#runeID=a3966ae7b13ca21b10205ef560b4573f0b73fbc2

#LevelEnd
#isSecret=False
#loadNextLevel=False
#pos=5,0,5

#Func_GiveItems
#health=0
#armor=0
#ammo=0
#ammoType=0
#key=0
#weaponID=22
#weaponID=52
#filterType=2
#entityFilter=players,chaos,prodeus,elder,noteam,key_none
#entityCollection=-1

"""
Node{
Func_Trigger
isOn=True
triggerSize=2,4,2
disOnEnt=False
disOnExit=False
disOnLastExit=False
lastOutDelay=0
entityFilterEnter=players,chaos,prodeus,elder,noteam,key_none
entityFilterExit=players,chaos,prodeus,elder,noteam,key_none
pos=5,1.75,5
rotation=0,0,0
id=7
layer=-1
parent=-1
targetStructs=OnFirstEnter,Activate,8
nodeName=Trigger(Clone)
}
Node{
LevelEnd
isSecret=False
loadNextLevel=False
pos=5,0,5
rotation=0,0,0
id=8
layer=-1
parent=-1
nodeName=LevelEnd(Clone)
}
"""