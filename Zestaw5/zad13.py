# Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników.
# Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.

def printT(T):
    cnt = 0
    for el in T:
        if el:
            cnt += 1

    T_new = [0] * cnt
    for i in range(cnt):
        T_new[i] = T[i]

    for j in range(cnt - 1):
        print(T_new[j], end='+')

    print(T_new[cnt - 1])

def zad13(n):
    T = [0] * n

    def rek(T, n, i = 0, n_bak = n):
        if n == 0 and T[0] != n_bak:
            printT(T)
            return
        if i == 0:
            min = 1
        else:
            min = T[i - 1] # jak mamy 1+2 to nastepny element nie moze byc mniejszy od 2
        for j in range(min, n + 1): # wybór wartości do wstawienia w tablicę
            T[i] = j
            rek(T, n - j, i + 1)
            T[i] = 0 # backtracking

    rek(T, n)

zad13(4)