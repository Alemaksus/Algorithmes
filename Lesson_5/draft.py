import platform
import sys
import cProfile

def profile(func):
    """Decorator for run function profile"""

    def wrapper(*args, **kwargs):
        profile_filename = func.__name__ + '.prof'
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        return result

    return wrapper


def abs123(q):
    for i in range(len(q)):
        if q[i] == 'a':
            q[i] = 10
        elif q[i] == 'b':
            q[i] = 11
        elif q[i] == 'c':
            q[i] = 12
        elif q[i] == 'd':
            q[i] = 13
        elif q[i] == 'e':
            q[i] = 14
        elif q[i] == 'f':
            q[i] = 15
    return q


def to16(s):
    for i in range(len(s)):
        if s[i] == 10:
            s[i] = 'a'
        elif s[i] == 11:
            s[i] = 'b'
        elif s[i] == 12:
            s[i] = 'c'
        elif s[i] == 13:
            s[i] = 'd'
        elif s[i] == 14:
            s[i] = 'e'
        elif s[i] == 15:
            s[i] = 'f'
    return s


def sum16(x, y):
    z = []
    xx = abs123(x[::-1])
    yy = abs123(y[::-1])
    if len(xx) >= len(yy):
        for i in range(len(xx) - len(yy)):
            yy.append(0)
    else:
        for i in range(len(yy) - len(xx)):
            xx.append(0)
    p, zz, zzz = 0, 0, 0
    for i in range(len(xx)):
        zz = int(xx[i]) + int(yy[i]) + p
        if zz >= 16:
            p = zz // 16
            zzz = zz % 16
        else:
            zzz = zz
            p = 0
        z.append(zzz)
    if p > 0:
        z.append(p)
    # print(z, to16(z[::-1]))
    return to16(z[::-1])


def to10(x):
    xx = abs123(x)
    tenn = 0
    for i in range(len(xx)):
        ll = len(xx) - i - 1
        s = 16 ** ll
        ten = int(xx[i]) * s
        tenn += ten
    return tenn


def mul(x, y):
    dd = x
    for i in range(to10(y) - 1):
        dd = sum16(x, dd)
    return dd


@profile
def main():
    a = input("\nВведите первое число в 16 формате: ")
    b = input("Введите второе число в 16 формате: ")
    # a = 'fff'
    # b = 'fff'
    aa = list(a)
    bb = list(a)
    sum = sum16(aa, bb)
    print(f"\nСумма чисел {a} и {b}:")
    for i in sum:
        print(i, end="")
    dd = mul(aa, bb)
    print(f"\nПроизведение чисел {a} и {b}:")
    for i in dd:
        print(i, end="")
    print(f"\n\nцифры в десятичном формате:\na = {to10(aa)}\nb = {to10(bb)}\nsum = {to10(sum)}\nmul = {to10(dd)}\n\n")

if __name__ == '__main__':
    main()
