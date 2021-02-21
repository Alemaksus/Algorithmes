# Написать программу умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования
# систем исчисления, задача решается в несколько строк.
# Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из одной системы
# исчисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

# Идеальное решение:

# a = 'A2'
# b = 'C4F'
# c = hex(int(a, 16) + int(b, 16))
# d = hex(int(a, 16) * int(b, 16))
# print(c, d)

# Но, по заданию нужно помучиться. Мой вариант:

# first = input("Введите первое шестнадатиричное число: ")
# second = input("Введите второе шестнадатиричное число: ")
#
# list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
#
# if len(first) > len(second):
#   first, second = second, first
#
# second = second[::-1]
# third = []
#
# j = -1
# k = 0
# for i in second:
#   one = list_of_numbers.index(i)
#   two = list_of_numbers.index(first[j])
#   third.append(list_of_numbers[(one + two + k) % 16])
#   if (one + two) >= 15:
#     k = 1
#   else:
#     k = 0
#   j -= 1
#   if j == -len(first)-1:
#     break
#
# diff = len(second) - len(first)
#
# if diff:
#     for i in second[-diff:]:
#         third.append(list_of_numbers[(list_of_numbers.index(second[-diff]) + k) % 16])
#         if list_of_numbers.index(second[-diff]) + 1 >= 15:
#             k = 1
#         else:
#             k = 0
#
# if k == 1:
#   third.append('1')
#
# print(third[::-1])

# Правильный вариант от Евгении Хохловой:

from collections import defaultdict
from collections import deque

num_1 = input('Введите первое число: ').upper()
num_2 = input('Введите второе число: ').upper()

chars = '0123456789ABCDEF'
table = defaultdict(int)
counter = 0
for key in chars:
    table[key] += counter
    counter += 1


def dexim(string):
    dex = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        dex += table[num[i]] * 16 ** i
    return dex


def hexim(numb):
    num = deque()
    while numb > 0:
        d = numb % 16
        for i in table:
            if table[i] == d:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)


num_1 = dexim(num_1)
num_2 = dexim(num_2)

sum = hexim(num_1 + num_2)
mult = hexim(num_1 * num_2)

print(f'Сумма: {sum}')
print(f'Произведение: {mult}')