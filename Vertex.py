import Vertex
class Vertex:
    def __init__(self):
        self.Heads : 'list[Vertex]' = []
        self.arcCount : 'list[int]' = []
        self.Tails : 'list[Vertex]' = []

    def addArc(self, v : Vertex) -> None:
        if v in self.Heads:
            self.arcCount[self.Heads.index(v)] += 1
        else:
            self.Heads.append(v)
            self.arcCount.append(1)
            v.Tails.append(self)
    
    def removeArc(self, v : Vertex) -> None:
        if v in self.Heads:
            if self.arcCount[self.Heads.index(v)] == 1:
                self.arcCount.pop(self.Heads.index(v))
                self.Heads.remove(v)
                v.Tails.remove(self)
            else:
                self.arcCount[self.Heads.index(v)] -= 1
        else:
            print('Fool! There is no arc to remove!')
    
    def getOutDegree(self) -> int:
        degreeSum : int = 0
        for i in self.arcCount:
            degreeSum += i
        return degreeSum
    
    def getInDegree(self) -> int:
        degreeSum : int = 0
        for v in self.Tails:
            degreeSum += v.arcCount[v.Heads.index(self)]
        return degreeSum    