# Dana jest duża tablica t. Proszę napisać funkcję, która zwraca informację czy w tablicy zachodzi następujący warunek:
# „wszystkie elementy, których indeks jest elementem ciągu Fibonacciego są liczbami złożonymi, a wśród pozostałych przynajmniej jedna jest liczbą pierwszą”.

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

def is_composite(a):
    if a != 0 and a != 1 and not is_prime(a):
        return True
    else:
        return False
    
def zad15(t):
    n = len(t)
    is_element_of_fib = [False] * n
    a, b = 1, 1 # bo ciag od 1
    while a < n:
        is_element_of_fib[a] = True # tablica czy indeks jest liczba z ciagu Fibbonacciego
        a, b = b, a + b

    flag = False
    for i in range(n):
        if is_element_of_fib[i] and not is_composite(t[i]):
            return False
        elif is_prime(t[i]):
            flag = True
    
    return flag

t = [31, 30, 85, 15, 4, 6]

print(zad15(t))