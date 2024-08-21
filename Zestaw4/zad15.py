# Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję, która odpowiada na pytanie,
# czy w tablicy istnieje wiersz, w którym każda liczba zawiera co najmniej jedną cyfrę będącą liczbą pierwszą?

from math import isqrt

def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5

    while i <= isqrt(n):
        if n % i == 0:
            return False
        else:
            i += 2
            if n % i == 0:
                return False
            else:
                i += 4
    
    return True

def zad15(T):
    n = len(T)

    for row in range(n):
        flag = True
        if flag:
            for column in range(n):
                tmp = T[row][column]
                inner_flag = False
                while tmp > 0 and not inner_flag:
                    if is_prime(tmp % 10):
                        inner_flag = True
                    tmp //= 10
                if not inner_flag:
                    flag = False
        if flag:
            return True
    
    return False
        

T = [[13, 4, 3, 3],
     [3, 3, 4, 5],
     [4, 2, 9, 8],
     [12,6, 9, 27]]

print(zad15(T))