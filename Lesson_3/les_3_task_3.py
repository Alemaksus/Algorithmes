# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import random

N = 7
array = [0] * N
for i in range(N):
    array[i] = int(random() * 100)
    print(array[i], end=' ')
print()

mn = min(array)
mx = max(array)
imn = array.index(mn)
imx = array.index(mx)
print('arr[%d]=%d arr[%d]=%d' % (imn + 1, mn, imx + 1, mx))
array[imn], array[imx] = array[imx], array[imn]
