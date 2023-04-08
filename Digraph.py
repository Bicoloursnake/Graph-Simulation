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
        a : Arc = Arc(tail, head, weight)
        tail.addArc(a)
        self.Arcs.append(a)

    def getVertices(self) -> 'list[Vertex]':
        return self.Vertices
    
    def getAdjacencyMatrix(self) -> 'list[list[int]]':
        adjMatrix : 'list[list[int]]' = []
        for x in range(len(self.Vertices)):
            adjMatrix.append([])
            for y in range(len(self.Vertices)):
                adjMatrix[x].append(0)
        for i in self.Vertices:
            for a in i.Heads:
                adjMatrix[self.Vertices.index(i)][self.Vertices.index(a.head)] += 1
        return adjMatrix
    
    def containsALoop(self) -> bool:
        for v in self.getVertices():
            for a in v.Heads:
                if a.isLoop():
                    return True
        return False