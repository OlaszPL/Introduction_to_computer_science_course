# Na szachownicy o wymiarach N × N umieszczono pewną liczbę pionków. Położenie pionków opisuje lista
# [(w0, k0),(w1, k1),(w2, k2), ...]. W lewym górnym rogu szachownicy (o współrzędnych 0, 0) znajduje się
# król, który musi dotrzeć do prawego dolnego rogu szachownicy. Król może wykonywać ruchy w prawo, w
# dół lub w górę szachownicy, nie może zbijać pionków ani wracać na pole, na którym już był. Proszę
# napisać funkcję king(N,L), która zwróci maksymalną liczbę ruchów jakie może wykonać król na drodze
# do celu. Do funkcji należy przekazać wyłącznie dwa parametry:
# rozmiar szachownicy N oraz listę L zawierającą położenia pionków.
# Jeżeli dotarcie do celu nie jest możliwe funkcja powinna zwrócić wartość None.

def is_correct(r, c, L, l, N, prev_moves):
    if -1 < r < N and -1 < c < N and not prev_moves[r][c]:
        for i in range(l):
            if r == L[i][0] and c == L[i][1]:
                return False
        
        return True
    else:
        return False

def king(N, L): # N - rozmiar szachownicy, L - tablica krotek z pionkami
    l = len(L)
    max_moves = 0
    prev_moves = [[False for _ in range(N)] for _ in range(N)] # bez tego ma mozliwosc sie cofac

    def rek(tmp_cnt = 0, r = 0, c = 0):
        nonlocal max_moves
        if r == c == N - 1:
            max_moves = max(max_moves, tmp_cnt)
            return
        moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0)]

        for move in moves:
            if is_correct(r + move[0], c + move[1], L, l, N, prev_moves):
                prev_moves[r][c] = True
                rek(tmp_cnt + 1, r + move[0], c + move[1])
                prev_moves[r][c] = False # backtracking
        
        return
    
    rek()
    
    return max_moves if max_moves != 0 else None

L = [(1, 2), (2, 3), (0, 1), (1, 0), (2, 2), (3, 1)]
print(king(4, L))