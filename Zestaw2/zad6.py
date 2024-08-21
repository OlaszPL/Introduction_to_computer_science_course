# Proszę napisać program wczytujący liczbę naturalną i rozkładający ją na iloczyn 2 liczb o najmniejszej różnicy. Np. 30 = 5 ∗ 6, 120 = 10 ∗ 12.
# ostatnia para podzielnikow daje najmniejsza roznice - co ciekawe zawsze

from math import isqrt

def zad6(n):
    i = 1
    a = b = 0

    while i <= isqrt(n):
        if n % i == 0:
            a = i
            b = n // i
            
        i += 1

    return a, b, abs(a - b)


print(zad6(int(input())))