# Proszę napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina.
# dla kata w radianach

from math import pi

eps = 1e-10

def cos(x):

    if x >= 2 * pi:
        x %= 2 * pi # skracam o okres fun cos

    fact = 24
    s = 1 - 0.5 * (x * x)
    k = 4
    a = 1
    m = 1

    while abs(a) >= eps:
        a = m * (1 / fact) * (x ** k)
        s += a
        k += 2
        fact *= (k - 1) * k
        m *= -1

    return s

print(cos(float(input())))