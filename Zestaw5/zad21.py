# Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
# wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
# elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
# wartość sumy, funkcja powinna zwrócić wartość typu bool.

def zad21(T, sum):
    n = len(T)
    Trow = [False for _ in range(n)] # tablica przechowujaca niezuzyte rzedy
    Tcol = [False for _ in range(n)] # tablica przechowujaca niezuzyte kolumny

    def rek(T, Trow, Tcol, sum, n):

        if sum < 0:
            return False
        if sum == 0:
            return True

        for r in range(n):
            if not Trow[r]:
                for c in range(n):
                    if not Tcol[c]:
                        Trow[r], Tcol[c] = True, True
                        if rek(T, Trow, Tcol, sum - T[r][c], n):
                            return True
                        
                        Trow[r], Tcol[c] = False, False # backtracking, cofamy zmiany
        
        return False
        
    return rek(T, Trow, Tcol, sum, n) 

T = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48],
    [49, 50, 51, 52, 53, 54, 55, 56],
    [57, 58, 59, 60, 61, 62, 63, 64]
]

print(zad21(T, 243))