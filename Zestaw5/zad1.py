# Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
# co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
# cyfry.

from math import isqrt, log10

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i <= isqrt(n):
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    
    return True

# skreslanie jest zlym pomyslem, lepiej generowac, albo dana cyfre dokladamy albo nie

def zad1(num):

    def rek(num, new_num = 0, rzad = 1, prev_num = 0):
        if is_prime(new_num) and (int(log10(new_num)) + 1) >= 2 and new_num != prev_num:
            print(new_num)
        if num == 0:
            return
        
        rek(num // 10, new_num + (num % 10 * rzad), rzad * 10, new_num)
        rek(num // 10, new_num, rzad, new_num) # prev_num wprowadzone bo tutaj pojawialy sie powtorzenia kiedy skracal i wypisywal kilka razy to samo

    rek(num)

zad1(123)