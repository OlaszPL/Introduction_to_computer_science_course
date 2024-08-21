# Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca sumę iloczynów elementów wszystkich
# niepustych podzbiorów zbioru podzielników pierwszych tej liczby. Można założyć, że liczba podzielników pierwszych
# nie przekracza 20, zatem w pierwszym etapie funkcja powinna wpisać podzielniki do tablicy pomocniczej.
# Przykład: 60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71

from math import isqrt

def dividers(n):
    tmp_div = [0] * 20
    j = 0
    i = 2
    while i <= isqrt(n):
        if n % i == 0:
            tmp_div[j] = i
            j += 1
        while n % i == 0:
            n //= i
        
        i += 1
    
    if n != 1:
        tmp_div[j] = n
        j += 1
    
    dividers = [0] * j

    for i in range(j):
        dividers[i] = tmp_div[i]
    
    return dividers


def zad31(num):
    divs = dividers(num)
    n = len(divs)
    sum = 0

    def rek(divs, n, p = 1, i = 0):
        nonlocal sum
        if i == n:
            sum += p
            return
        
        rek(divs, n, p, i + 1)
        rek(divs, n, p * divs[i], i + 1)

    rek(divs, n)

    return sum - 1

print(zad31(60))
