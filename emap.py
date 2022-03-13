from header import header_text
from brush import Brush
from node import Node

class Emap:
    def __init__(self, tile_width, tile_height, wall_height):
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.wall_height = wall_height
        self.materials = [
            "Blockout",
            "Skybox/Asteroid_Surface",
            "Industrial/Cement01_GenFull",
            "SciFi/PanelDetail_GenFull"
        ]
        self.brushes = []
        self.nodes = []

        self.skyMaterial = 1
        self.floorMaterial = 2
        self.wallMaterial = 3

    def addSkybox(self):
        topLeft="%s,%s,%s" % (0,self.wall_height,0)
        topRight="%s,%s,%s" % (100,self.wall_height,0)
        botLeft="%s,%s,%s" % (0,self.wall_height,100)
        botRight="%s,%s,%s" % (100,self.wall_height,100)
        uvTopLeft="0,0"
        uvTopRight="1,0"
        uvBotLeft="0,1"
        uvBotRight="1,1"
        verts="%s;%s;%s;%s" % (topLeft,topRight,botLeft,botRight)
        #uvs="%s;%s;%s;%s" % (uvTopLeft,uvTopRight,uvBotLeft,uvBotRight)
        trisArray=[0,2,3,1] # counter clock wise
        self.addBrush(verts, [uvTopLeft,uvTopRight,uvBotLeft,uvBotRight], trisArray, self.skyMaterial)

    def addBrush(self, verts, uvArray, trisArray, materialNr=0):
        self.brushes.append(Brush(verts, uvArray, trisArray, materialNr))

    def addNode(self, type, pos, extras):
        self.nodes.append(Node(type, pos, extras))

    def addFloor(self, x,y):
        # we pretent we look from above
        topLeft="%s,%s,%s" % (x*self.tile_width,0,y*self.tile_height)
        topRight="%s,%s,%s" % ((x+1)*self.tile_width,0,y*self.tile_height)
        botLeft="%s,%s,%s" % (x*self.tile_width,0,(y+1)*self.tile_height)
        botRight="%s,%s,%s" % ((x+1)*self.tile_width,0,(y+1)*self.tile_height)
        uvTopLeft="0,0"
        uvTopRight="1,0"
        uvBotLeft="0,1"
        uvBotRight="1,1"
        verts="%s;%s;%s;%s" % (topLeft,topRight,botLeft,botRight)
        #uvs="%s;%s;%s;%s" % (uvTopLeft,uvTopRight,uvBotLeft,uvBotRight)
        trisArray=[0,2,3,1] # counter clock wise
        self.addBrush(verts, [uvTopLeft,uvTopRight,uvBotLeft,uvBotRight], trisArray, self.floorMaterial)

    def addH_Wall(self, x,y):
        # we pretent we look from the side
        topLeft="%s,%s,%s" % (x*self.tile_width,self.wall_height,y*self.tile_height)
        topRight="%s,%s,%s" % ((x+1)*self.tile_width,self.wall_height,y*self.tile_height)
        botLeft="%s,%s,%s" % (x*self.tile_width,0,y*self.tile_height)
        botRight="%s,%s,%s" % ((x+1)*self.tile_width,0,y*self.tile_height)
        uvTopLeft="0,0"
        uvTopRight="1,0"
        uvBotLeft="0,1"
        uvBotRight="1,1"
        verts="%s;%s;%s;%s" % (topLeft,topRight,botLeft,botRight)
        #uvs="%s;%s;%s;%s" % (uvTopLeft,uvTopRight,uvBotLeft,uvBotRight)
        trisArray=[0,2,3,1] # counter clock wise
        self.addBrush(verts, [uvTopLeft,uvTopRight,uvBotLeft,uvBotRight], trisArray, self.wallMaterial)

    def addV_Wall(self, x,y):
        # we pretent we look from the side
        topLeft="%s,%s,%s" % (x*self.tile_width,self.wall_height,(y+1)*self.tile_height)
        topRight="%s,%s,%s" % (x*self.tile_width,self.wall_height,y*self.tile_height)
        botLeft="%s,%s,%s" % (x*self.tile_width,0,(y+1)*self.tile_height)
        botRight="%s,%s,%s" % (x*self.tile_width,0,y*self.tile_height)
        uvTopLeft="0,0"
        uvTopRight="1,0"
        uvBotLeft="0,1"
        uvBotRight="1,1"
        verts="%s;%s;%s;%s" % (topLeft,topRight,botLeft,botRight)
        #uvs="%s;%s;%s;%s" % (uvTopLeft,uvTopRight,uvBotLeft,uvBotRight)
        trisArray=[0,2,3,1] # counter clock wise
        self.addBrush(verts, [uvTopLeft,uvTopRight,uvBotLeft,uvBotRight], trisArray, self.wallMaterial)


    def printMap(self):
        print(header_text)
        print("Materials{")
        for material in self.materials:
            print(material)
        print("}")

        print("Brushes{")
        for brush in self.brushes:
            brush.printBrush()
        print("}")

        print("Nodes{")
        for node in self.nodes:
            node.printNode()
        print("}")
