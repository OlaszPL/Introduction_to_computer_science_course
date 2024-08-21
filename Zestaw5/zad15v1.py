# Problem 8 Hetmanów - problem polegający na wyznaczeniu liczby różnych rozmieszczeń
# ośmiu hetmanów na tradycyjnej szachownicy 8×8 tak, aby wzajemnie się nie atakowały.

def ustaw_hetmana(T, n, r, c):
    for i in range(n):
        T[r][i] = True
        T[i][c] = True
        if r + i < n and c + i < n:
            T[r + i][c + i] = True
        if -1 < r - i and -1 < c - i:
            T[r - i][c - i] = True
        if -1 < r - i and c + i < n:
            T[r - i][c + i] = True
        if r + i < n and -1 < c - i:
            T[r + i][c - i] = True
    

def zad15(n, k): # n - wymiar szachownicy, k = ilosc hetmanow
    T = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0

    def rek(T, n, k, r = 0):
        nonlocal cnt
        if k == 0:
            cnt += 1
            return True
        if r == n:
            return False
        
        for c in range(n):
            if not T[r][c]:
                T_copy = [row[:] for row in T]
                ustaw_hetmana(T_copy, n, r, c)
                rek(T_copy, n, k - 1, r + 1)

        return False
    
    rek(T, n, k)

    return cnt

print(zad15(8, 8))