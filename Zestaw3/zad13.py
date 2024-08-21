# Proszę napisać program, który wypełnia N-elementową tablicę t trzycyfrowymi liczbami
# pseudolosowymi, a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego znajdującego
# się w tablicy dla którego w tablicy występuje również rewers tego ciągu. Na przykład dla tablicy: 
# t = [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] odpowiedzią jest liczba 4.
# zakladam, ze [1,2,3,4,3,2,1] - to 4 nie jest uwspolnione

from random import randint

def podciag(n):

    #t = [2,4,5,6,7,8,7,6,5,4,2,3,3,3] # n = 14
    #t = [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] # n = 15
    
    t = [randint(100, 999) for _ in range(n)]
    print(t)
    max_len = 0

    for i in range(n - 1): # chcemy maksymalnie dla indeksu 13 bo 14 jest ostatni
        for j in range(n - 1, i, -1): #od n - 1 bo początek dosięga danego indeksu, a nie ma indeksu 15, bo startujemy od 0
            temp_len = 0
            a, b = i, j # bo niszczbylyby sie zmienne do iterowania
            while t[a] == t[b] and a < n and b > a: # wazne ze b > a bo inaczej zaczynaja na siebie nachodzic
                temp_len += 1
                a += 1
                b -= 1

            if temp_len > max_len:
                max_len = temp_len
                
    return max_len

print(podciag(int(input())))