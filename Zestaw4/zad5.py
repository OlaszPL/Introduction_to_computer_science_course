# Poprzednie zadanie z tablicą wypełnioną liczbami całkowitymi.

# (suma elementow kolumny) / (suma elementow wiersza) --> najwieksza

# max(suma kolumny); min(suma wiersza)

def zad5(T):
    n = len(T)
    sum_of_columns = [0] * n # indeks tablicy odpowiada indeksowi kolumny z tablicy pierwotnej
    sum_of_rows = [0] * n
    res_row, res_column = 0, 0

    for row in range(n):
        for column in range(n): # dziala bo indeksy w tablicach sum sa rozne
            sum_of_rows[row] += T[row][column]
            sum_of_columns[column] += T[row][column]

    # print(sum_of_rows)
    # print(sum_of_columns)
            
    ratio = -float('inf')

    for rrow in range(n):
        for rcolumn in range(n):
            tmp_ratio = sum_of_columns[rcolumn] / sum_of_rows[rrow]
            if tmp_ratio > ratio:
                ratio = tmp_ratio
                res_row = rrow
                res_column = rcolumn

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

print(zad5(T))