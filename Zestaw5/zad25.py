# Tablica t[N] jest wypełniona liczbami naturalnymi. Skok z pola i-tego można wykonać na pola
# o indeksach i+k, gdzie k jest czynnikiem pierwszym liczby t[i] (mniejszym od niej samej).
# Napisz funkcję, która sprawdza, czy da się przejść z pola 0 do N-1 –
# jeśli się da, zwraca ilość skoków, jeśli się nie da, zwraca -1.

from math import isqrt

def gen_prime(n): # zwróci tablicę liczb pierwszych mniejszych od samej liczby
    T = [0] * (isqrt(n) + 1)
    i = 2
    j = 0
    n_bak = n

    while i <= isqrt(n):
        if n % i == 0:
            T[j] = i
            j += 1
            while n % i == 0:
                n //= i

        i += 1

    if n != 1 and n < n_bak:
        T[j] = n
        j += 1
    
    primes = [0] * j
    for k in range(j):
        primes[k] = T[k]

    return primes

def zad25(T):
    n = len(T)
    cnt = 0
    
    def rek(T, n, i = 0, tmp_cnt = 0):
        nonlocal cnt
        if i == n - 1:
            cnt = tmp_cnt

        jumps = gen_prime(T[i])

        for jump in jumps:
            rek(T, n, i + jump, tmp_cnt + 1)
        
        return
    
    rek(T, n)

    return cnt if cnt else -1
    
T = [4, 0, 6, 0, 0, 1]

print(zad25(T))