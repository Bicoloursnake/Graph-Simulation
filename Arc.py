from Vertex import Vertex
class Arc:
    weight : int
    def __init__(self, tail: Vertex, head: Vertex, weight : int = 1) -> None:
        self.tail : Vertex = tail
        self.head : Vertex = head
        self.weight = weight

    def isLoop(self) -> bool:
        return self.tail == self.head
        