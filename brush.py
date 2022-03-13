class Brush:
    def __init__(self, verts, uvArray, trisArray, materialNr=0):
        self.verts = verts
        self.uvArray = uvArray
        self.trisArray = trisArray
        self.materialNr = materialNr

    def printBrush(self):
        tris=";".join([str(e) for e in self.trisArray])
        tris2=";".join([str(e) for e in reversed(self.trisArray)])
        uvs=""
        for x in range(len(self.trisArray)):
            uvs+="%s;" % self.uvArray[self.trisArray[x]]
        uvs2=""
        self.trisArray.reverse()
        for x in range(len(self.trisArray)):
            uvs2+="%s;" % self.uvArray[self.trisArray[x]]
        print(brush_text % (self.verts,self.materialNr,tris,uvs,self.materialNr,tris2,uvs2))

# mappingType=0 == World
# mappingType=2 == HotSpot

brush_text="""Brush{
parent=-1
layer=-1
pos=0,0,0
smooth=False
points=%s
edges=
Face{
surf={
localMapping=False
mappingType=2
material=%d
color=0
colorEmissive=0
seed=843
halfRes=False
uvScaleBias=1,1,0,0
uvScroll=0,0
localOffset=0,0,0
worldOffset=0,0,0
uvRotation=0
uvFlipH=False
uvFlipV=False
}
points=%s
uvs=%s
}
Face{
surf={
localMapping=False
mappingType=2
material=%d
color=0
colorEmissive=0
seed=843
halfRes=False
uvScaleBias=1,1,0,0
uvScroll=0,0
localOffset=0,0,0
worldOffset=0,0,0
uvRotation=0
uvFlipH=False
uvFlipV=False
}
points=%s
uvs=%s
}
}
"""
