import random

class EmapNodeType:
    Player = "Player"
    Weapon_Shotgun = "Weapon_Shotgun"
    Weapon_SuperShotgun="Weapon_SuperShotgun"
    Light="Light"
    Armor_Large="Armor_Large"
    Ammo_Bullets_Large="Ammo_Bullets_Large"
    Ammo_Shells_Large="Ammo_Shells_Large"
    Health_Small="Health_Small"
    Weapon_Pistol="Weapon_Pistol"
    Weapon_SMG="Weapon_SMG"
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

    smallMonsterNames = [
        Zombie,
        ZombieHazmat,
        ZombieHeavy_Minigun,
        Soldier_Shotgun,
        Cryomancer,
        Harbinger,
    ]
    bigMonsterNames = [
        ZombieSniper,
        Phantom,
        Bloater,
        Monster_Crawler,
        Fiend,
        Monster_Hunter,
        Lunger,
        SkullFish,
        Monster_Slayer,
        VoidReaper,
    ]

    def getRandomSmallMonster():
        return random.choice(EmapNodeType.smallMonsterNames)

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

    def printNode(self):
        print("Node{")
        print(self.type)
        for extra in self.extras:
            print(extra + "=" + self.extras[extra])
        print("pos=" + self.pos)
        print("rotation=" + self.rotation)
        print("id=" + str(self.id))
        print("layer=" + str(self.layer))
        print("parent=" + str(self.parent))
        print("nodeName=" + str(self.nodeName))
        print("}")

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
#pos=95,0,5.5

#Armor_Large
#Ammo_Bullets_Large
#Ammo_Shells_Large
#Health_Small
#Weapon_Pistol
#Weapon_SMG
#startSpawned=True
#triggerEverySpawn=True
#triggerEachPlayer=False
