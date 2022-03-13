import json
from emap import Emap

def loadJSON(filename):
    with open(filename) as f:
        return json.load(f)

h_walls=loadJSON("h_walls.json")
v_walls=loadJSON("v_walls.json")
w=10
h=10
tile_width=10
tile_height=10
wall_height=10

emap = Emap()

def addFloor(x,y):
    # we pretent we look from above
    topLeft="%s,%s,%s" % (x*tile_width,0,y*tile_height)
    topRight="%s,%s,%s" % ((x+1)*tile_width,0,y*tile_height)
    botLeft="%s,%s,%s" % (x*tile_width,0,(y+1)*tile_height)
    botRight="%s,%s,%s" % ((x+1)*tile_width,0,(y+1)*tile_height)
    uvTopLeft="0,0"
    uvTopRight="1,0"
    uvBotLeft="0,1"
    uvBotRight="1,1"
    verts="%s;%s;%s;%s" % (topLeft,topRight,botLeft,botRight)
    #uvs="%s;%s;%s;%s" % (uvTopLeft,uvTopRight,uvBotLeft,uvBotRight)
    trisArray=[0,2,3,1] # counter clock wise
    emap.addBrush(verts, [uvTopLeft,uvTopRight,uvBotLeft,uvBotRight], trisArray, 1)

def addH_Wall(x,y):
    # we pretent we look from the side
    topLeft="%s,%s,%s" % (x*tile_width,wall_height,y*tile_height)
    topRight="%s,%s,%s" % ((x+1)*tile_width,wall_height,y*tile_height)
    botLeft="%s,%s,%s" % (x*tile_width,0,y*tile_height)
    botRight="%s,%s,%s" % ((x+1)*tile_width,0,y*tile_height)
    uvTopLeft="0,0"
    uvTopRight="1,0"
    uvBotLeft="0,1"
    uvBotRight="1,1"
    verts="%s;%s;%s;%s" % (topLeft,topRight,botLeft,botRight)
    #uvs="%s;%s;%s;%s" % (uvTopLeft,uvTopRight,uvBotLeft,uvBotRight)
    trisArray=[0,2,3,1] # counter clock wise
    emap.addBrush(verts, [uvTopLeft,uvTopRight,uvBotLeft,uvBotRight], trisArray, 2)

def addV_Wall(x,y):
    # we pretent we look from the side
    topLeft="%s,%s,%s" % (x*tile_width,wall_height,(y+1)*tile_height)
    topRight="%s,%s,%s" % (x*tile_width,wall_height,y*tile_height)
    botLeft="%s,%s,%s" % (x*tile_width,0,(y+1)*tile_height)
    botRight="%s,%s,%s" % (x*tile_width,0,y*tile_height)
    uvTopLeft="0,0"
    uvTopRight="1,0"
    uvBotLeft="0,1"
    uvBotRight="1,1"
    verts="%s;%s;%s;%s" % (topLeft,topRight,botLeft,botRight)
    #uvs="%s;%s;%s;%s" % (uvTopLeft,uvTopRight,uvBotLeft,uvBotRight)
    trisArray=[0,2,3,1] # counter clock wise
    emap.addBrush(verts, [uvTopLeft,uvTopRight,uvBotLeft,uvBotRight], trisArray, 2)


for x in range(w+1):
    for y in range(h+1):
        if(x<w and y<h):
            addFloor(x,y)
        if h_walls[y*w+x]==1:
            addH_Wall(x,y)
        if v_walls[y*w+x]==1:
            addV_Wall(x,y)

emap.printMap()
