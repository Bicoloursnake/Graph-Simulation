from Digraph import Digraph
from Vertex import Vertex

class Graph(Digraph):
    def __init__(self) -> None:
        self.underlyingDigraph : Digraph = Digraph()

    def newEdge(self, u: Vertex, v: Vertex, weight: int = 1) -> None:
        self.underlyingDigraph.newArc(u,v,weight)
        self.underlyingDigraph.newArc(v,u,weight)