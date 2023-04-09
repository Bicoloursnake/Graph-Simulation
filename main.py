from Digraph import Digraph

input : 'list[str]' = open("./matrix.csv", "r").read().split('\n')
inputMatrixStr : 'list[list[str]]' = []
for i in range(len(input)):
    inputMatrixStr.append(input[i].split(','))

inputMatrix : 'list[list[int]]' = [[int(j) for j in i] for i in inputMatrixStr]



print(Digraph(inputMatrix))