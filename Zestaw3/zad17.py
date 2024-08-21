# Dane są dwie N-elementowe tablice t1 i t2 zawierające liczby naturalne.
# Z wartości w obu tablicach możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co
# najmniej jeden element (z tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic:
# t1 = [1,3,2,4] i t2 = [9,7,4,8] poprawnymi sumami są na przykład
# 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8.
# Proszę napisać funkcje generującą i wypisująca wszystkie poprawne sumy, które są liczbami pierwszymi.
# Do funkcji należy przekazać dwie tablice, funkcja powinna zwrócić liczbę znalezionych i wypisanych
# sum.

# maska tritowa
# 0 - element z tablicy 1, 1 - element z tablicy 2, 2 - elementy z obu tablic
# system trójkowy: n % 3: [ 0, 1, 2 ]

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

def gen_sum_from_mask(t1, t2, mask):
    sum = 0
    n = len(t1) # bo sa tej samej wielkosci

    for i in range(n):
        if mask % 3 == 0:
            sum += t1[i]
        elif mask % 3 == 1:
            sum += t2[i]
        elif mask % 3 == 2:
            sum += t1[i] + t2[i]
        mask //= 3
    
    return sum

def maska_tritowa(t1, t2):
    n = len(t1)
    cnt = 0

    for mask in range(3 ** n):
        if is_prime(gen_sum_from_mask(t1, t2, mask)):
            cnt += 1
    
    return cnt

t1 = [1, 4, 52, 3, 5, 2, 35]
t2 = [33, 0, 93, 5, 12, 2, 5]

print(maska_tritowa(t1, t2))