# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów
# w kolumnie w którym leży element do sumy elementów wiersza w którym leży element jest największa.

# (suma elementow kolumny) / (suma elementow wiersza) --> najwieksza

# max(suma kolumny); min(suma wiersza)

def zad4(T):
    n = len(T)
    max_column_sum = -float('inf')
    min_row_sum = float('inf')
    res_row, res_column = 0, 0 # result

    for row in range(n):
        tmp_row_sum = 0
        for column in range(n):
            tmp_row_sum += T[row][column]

        if tmp_row_sum < min_row_sum:
            min_row_sum = tmp_row_sum
            res_row = row

    for column in range(n):
        tmp_column_sum = 0
        for row in range(n):
            tmp_column_sum += T[row][column]
        
        if tmp_column_sum > max_column_sum:
            max_column_sum = tmp_column_sum
            res_column = column

    return(res_row, res_column)

# T = [[1, 2, 3, 4, 5, 6, 7],
# [24, 25, 26, 27, 28, 29, 8],
# [23, 40, 41, 42, 43, 30, 9],
# [22, 39, 48, 49, 44, 31, 10],
# [21, 38, 47, 46, 45, 32, 11],
# [20, 37, 36, 35, 34, 33, 12],
# [19, 18, 17, 16, 15, 14, 13]]

T = [
    [2, 2, 2, 2, 2],
    [1, 1, 3, 3, 3],
    [1, 1, 1, 1, 1],
    [1, 1, 7, 7, 7],
    [1, 1, 11, 11, 11]
]

print(zad4(T))