# Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Proszę napisać funkcję,
# która wyszuka spójny podciąg elementów leżący poziomo lub pionowo o największej sumie.
# Maksymalna długość podciągu może wynosić 10 elementów. Do funkcji należy przekazać tablicę T,
# funkcja powinna zwrócić sumę maksymalnego podciągu.

def zad18(T):
    n = len(T)
    max_sum = -float('inf')

    for row in range(n):
        for column in range(n):
            i = 0
            sum_r = 0
            while row + i < n and i <= 10:
                sum_r += T[row + i][column]
                i += 1

            i = 0
            sum_c = 0
            while column + i < n and i <= 10:
                sum_c += T[row][column + i]
                i += 1

            max_sum = max(max_sum, sum_r, sum_c)
    
    return max_sum

T = [
[1,     2,  3,  4, 5, 6, 7 ],
[24, 25, 26, 27, 28, 29, 8 ],
[23, 40, 41, 42, 43, 30, 9 ],
[22, 39, 48, 49, 44, 31, 10],
[21, 38, 47, 46, 45, 32, 11],
[20, 37, 36, 35, 34, 33, 12],
[19, 18, 17, 168, 15, 14, 13]]

print(zad18(T))