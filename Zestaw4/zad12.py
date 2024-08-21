# Dana jest tablica T[N][N][N]. Proszę napisać funkcję, do której przekazujemy tablicę wypełnioną 
# liczbami większymi od zera. Funkcja powinna zwracać wartość True, jeżeli na wszystkich poziomach
# tablicy liczba elementów sąsiadujących (w obrębia poziomu) z co najmniej 6 liczbami złożonymi
# jest jednakowa albo wartość False w przeciwnym przypadku.

from math import isqrt

def is_composite(n):
    if n == 0 or n == 1 or n == 2 or n == 3:
        return 0
    if n % 2 == 0 or n % 3 == 0:
        return 1
    
    i = 5

    while i <= isqrt(n):
        if n % i == 0:
            return 1
        i += 2
        if n % i == 0:
            return 1
        i += 4
    
    return 0

def slice(T): # 1 plaster
    n = len(T)
    l = [[0 for _ in range(n)] for _ in range(n)] # przechowuje czy zlozona czy nie

    for row in range(n):
        for column in range(n): # sprawdza czy sa pierwsze
            l[row][column] = is_composite(T[row][column])

    # policzyc ile elementow ma 6 sasiadow zlozonych

    cnt = 0

    for row in range(1, n - 1): # bo skrajne nie moga miec sasiadow
        for column in range(1, n - 1):
            li = -l[row][column]
            for row1 in range(row - 1, row + 2): # przelatujemy po malym kwadracie
                for column1 in range(column - 1, column + 2):
                    li += l[row - 1][column - 1]

            if li >= 6:
                cnt += 1
    
    return cnt

def main(T):
    n = len(T)
    cnt = slice(T[0])

    for i in range(1, n):
        if slice(T[i]) != cnt:
            return False
    
    return True