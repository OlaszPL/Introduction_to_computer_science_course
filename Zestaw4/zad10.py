# Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca wartość
# True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz wartość
# False w przeciwnym przypadku.

# sprawdzamy 'na ukos'

def zad10(T):
    n = len(T)

    for row in range(n):
        row_check, column_check = False, False
        for column in range(n):
            if T[row][column] == 0:
                row_check = True
            if T[column][row] == 0:
                column_check = True

        if not row_check or not column_check:
            return False
    
    return True

T = [
    [0, 2, 2, 0, 0],
    [1, 0, 0, 3, 3],
    [0, 1, 5, 1, 1],
    [1, 1, 0, 8, 7],
    [1, 0, 11, 11, 9]
]

print(zad10(T))