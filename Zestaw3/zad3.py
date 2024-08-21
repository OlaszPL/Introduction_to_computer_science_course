#  Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa.

from math import isqrt

def gen_prime_numbers(n):
    T = [True] * n # ostatni indeks to bedzie n-1 i tak
    T[0], T[1] = False, False

    for i in range(4, n, 2):
        T[i] = False
    
    for i in range(6, n, 3):
        T[i] = False
    
    d = 5

    while d <= isqrt(n): # nie ma juz sensu szukac wiekszych liczb pierwszych
        if T[d]:
            for i in range(2 * d, n, d):
                T[i] = False

        d += 2

        if T[d]:
            for i in range(2 * d, n, d ):
                T[i] = False

        d += 4

    cnt = 0
    for j in range(n):
        if T[j]:
            cnt += 1

    prime_numbers = [0] * cnt
    indx = 0
    for k in range(n):
        if T[k]:
            prime_numbers[indx] = k
            indx += 1
    
    return prime_numbers

    # with open('prime_numbers.txt', 'w') as f:
    #     for line in prime_numbers:
    #         f.write(f"{line}\n")

# nie da sie wiecej niz 1000000000 bo memory error
print(gen_prime_numbers(1000000000))