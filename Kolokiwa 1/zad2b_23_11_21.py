# Liczbę nazywamy iloczynowo-pierwszą jeżeli iloczyn jej cyfr w systemie o podstawie b jest liczbą
# pierwszą. Na przykład:
# 13 jest liczbą iloczynowo-pierwszą w systemie dziesiętnym, bo 1 · 3 = 3.
# 16 jest liczbą iloczynowo-pierwszą w systemie trójkowym, bo 16(10) = 12(13), 1 · 2 · 1 = 2.
# W liczbie naturalnej możemy dokonywać rotacji jej cyfr, np. 1428, 4281, 2814, 8142 albo 209, 092,
# 920.
# Proszę napisać funkcję, która dla danej liczby naturalnej N, zwróci najmniejszą podstawę systemu (z
# zakresu 2-16) w którym przynajmniej jedna z rotowanych liczb jest iloczynowo-pierwsza albo wartość
# None, gdy taka podstawa nie istnieje.

from math import isqrt, log10

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

def czy_iloczynowo_pierwsza(num, sys):
    iloczyn = 1
    while num > 0:
        iloczyn *= num % sys
        num //= sys
    
    return is_prime(iloczyn)

def zad2(num):
    num_len = int(log10(num) + 1)
    rotacje = [0] * num_len

    for i in range(num_len):
        rotacje[i] = num
        x = num % 10
        num //= 10
        num += x * 10 ** (num_len - 1)
    
    for sys in range(2, 16 + 1):
        for el in rotacje:
            if czy_iloczynowo_pierwsza(el, sys):
                return sys
    
    return None

print(zad2(16))