# Rekurencyjne obliczanie wyznacznika z macierzy (treść oczywista)

def are_rows_or_columns_null(T, n): # bo jak jakis wiersz lub rzad == 0 to wtedy wyznacznik == 0
    for r in range(n):
        flag = True
        for c in range(n):
            if T[r][c] != 0:
                flag = False
                break
        if flag:
            return True
    
    for c in range(n):
        flag = True
        for r in range(n):
            if T[r][c] != 0:
                flag = False
                break
        if flag:
            return True
    
    return False

def matrix2x2(T):
    return (T[0][0] * T[1][1]) - (T[0][1] * T[1][0])

def matrix3x3(T):
    return (T[0][0] * T[1][1] * T[2][2]) + (T[0][1] * T[1][2] * T[2][0]) + (T[0][2] * T[1][0] * T[2][1]) - (\
        T[2][0] * T[1][1] * T[0][2]) - (T[2][1] * T[1][2] * T[0][0]) - (T[2][2] * T[1][0] * T[0][1])

def wyznacznik(T):
    n = len(T)

    if n == 2:
        return matrix2x2(T)
    elif n == 3:
        return matrix3x3(T)
    elif are_rows_or_columns_null(T, n):
        return 0
    
    def laplace_rek(T, n):
        if n == 3:
            return matrix3x3(T)
        
        res = 0

        for r_rm in range(n): #column == 0 always
            T_new = [[0 for _ in range(n - 1)] for _ in range(n - 1)] # slicing
            i, j = 0, 0
            for r_to_cop1 in range(0, r_rm):
                for c_to_cop1 in range(1, n):
                    T_new[i][j] = T[r_to_cop1][c_to_cop1]
                    j += 1
                i += 1
                j = 0

            for r_to_cop2 in range(r_rm + 1, n):
                for c_to_cop2 in range(1, n):
                    T_new[i][j] = T[r_to_cop2][c_to_cop2]
                    j += 1
                i += 1
                j = 0

            res += T[r_rm][0] * ((-1) ** (1 + r_rm + 1)) * laplace_rek(T_new, n - 1) # liczenie elementow w macierzy jest inne bo od 1 a nie od 0

        return res
    
    return laplace_rek(T, n)

T = [
    [1, 2, 3, 4, 3],
    [5, 6, 7, 8, 9],
    [9, 10, 11, 1, 10],
    [13, 14, 15, 16, 15],
    [11, 12, 33, 44, -67]
]

print(wyznacznik(T))