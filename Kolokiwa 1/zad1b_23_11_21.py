# Dana jest N-elementowa tablica T, zawierająca liczby. Proszę napisać funkcję, która zwróci indeks
# największej liczby, która jest iloczynem wszystkich liczb pierwszych leżących w tablicy na indeksach
# mniejszych od niej lub None, jeżeli taka liczba nie istnieje.

from math import isqrt

def is_prime(a):
    if a <= 1:
        return False
    if a == 2 or a == 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False
    i = 5
    while i <= isqrt(a): # type: ignore
        if a % i == 0:
            return False
        i += 2
        if a % i == 0:
            return False
        i += 4
    
    return True

def zad1(T):
    n = len(T)
    multiply = 1
    stored_i = None

    for i in range(n):
        if is_prime(T[i]):
            multiply *= T[i]
        elif T[i] == multiply:
            stored_i = i
    
    return stored_i

T = [12, 22, 2, 3, 7, 13, 546, 121]

print(zad1(T))