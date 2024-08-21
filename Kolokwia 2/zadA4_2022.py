# Na szachownicy o rozmiarach N × N reprezentowanej przez tablicę T[N][N] umieszczono pewną liczbę
# skoczków. Położenie skoczka w tablicy oznaczono liczbą 1, puste pola oznaczono liczbą 0.
# Część pustych pól na szachownicy jest szachowana przez znajdujące się na niej skoczki.
# Proszę zaproponować funkcję place(T), która znajdzie na szachownicy puste pole położone najbliżej
# środka szachownicy, takie że umieszczenie tam skoczka maksymalnie zwiększy liczbę szachowanych pustych pól.
# Do funkcji przekazujemy tablicę T zawierającą położenie skoczków. Funkcja powinna zwrócić pole
# (wiersz, kolumna), na którym należy umieścić skoczka.
# Odległość pomiędzy polami: (w1, k1) i (w2, k2) jest równa max(abs(w1 − w2), abs(k1 − k2))
# Uwagi:
# • Można założyć, że rozmiar N tablicy jest liczbą nieparzystą większą od 2.

def place(T):
    n = len(T)
    szachowane = [[False for _ in range(n)] for _ in range(n)]
    szachowanie = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

    for r in range(n): # zaznaczy pola szachowane przez skoczki co sa juz wczesniej na szachownicy
        for c in range(n):
            if T[r][c] == 1:
                for szach in szachowanie:
                    if -1 < r + szach[0] < n and -1 < c + szach[1] < n:
                        szachowane[r + szach[0]][c + szach[1]] = True

    odleglosc = float('inf')
    ilosc_zszachownaych = -float('inf')
    res_r, res_c = 0, 0

    for r in range(n):
        for c in range(n):
            if T[r][c] == 0:
                tmp_cnt = 0
                for szach in szachowanie:
                    if -1 < r + szach[0] < n and -1 < c + szach[1] < n and not szachowane[r + szach[0]][c + szach[1]]:
                        tmp_cnt += 1
                if tmp_cnt > 0:
                    tmp_odleglosc = max(abs(r - (n // 2)), abs(c - (n // 2)))
                    if tmp_odleglosc <= odleglosc and tmp_cnt >= ilosc_zszachownaych:
                        odleglosc = tmp_odleglosc
                        ilosc_zszachownaych = tmp_cnt
                        res_r, res_c = r, c
                           
    return res_r, res_c

T = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

print(place(T))