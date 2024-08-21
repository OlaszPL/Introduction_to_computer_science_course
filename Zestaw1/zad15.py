# Nieskończony iloczyn sqrt(0.5) * sqrt(0.5 + 0.5 * sqrt(0.5)) * sqrt(0.5 + 0.5 * sqrt (0.5 + 0.5 * sqrt(0.5))) * ...
# ma wartość 2/π. Proszę napisać program korzystający z tej zależności i wyznaczający wartość π.

from math import sqrt

def pi_value(accuracy):

    pi = 2
    a = sqrt(0.5)

    for _ in range(accuracy):
        pi /= a
        a = sqrt(0.5 + 0.5 * a)

    return pi

print(pi_value(1000000))
