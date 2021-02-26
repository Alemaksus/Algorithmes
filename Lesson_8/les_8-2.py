# Доработать алгоритм Дейкстры так, чтобы он дополнительно
# возвращал список вершин, которые необходимо обойти.

from collections import deque

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 1],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

def dijkstra(graph, start):

    length = len(graph)

    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    tops = []
    for i in range(length):
        j = i
        top = [i]
        while parent[j] != -1:
            top.append(parent[j])
            j = parent[j]
        tops.append(top)

    return cost, tops

s = int(input('От какой вершины идти: '))
result = dijkstra(g, s)
print(f'Стоимость путей до каждой вершины {result[0]}')
print(f'Списки вершин, которые нужно обойти {result[1]}')