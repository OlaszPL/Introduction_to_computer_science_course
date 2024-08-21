# Dana jest N-elementowa tablica t zawierająca liczby naturalne. W tablicy możemy przeskoczyć
# z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby t[k].
# Napisać funkcję sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.

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

def is_prime_factor(num, fact):
    if num % fact == 0 and is_prime(fact):
        return True
    else:
        return False
    
def zad8(t):
    N = len(t)
    n = N - 1 # przeskok
    if is_prime_factor(t[0], n):
        return True
    else:
        return False

t = [15, 5, 5, 4, 5, 7]

print(zad8(t))