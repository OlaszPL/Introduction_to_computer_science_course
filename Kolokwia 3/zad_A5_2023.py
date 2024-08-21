# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi, na której możemy wykonywać operacje:
# • rotacji elementów danego wiersza w prawo,
# • rotacji elementów danej kolumny w dół.
# Tablicę taką nazywamy kwadratem magicznym, wtedy gdy suma elementów w każdym wierszu i każdej kolumnie
# jest jednakowa. Proszę napisać funkcję magic(T), która sprawdza czy po wykonaniu dokładnie dwóch
# dowolnych operacji tablica T stanie się kwadratem magicznym. Funkcja powinna zwrócić True albo False.
# Na przykład dla tablicy:
# 3 11 14 17
# 6 12 7 9
# 10 8 16 13
# 5 15 4 2
# po wykonaniu rotacji wiersza 0, następnie rotacji kolumny 2, tablica będzie kwadratem magicznym.

def check(T):
    n = len(T)
    sum = 0
    for i in range(n):
        sum += T[i][0]

    for r in range(n):
        tmp1, tmp2 = 0, 0
        for c in range(n):
            tmp1 += T[r][c]
            tmp2 += T[c][r]
        
        if tmp1 != tmp2 != sum:
            return False
        
    return True

def rotate_right(T, r):
    n = len(T)
    i = 0
    tmp = T[r][-1]
    while i < n:
        T[r][i], tmp = tmp, T[r][i]
        i += 1

    return T

def rotate_left(T, r):
    n = len(T)
    i = 1
    tmp = T[r][0]
    while n - i > -1:
        T[r][n - i], tmp = tmp, T[r][n - i]
        i += 1
    
    return T

def rotate_down(T, c):
    n = len(T)
    i = 0
    tmp = T[-1][c]
    while i < n:
        T[i][c], tmp = tmp, T[i][c]
        i += 1

    return T

def rotate_up(T, c):
    n = len(T)
    i = 1
    tmp = T[0][c]
    while n - i > -1:
        T[n - i][c], tmp = tmp, T[n - i][c]
        i += 1
    
    return T

def magic(T):
    n = len(T)

    opers = [(0, 0), (0, 1), (1, 0), (1, 1)] # 0 - w dół, 1 - w prawo

    for r in range(n):
        for c in range(n):
            for op in opers:
                if op[0] == 0:
                    rotate_down(T, c)
                else:
                    rotate_right(T, r)
                if op[1] == 0:
                    rotate_down(T, c)
                else:
                    rotate_right(T, r)
                if check(T):
                    print(*T, sep = '\n')
                    return True
                if op[1] == 0: # koniecznie sprawdzać na odwrót
                    rotate_up(T, c)
                else:
                    rotate_left(T, r)
                if op[0] == 0:
                    rotate_up(T, c)
                else:
                    rotate_left(T, r)
    
    return False
            
T = [
    [3, 11, 14, 17],
    [6, 12, 7, 9],
    [10, 8, 16, 13],
    [5, 15, 4, 2]
]

print(magic(T))