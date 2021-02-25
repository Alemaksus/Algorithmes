# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

from analyzer import print_analyze, values

@print_analyze
def bubble_sort(data, reverse=False):
    """ Bubble sorting """
    sorting = True
    last_sorted = 1
    while sorting:
        sorting = False
        for index in range(len(data) - last_sorted):
            if ((data[index] > data[index + 1]) ^ reverse) and data[index] != data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]
                sorting = True
        last_sorted += 1
    return data

if __name__ == '__main__':
    source = values((-100, 100), count=100)
    print(f'Source:     | length={len(source)}\n{source}')
    print(bubble_sort(source, reverse=True))