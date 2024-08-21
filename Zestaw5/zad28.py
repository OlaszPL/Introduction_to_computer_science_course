# Dany jest zbiór N liczb naturalnych umieszczony w tablicy T[N]. Proszę napisać funkcję,
# która zwraca informację, czy jest możliwy podział zbioru N liczb na trzy podzbiory, tak aby w każdym
# podzbiorze, łączna liczba jedynek użyta do zapisu elementów tego podzbioru w systemie dwójkowym była
# jednakowa. Na przykład: [2, 3, 5, 7, 15] → true, bo podzbiory {2,7} {3,5} {15} wymagają użycia 4 jedynek,
# [5, 7, 15] → false, podział nie istnieje.

def sum_ones(num):
    cnt = 0
    while num > 0:
        cnt += num % 2
        num //= 2

    return cnt

def zad28(T):
    n = len(T)

    def rek(T, n, a = 0, b = 0, c = 0, i = 0): # abc sumy jedynek danych liczb
        if i == n:
            if a != 0 and b != 0 and c != 0:
                return a == b == c
            else:
                return False
        
        return rek(T, n, a + sum_ones(T[i]), b, c, i + 1) or rek(T, n, a, b + sum_ones(T[i]), c, i + 1) or rek(T, n, a, b, c + sum_ones(T[i]), i + 1)
    
    return rek(T, n)

T = [2, 3, 5, 7, 15]
# T = [5, 7, 15]
print(zad28(T))