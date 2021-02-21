# Variant 1: Простейший циклический алгоритм, основанный на вычитании
def gcd(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m

# Variant 2: Рекурсивный алгоритм, основанный на нахождении остатка от деления:
def gcd2(m, n):
    if n == 0:
        return m
    return gcd2(n, m % n)

# Variant 3 (наиболее быстрый и наименее ресурсозатратный): Циклический алгоритм, основанный на нахождении остатка от деления:
def gcd3(m, n):
    while n != 0:
        m, n = n, m % n
    return m

print(gcd(540, 120))
print(gcd2(540, 120))
print(gcd3(540, 120))

