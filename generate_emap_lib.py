from emap import Emap
from node import EmapNodeType

def generateEmap( w, h, h_walls, v_walls, tile_width,tile_height,wall_height):

    emap = Emap(tile_width,tile_height,wall_height)
    emap.addSkybox()

    def getNodePos(x,y):
        return "%d,0,%d" % (x*tile_width+5,y*tile_height+5)

    def getLightPos(x,y):
        return "%d,7,%d" % (x*tile_width+5,y*tile_height+5)


    for x in range(w+1):
        for y in range(h+1):

            if h_walls[y*w+x]==1:
                emap.addH_Wall(x,y)

            if v_walls[y*w+x]==1:
                emap.addV_Wall(x,y)

            if(x<w and y<h):
                emap.addFloor(x,y)
                if (x+y)%2==0:
                    emap.addNode(EmapNodeType.Health_Small, getNodePos(x,y), {})
                else:
                    emap.addNode(EmapNodeType.Ammo_Bullets_Small, getNodePos(x,y), {})

                if(x==0 and y==0):
                    emap.addNode(EmapNodeType.Player, getNodePos(x,y), {})
                    emap.addNode(EmapNodeType.Weapon_Pistol, getNodePos(x,y), {})
                    emap.addNode(EmapNodeType.Weapon_Shotgun, getNodePos(x,y), {})
                    emap.addNode(EmapNodeType.Weapon_SMG, getNodePos(x,y), {})
                    #emap.addNode(EmapNodeType.Weapon_Mammoth, getNodePos(x,y), {})
                    #emap.addNode(EmapNodeType.Weapon_AutoShotgun, getNodePos(x,y), {})
                    emap.addNode(EmapNodeType.AutoMap, getNodePos(x,y), {})
                elif(x==1 and y==0):
                    emap.addNode(EmapNodeType.Weapon_Plexus, getNodePos(x,y), {})
                elif(x==0 and y==1):
                    emap.addNode(EmapNodeType.Weapon_SuperShotgun, getNodePos(x,y), {})
                elif(x==1 and y==1):
                    emap.addNode(EmapNodeType.Weapon_RocketLauncher, getNodePos(x,y), {})
                elif(x%5==0 and y%5==0):
                    lightExtras = {
                        "isOn":"True",
                        "range":"50",
                        "color":"1,1,1,1",
                        "intensity":"1",
                        "type":"2",
                        "spotAngle":"30",
                        "shadows":"False",
                        "flickerTime":"1",
                        "loop":"True",
                        "isSun":"False",
                    }
                    emap.addNode(EmapNodeType.Light, getLightPos(x,y), lightExtras)
                    emap.addNode(EmapNodeType.Ammo_Shells_Large, getNodePos(x,y), {})
                    emap.addNode(EmapNodeType.getRandomMiddleMonster(), getNodePos(x,y), {})
                elif(x==9 and y==9):
                    emap.addNode(EmapNodeType.LevelEnd, getNodePos(x,y), {}) # TODO: this needs a trigger
                elif(x>7 and y>7):
                    emap.addNode(EmapNodeType.getRandomBigMonster(), getNodePos(x,y), {})
                else:
                    emap.addNode(EmapNodeType.getRandomSmallMonster(), getNodePos(x,y), {})
    return emap