# Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
# na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą
# Długość każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe,
# a dla ciągu 110100 nie jest możliwe.

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

def zad5(T):
    n = len(T)

    def rek(T, n, num = 0, i = 0):
        if i == n:
            return is_prime(num)
        
        new_num = num + T[i] * 2 ** (n - 1 - i)

        if is_prime(new_num):
            return rek(T, n, 0, i + 1) or rek(T, n, new_num, i + 1) # jezeli pierwsza to mozemy podzielic albo dobrac nastepna
        
        return rek(T, n, new_num, i + 1) # dla nie pierwszej mozemy tez dobrac nastepna
    
    return rek(T, n)

T = [1,1,0,1,0,0]

print(zad5(T))