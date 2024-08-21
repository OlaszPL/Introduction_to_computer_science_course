# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego suma otaczających go elementów jest największa.
# oczywiscie bez tego elementu
# Na rogach nigdy nie będzie większa suma ani na krańcach

def zad17(T):
    n = len(T)
    max_sum = 0
    res_row, res_column = 0, 0

    for row in range(1, n - 1): # bo to co napisalem wyzej
        for column in range(1, n - 1):
            sum = 0
            for n_row in range(row - 1, row + 2):
                for n_column in range(column - 1, column + 2):
                    sum += T[n_row][n_column]
            sum -= T[row][column]
            if sum > max_sum:
                max_sum = sum
                res_row, res_column = row, column

    return res_row, res_column


T = [
[1,     2,  3,  4, 5, 6, 7 ],
[24, 25, 26, 27, 28, 29, 8 ],
[23, 40, 41, 42, 43, 30, 9 ],
[22, 39, 48, 49, 44, 31, 10],
[21, 38, 47, 46, 45, 32, 11],
[20, 37, 36, 35, 34, 33, 12],
[19, 18, 17, 168, 15, 14, 13]]

print(zad17(T))