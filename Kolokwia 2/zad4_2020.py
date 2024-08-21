# Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza czy jest możliwe
# pocięcie liczby N na kawałki, tak aby każdy z kawałków był liczba pierwszą oraz liczba kawałków też była
# liczbą pierwszą. Funkcja powinna zwracać wartość logiczną. Na przykład: divide(2347)=True, podział na
# 23 i 47, natomiast divide(2255)=False.
# Przykładowe wywołania funkcji:
# print(divide(273)) # True, podział 2|7|3
# print(divide(22222)) # True, podział 2|2|2|2|2
# print(divide(23672)) # True, podział 23|67|2
# print(divide(2222)) # False
# print(divide(21722)) # False

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

def divide(n, zbior = 0, kawalki = 1): # kawalki = 1 bo bazowo istnieje 1
    if n == 0:
        return is_prime(kawalki) and is_prime(zbior)
    
    if is_prime(zbior):
        if divide(n, 0, kawalki + 1): # zaczynamy nowy zbior i zwiekszyamy ilosc kawalkow
            return True
        
    return divide(n % 10 ** int(log10(n)), zbior * 10 + (n // 10 ** int(log10(n))), kawalki)
    
print(divide(23672))