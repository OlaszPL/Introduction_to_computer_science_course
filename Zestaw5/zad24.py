# Tablica T = [(x1, y1),(x1, y1), ...] zawiera położenia N punktów o współrzędnych opisanych
# wartościami typu float. Proszę napisać funkcję, która zwróci najmniejszą odległość między
# środkami ciężkości 2 niepustych podzbiorów tego zbioru.

from math import sqrt

def dist(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def zad24(T):
    res = float('inf')
    n = len(T)

    def rek(T, n, Sx1 = 0, Sy1 = 0, Sx2 = 0, Sy2 = 0, n1 = 0, n2 = 0, i = 0):
        nonlocal res
        if n1 and n2: # czy niepuste
            res = min(dist(Sx1 / n1, Sy1 / n1, Sx2 / n2, Sy2 / n2), res)
        if i == n:
            return
        
        rek(T, n, Sx1 + T[i][0], Sy1 + T[i][1], Sx2, Sy2, n1 + 1, n2, i + 1)
        rek(T, n, Sx1, Sy1, Sx2 + T[i][0], Sy2 + T[i][1], n1, n2 + 1, i + 1)
        rek(T, n, Sx1, Sy1, Sx2, Sy2, n1, n2, i + 1)

        return
    
    rek(T, n)

    return res

T = [(0, 1), (1, 8), (5, 14), (1, 1.3), (16, 18.5), (99, 105.3), (23, 15), (1.23, 8.93)]
print(zad24(T))