import json
from generate_emap_lib import generateEmap

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

emap = generateEmap(w, h, h_walls, v_walls, tile_width, tile_height, wall_height)

emap.writeMap("C:\\Users\\Ray\\AppData\\LocalLow\\BoundingBoxSoftware\\Prodeus\\LocalData\\Maps\\aaa.emap")
