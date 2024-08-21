# Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr
# 1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca
# ilość wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym
# (najstarszy bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3
# ilość liczb wynosi 3, są to 10010(2), 10100(2), 11000(2).

# Z klucza wynika, że A i B muszą być zużyte w całości

from math import isqrt

def is_composite(a):
    if a <= 1:
        return False
    if a == 2 or a == 3:
        return False
    if a % 2 == 0 or a % 3 == 0:
        return True
    i = 5
    while i <= isqrt(a):
        if a % i == 0:
            return True
        i += 2
        if a % i == 0:
            return True
        i += 4
    
    return False

def convert_to_decimal(num):
    res = 0
    pow = 0
    while num > 0:
        if num % 2 == 1:
            res += 2 ** pow
        pow += 1
        num //= 10
    
    return res

def zad26(A, B):
    cnt = 0

    def rek(A, B, new_num):
        nonlocal cnt
        if A == 0 and B == 0 and is_composite(convert_to_decimal(new_num)):
            cnt += 1
            return
        
        if A != 0:
            rek(A - 1, B, (new_num * 10) + 1)
        if B != 0:
            rek(A, B - 1, new_num * 10)

        return
    
    rek(A - 1, B, 1) # bo 1 ma byc na poczatku zawsze

    return cnt

print(zad26(2, 3))
