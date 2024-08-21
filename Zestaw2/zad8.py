# Pewnych liczb nie można przedstawić jako sumy elementów spójnych fragmentów ciągu Fibonacciego, np. 9, 14, 15, 17, 22.
# Proszę napisać program, który wczytuje liczbę naturalną n, wylicza i wypisuje następną taką liczbę większą od n. Można założyć, że 0 < n < 1000.
# 1 1 2 3 5 8 13 21
# suma elementow spojnych fragmentow, niekoniecznie z poczatku

def is_in_fib(n):
    a = b = an = bn= 1
    sum = 0
    while sum < n:
        sum += a
        a, b = b, a + b
    
    while sum > n:
        sum -= an
        an, bn = bn, an + bn

    return sum == n

def next_not_in_fib(n):
    n += 1 # aby nie wyszło na to, ze ta sama liczba juz spelni warunek nie bycia suma podciagu
    while is_in_fib(n):
        n += 1
    
    return n

print(next_not_in_fib(int(input())))