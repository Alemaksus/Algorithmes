# Разворот массива:

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

def revers(array):
    for i in range(len(array) // 2):
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]

revers(array)
print(array)

array.reverse()
print(array)

# встроенная сортировка:

array.sort(reverse=True) # - это одновременная сортировка и разворот массива.
print(array)

# сортировка кортежа:

print('*' * 50)
t = tuple(random.randint(0, 100) for _ in range(size))
print(t)

# t.sort() - этот способ сортировки не работает для кортежа
t = tuple(sorted(t, reverse=True)) # - зато этот работает
print(t)
