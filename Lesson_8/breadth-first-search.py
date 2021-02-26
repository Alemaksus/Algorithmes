# Поиск кратчайшего пути в ширину:

from collections import deque

g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]

def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))] # - здесь хранится родитель для каждой вершины
    is_visited = [False for _ in range(len(graph))] # - здесь хранится True (посетили) или False (ещё нет)

    deg = deque([start])
    is_visited[start] = True

    while len(deg) > 0:
        current = deg.pop()
        if current == finish:
            # return parent
            break

        for i, vertex in enumerate(graph[current]):
            if vertex == 1 and not is_visited[i]:

                is_visited[i] = True
                parent[i] = current
                deg.appendleft(i)
    else:
        return f'Из вершины {start} нельзы попасть в вершину {finish}'

    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return f'кратчайший путь {list(way)} длинной в {cost} условных единиц'

s = int(input('От какой вершины идти: '))
f = int(input('До какой вершины идти: '))
print(bfs(g, s, f))