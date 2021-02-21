


import random
import sys

lst = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {lst}')

min_index_1 = 0
min_index_2 = 1

for i in lst:
    if lst[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = lst.index(i)
    elif lst[min_index_2] > i:
        min_index_2 = lst.index(i)

print(f'\nДва наименьших элемента: {lst[min_index_1]} и {lst[min_index_2]}')

print('\nРазмер списка:', sys.getsizeof(lst))
print('Размер элемента списка', sys.getsizeof(lst[0]))
print('Размер кортежа', sys.getsizeof(tuple(lst)))
print('Размер элемента кортежа', sys.getsizeof(tuple(lst)[0]))

sum = 0

for size in lst:
    sum += sys.getsizeof(size)

print('\nРазмер всех элементов в листе: ', sum, 'байт')

# Размер списка больше, чем неизменяемый кортеж, с одним набором данных
# (920 байт у списка против 840 у кортежа).
# Размер не зависит от разрядности чисел, но зависим от размера массива.
# Каждый элемент массива занимает 28 байт.
# 100 элементов по 28 байт занимают # 2800 байт, что значительно больше
# размера массива этих данных, т.к. Python делает оптимизацию и создаёт ссылки
# на один и тот же объект.