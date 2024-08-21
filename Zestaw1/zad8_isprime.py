#Proszę napisać program sprawdzający czy zadana liczba jest pierwszą.

from math import isqrt

def is_prime(a):
    if a <= 1:
        return False
    if a == 2 or a == 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False

    i = 5

    while i <= isqrt(a):
        if a % i == 0:
            return False
        i += 2

        if a % i == 0:
            return False
        i += 4

    return True

a = int(input())
print(is_prime(a))