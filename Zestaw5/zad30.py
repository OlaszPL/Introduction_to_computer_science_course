# Punkt leżący na płaszczyźnie jest opisywany parą liczb typu float (x,y). Tablica T[N] zawiera
# współrzędne N punktów leżących na płaszczyźnie. Punkty posiadają jednostkową masę. Proszę napisać funkcję,
# która sprawdza czy istnieje niepusty podzbiór n punktów, gdzie n < k oraz n jest wielokrotnością liczby
# 3, którego środek ciężkości leży w odległości mniejszej niż r od początku układu współrzędnych. Do funkcji
# należy przekazać dokładnie 3 parametry: tablicę t, promień r, oraz ograniczenie k, funkcja powinna zwrócić
# wartość typu bool.

from math import sqrt

def dist(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 )

def zad29(T, r, k):
    N = len(T)

    def rek(T, r, k, N, Sx = 0, Sy = 0, n = 0, i = 0):
        if 0 < n < k and n % 3 == 0 and dist(Sx / n, Sy / n, 0, 0) < r:
            return True
        if i == N:
            return False
        
        return rek(T, r, k, N, Sx + T[i][0], Sy + T[i][1], n + 1, i + 1) or rek(T, r, k, N, Sx, Sy, n, i + 1)
    
    return rek(T, r, k, N)


T = [(1, 1.12), (2, 3), (12.3, 3.5), (3, 6), (1, 9), (2.26, 6.7)]
print(zad29(T, 5.98, 4))