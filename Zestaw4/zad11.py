# Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane są liczby
# są identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona liczbami
# naturalnymi. Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy sąsiaduje wyłącznie z
# przyjaciółkami.

# sąsiaduje --> wielowymiarowo

def is_a_friend(a, b): # iteracje traktujemy jako cyfra z liczby
    t_a, t_b = [False] * 10, [False] * 10 # o tyle jest cyfr 0-9

    while a > 0:
        t_a[a % 10] = True
        a //= 10

    while b > 0:
        t_b[b % 10] = True
        b //= 10

    return t_a == t_b

def check_neighbours(T, row, column, n): # sprawdzi sasiadow dla danej liczby
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # n = len(T), juz przyszlo z funkcji wczesniej

    for direction in directions: # wybiera krotki
        if -1 < row + direction[0] < n and -1 < column + direction[1] < n: # bo n > indeksy
            if not is_a_friend(T[row][column], T[row + direction[0]][column + direction[1]]):
                return False
    
    return True

def zad11(T):
    n = len(T)
    cnt = 0
    for row in range(n):
        for column in range(n):
            if check_neighbours(T, row, column, n):
                cnt += 1

    return cnt



T = [[123, 321, 111, 567], # tablice najlepiej zapisac tak to mniej sie glupieje
     [312, 123, 231, 890],
     [123, 231, 576, 987],
     [345, 321, 547, 234]]

print(zad11(T))