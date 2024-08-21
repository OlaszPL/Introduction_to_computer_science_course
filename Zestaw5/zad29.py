# Punkt leżący w przestrzeni jest opisywany trójką liczb typu float (x,y,z). Tablica T[N] zawiera
# współrzędne N punktów leżących w przestrzeni. Punkty posiadają jednostkową masę. Proszę napisać funkcję,
# która sprawdza czy istnieje podzbiór punktów liczący co najmniej 3 punkty, którego środek ciężkości leży w
# odległości nie większej niż r od początku układu współrzędnych. Do funkcji należy przekazać tablicę T oraz
# promień r, funkcja powinna zwrócić wartość typu bool.

from math import sqrt

def dist(x1, y1, z1, x2, y2, z2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def zad29(T, r):
    n = len(T)

    def rek(T, r, n, Sx = 0, Sy = 0, Sz = 0, n1 = 0, i = 0):
        if n1 >= 3 and dist(Sx / n1, Sy / n1, Sz / n1, 0, 0, 0) <= r:
            return True
        if i == n:
            return False
        
        return rek(T, r, n, Sx + T[i][0], Sy + T[i][1], Sz + T[i][2], n1 + 1, i + 1) or rek(T, r, n, Sx, Sy, Sz, n1, i + 1)
    
    return rek(T, r, n)


T = [(1, 1.12, 3), (2, 3, 8), (12.3, 3.5, 6.7), (3, 6, 7), (1, 9, 7), (2.26, 6.7, 2.3)]
print(zad29(T, 5.98))