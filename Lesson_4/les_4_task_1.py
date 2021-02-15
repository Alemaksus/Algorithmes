# Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.

import cProfile
import timeit
from random import random

def myArrow():
    N = 14
    arrow = []
    for i in range(N):
        arrow.append(int(random() * 100))

    indexMin = arrow.index(min(arrow))
    indexMax = arrow.index(max(arrow))
    minMy = min(arrow)
    maxMy = max(arrow)

    arrow[indexMin] = maxMy
    arrow[indexMax] = minMy
    return arrow

def myArrow2():
    N = 14
    arrow = []
    for i in range(N):
        arrow.append(int(random() * 100))
    arrow.sort()

    minMy = arrow[0]
    maxMy = arrow[-1]

    arrow[0] = maxMy
    arrow[-1] = minMy
    return arrow

# print(timeit.timeit(myArrow))
# Результат: 2.7984501

# print(timeit.timeit(myArrow2))
# Результат: 2.0800923

#  "les_4_task_1.m
# yArrow"
# 2.7523938
# 2.0264723
# 1000 loops, best of 5: 19.4 nsec per loop

# Вывод: Скорость обработки функции myArrow2 выше чем у myArrow
# за счет применения метода sort ~ 720 usec.