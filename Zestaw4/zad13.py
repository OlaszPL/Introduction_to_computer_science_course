# Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą. Dana jest tablica T[N][N]
# wypełniona liczbami naturalnymi. Proszę napisać funkcję, która zeruje elementy nie posiadające liczby komplementarnej.

from math import isqrt

def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0  or n % 3 == 0:
        return False
    
    i = 5

    while i <= isqrt(n):
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    
    return True

def zad13(T):
    n = len(T)
    T2 = [[False for _ in range(n)] for _ in range(n)]

    for row in range(n):
        for column in range(n):
            for row2 in range(n):
                for column2 in range(n):
                    if is_prime(T[row][column] + T[row2][column2]): # nie moge w tym momenicie wyzerowac rekordu tablicy
                        T2[row][column] = True

    for row in range(n):
        for column in range(n):
            if not T2[row][column]:
                T[row][column] = 0
    
    # return T

T = [[2, 7, 2, 2],
     [2, 2, 2, 2],
     [2, 2, 4, 2],
     [2, 2, 2, 2]]

zad13(T)

print(*T, sep='\n')