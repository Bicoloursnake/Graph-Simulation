from Digraph import Digraph

input : 'list[str]' = open("./matrix.csv", "r").read().split('\n')
inputMatrix : 'list[list[str]]' = []

digraph : Digraph = Digraph()
for i in range(len(input)):
    digraph.newVertex()
    inputMatrix.append(input[i].split(','))

for i in range(len(inputMatrix)):
    for j in range(len(inputMatrix[i])):
        for k in range(int(inputMatrix[i][j])):
            digraph.newArc(digraph.getVertices()[i], digraph.getVertices()[j])

print(digraph.containsALoop())
print(digraph.getAdjacencyMatrix())


