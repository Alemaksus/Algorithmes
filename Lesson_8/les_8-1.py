# На улице встретились N друзей. Каждый пожал руку всем остальным
# друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

from functools import reduce

f = int(input('Сколько вас было: '))
graph = [[int(i > j) for i in range(f)] for j in range(f)]
count = reduce(lambda acc, x: acc + sum(x), graph, 0)
print(f'Получилось {count} рукопожатий')