# „Obcięcie” liczby naturalnej polega na usunięciu z niej M początkowych i N końcowych cyfr, gdzie
# M, N ⩾ 0. Proszę napisać funkcję, która dla danej liczby naturalnej K zwraca największą liczbę
# pierwszą o różnych cyfrach jaką można uzyskać z obcięcia liczby K albo 0, gdy taka liczba nie
# istnieje. Na przykład dla liczby 1202742516 spośród obciętych liczb pierwszych: 2, 5, 7, 251, 2027
# liczbą spełniającą warunek jest liczba 251.

from math import isqrt, log10

def is_prime(a):
    if a <= 1:
        return False
    if a == 2 or a == 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False
    i = 5
    while i <= isqrt(a): # type: ignore
        if a % i == 0:
            return False
        i += 2
        if a % i == 0:
            return False
        i += 4
    
    return True

def num_len(n):
    return int(log10(n) + 1)

def diff_digits(n):
    digits = [0] * 10
    # 10 cyfr 0-9

    while n > 0:
        digits[n % 10] += 1
        n //= 10

    for digit in digits:
        if digit > 1:
            return False
    
    return True


def zad1a(n):
    max_prime_num = 0

    while n > 1:
        # scinam poczatkowe cyfry
        n %= 10 ** (num_len(n) - 1)
        a = n
        while a > 1:
            # scinam koncowe cyfry
            a //= 10
            if is_prime(a) and diff_digits(a):
                max_prime_num = max(max_prime_num, a)

    return max_prime_num

print(zad1a(1202742516))