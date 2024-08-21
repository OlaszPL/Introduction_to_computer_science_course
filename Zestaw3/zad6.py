# Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi 1-1000 i
# sprawdzający czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą.

from random import randint

def odd_digit(num):
    while num > 0:
        if not (num % 10) % 2 == 0:
            return True
        num //= 10
    
    return False

def zad6(n):
    T = [randint(1, 1000) for _ in range(n)]
    print(T)
    for i in T:
        if not odd_digit(i):
            return False
        
    return True

print(zad6(10))