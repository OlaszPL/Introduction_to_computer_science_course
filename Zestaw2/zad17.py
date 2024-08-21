# Proszę napisać program wyliczający pierwiastek równania x^x = 2020 metodą stycznych.

from math import log, e

def f(x):
    return x ** x - 2020

def f_prim(x):
    return (x ** x) * (log(x, e) + 1)

def newton(x, eps = 1e-10):
    while abs(f(x)) > eps:
        x = x - ((f(x) / f_prim(x)))

    return x, f(x)

print(newton(3))