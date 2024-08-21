# Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie M=N*N.
# W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco (w obrębie wiersza) liczby naturalne.
# Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy T2
# były uporządkowane niemalejąco.

def zad7(T1):
    n = len(T1)
    T2 = [float('inf')] * (n * n)

    for row in range(n):
        for column in range(n):
            x = T1[row][column]
            for i in range(n * n): # iterujemy po T2
                if x < T2[i]:
                    x, T2[i] = T2[i], x

    return T2
    
T1 = [
    [2, 2, 2, 2, 2],
    [1, 1, 3, 3, 3],
    [1, 1, 1, 1, 1],
    [1, 1, 7, 7, 7],
    [1, 1, 11, 11, 11]
]

print(zad7(T1))