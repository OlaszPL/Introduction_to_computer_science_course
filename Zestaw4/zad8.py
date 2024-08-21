# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która w poszukuje w tablicy najdłuższego
# ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego co najmniej 3 elementy. Do funkcji należy przekazać tablicę.
# Funkcja powinna zwrócić informacje czy udało się znaleźć taki ciąg oraz długość tego ciągu.
# zawsze mogę wziąć co najmniej 2 elementy

def zad8(T):
    n = len(T)
    max_len = 0
    # zawsze jeden ten sam ruch
    for row in range(n - 1):
        for column in range(n - 1):
            i = 1
            q = T[row + i][column + i] / T[row][column]
            cnt = 2
            while row + i + 1 < n and column + i + 1 < n:
                if T[row + i + 1][column + i + 1] == q * T[row + i][column + i]:
                    cnt += 1
                i += 1

            if cnt >= 3:
                max_len = max(max_len, cnt)
    
    return max_len >= 3, max_len

T = [[1, 2, 3, 4],
     [3, 3, 4, 5],
     [4, 2, 9, 8],
     [12,6, 9, 27]]

print(zad8(T))