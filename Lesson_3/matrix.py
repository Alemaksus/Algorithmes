import random
# Проще всего создать матрицу вложением одного генератора списка в другой:

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()