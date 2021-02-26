from collections import namedtuple

# Список смежности ненаправленного графа:

graph = []

graph.append([1, 2])
graph.append([0, 2, 3])
graph.append([0, 1])
graph.append([1])

print(*graph, sep='\n')

# Словарь ненаправленного графа:

print('*' * 50)

graph_2 = {
    0: {1, 2},
    1: {0, 2, 3},
    2: {0, 1},
    3: {1}
}

print(graph_2)

if 2 in graph_2[1]:
    print(True)

# Список смежности взвешенного графа:
print('*' * 50)
Vertex = namedtuple('Vertex', ['vertex', 'edge'])
graph_3 = []

graph_3.append([Vertex(1, 2), Vertex(2, 3)])
graph_3.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
graph_3.append([Vertex(0, 3), Vertex(1, 2)])
graph_3.append([Vertex(1, 1)])

print(*graph_3, sep='\n')

for v in graph_3[1]:
    if v.vertex == 3:
        print(True)

# Пример хранение графов в виде классов:

class Graph:
    def __init__(self, vertex, edge, spam): # spam - дополнительная переменная, которая легко вписывается в класс
        self.vertex = vertex
        self.edge = edge
        self.spam = spam
