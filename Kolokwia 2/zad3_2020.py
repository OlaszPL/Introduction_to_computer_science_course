# Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami całkowitymi. Proszę
# zaimplementować funkcję chess(T) która ustawia na szachownicy dwie wieże, tak aby suma liczb na
# „szachowanych” przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna
# zwrócić położenie wież w postaci krotki (row1, col1, row2, col2).
# Uwaga: zakładamy, że pola na których znajdują się wieże nie są szachowane.
# Przykładowe wywołania funkcji:
# print(chess([[4,0,2],[3,0,0],[6,5,3]])) # (0,1,1,0) suma=17
# print(chess([[1,1,2,3],[-1,3,-1,4], [4,1,5,4], [5,0,3,6]] # (2,3,3,1) suma=35

# O ile dobrze pamiętam trzeba rozpatrzyc wiele przypadkow

def zad20(T):
    n = len(T)
    max_sum = -float('inf')
    res_row1, res_column1, res_row2, res_column2 = 0, 0, 0, 0
    
    for row1 in range(n): # wybor pozycji wiezy1
        for column1 in range(n):
            for row2 in range(n): # wybor pozycji wiezy2
                for column2 in range(n):
                    sum = 0
                    if row1 != row2 and column1 != column2:
                        sum -= (2 * T[row1][column1] + 2 * T[row2][column2]) # odejmuje wartosi wiez ktore bylyby dodane przy sumowaniu rzedu i kolumny
                        sum -= (T[row1][column2] + T[row2][column1]) # odemuje raz przeciecia
                        for i in range(n):
                            sum += T[row1][i] + T[i][column1] + T[row2][i] + T[i][column2]
                    elif row1 == row2 and column1 != column2:
                        sum -= T[row1][column1] + T[row2][column2] # odejmujemy raz po wartosci wiezy bo tutaj jak 1 szachuje 2 to to sie wlicza
                        for i in range(n):
                            sum += T[row1][i] + T[i][column1] + T[i][column2] # dodajemy tylko raz rzad
                    elif row1 != row2 and column1 == column2:
                        sum -= T[row1][column1] + T[row2][column2] # odejmujemy raz po wartosci wiezy bo tutaj jak 1 szachuje 2 to to sie wlicza
                        for i in range(n):
                            sum += T[row1][i] + T[i][column1] + T[row2][i]  # dodajemy tylko kolumne
                    if sum > max_sum:
                        max_sum = sum
                        res_row1, res_column1, res_row2, res_column2 = row1, column1, row2, column2

    return (res_row1, res_column1), (res_row2, res_column2)

T = [
[1,     1000,  3,  4, 5, 6, 7 ],
[24, 25, 26, 27, 28, 29, 8 ],
[23, 40, 1000, 42, 43, 30, 9 ],
[22, 39, 48, 49, 44, 31, 10],
[21, 38, 1000, 46, 45, 32, 11],
[20, 37, 36, 35, 34, 33, 12],
[19, 18, 17, 168, 15, 14, 13]]

# T = [
#     [0,0,10],
#     [10,10,0],
#     [10,10,0]
# ]

print(zad20(T))