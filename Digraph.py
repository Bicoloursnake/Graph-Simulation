from Vertex import Vertex
from Arc import Arc
class Digraph:

    def __init__(self):
        self.Vertices : 'list[Vertex]' = []
        self.Arcs : 'list[Arc]' = []

    def newVertex(self):
        v : Vertex = Vertex()
        self.Vertices.append(v)

    def newArc(self, tail: Vertex, head: Vertex, weight : int = 1):
        tail.addArc(head)
        self.Arcs.append(Arc(tail,head,weight))

    def printDigraphCSV(self):
        outputStr : str = ''
        for i in self.Vertices:
            for j in self.Vertices:
                arcCount : int = 0
                if j in i.Heads:
                    outputStr += str(i.arcCount[i.Heads.index(j)]) + ','
                else:
                    outputStr += '0,'
            outputStr = outputStr[0:len(outputStr)-1]
            outputStr += '\n'
        outputStr = outputStr[0:len(outputStr)-1]
        print(outputStr)

    def getVertices(self) -> 'list[Vertex]':
        return self.Vertices