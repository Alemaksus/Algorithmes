# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

from random import random

N = 7
array = []
for i in range(N):
    array.append(int(random() * 100) - 50)
print(array)

i = 0
index = -1
while i < N:
    if array[i] < 0 and index == -1:
        index = i
    elif array[i] < 0 and array[i] > array[index]:
        index = i
    i += 1

print("Максимальный отрицательный элемент:", array[index], ', с индексом:', index + 1)