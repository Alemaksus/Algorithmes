# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

import cProfile
import timeit


def Eratos(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve


def Alterfunc(n):
    f = []
    for i in range(2, n):
        result = True
        for j in range(2, i):
            if i % j == 0:
                result = False
        if result:
            f.append(i)
    return f

cProfile.run("Eratos(10000)")

# 1233 function calls in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#      1    0.001    0.001    0.001    0.001 les_4_task_2.py:13(Eratos)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#   1229    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run("Alterfunc(10000)")

# 1233 function calls in 1.701 seconds
#
# Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.701    1.701 <string>:1(<module>)
#         1    1.701    1.701    1.701    1.701 les_4_task_2.py:23(Alterfunc)
#         1    0.000    0.000    1.701    1.701 {built-in method builtins.exec}
#      1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод: Функция Eratos в 1700 раз быстрее варианта Alterfunc