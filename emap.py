from header import header_text;
from brush import Brush;

class Emap:
    def __init__(self):
        self.materials = [
            "Blockout",
            "Industrial/Cement01_GenFull",
            "SciFi/PanelDetail_GenFull"
        ]
        self.brushes = []

    def addBrush(self, verts, uvArray, trisArray, materialNr=0):
        self.brushes.append(Brush(verts, uvArray, trisArray, materialNr))

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
