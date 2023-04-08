import Vertex
from Arc import Arc
class Vertex:
    def __init__(self):
        self.Heads : 'list[Arc]' = []
        self.Tails : 'list[Arc]' = []

    def addArc(self, a : Arc) -> None:
        self.Heads.append(a)
        a.tail.Tails.append(self)
    
    def removeArc(self, a : Arc) -> None:
        self.Heads.remove(a)
        a.tail.Tails.remove(a)
    
    def getOutDegree(self) -> int:
        return len(self.Heads)
    
    def getInDegree(self) -> int:
        return len(self.Tails) 