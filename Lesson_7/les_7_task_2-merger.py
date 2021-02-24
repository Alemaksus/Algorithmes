# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

size = 10
min_el = 0
max_el = 51
array = [random.randint(min_el, max_el) for _ in range(size)]

def fusion_sort(arr):

    def merger(fst_el, snd_el):
        result = []
        i, j = 0, 0

        while i < len(fst_el) and j < len(snd_el):

            if fst_el[i] < snd_el[j]:
                result.append(fst_el[i])
                i += 1

            else:
                result.append(snd_el[j])
                j += 1

        result.extend(fst_el[i:] if i < len(fst_el) else snd_el[j:])

        return result

    def div_half(lst_el):

        if len(lst_el) == 1:
            return lst_el

        elif len(lst_el) == 2:
            return lst_el if lst_el[0] <= lst_el[1] else lst_el[::-1]

        else:
            return merger(div_half(lst_el[:len(lst_el)//2]), div_half(lst_el[len(lst_el)//2:]))

    return div_half(arr)

print('Случайный массив:', array, sep='\n')
print('\nМассив после сортировки:', fusion_sort(array), sep='\n')