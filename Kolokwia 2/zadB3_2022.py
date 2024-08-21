# Na szachownicy o wymiarach N × N umieszczono pewną liczbę pionków. Położenie pionków opisuje lista [(w0, k0),(w1, k1),(w2, k2), ...].
# W lewym górnym rogu szachownicy (o współrzędnych 0, 0) znajduje się
# wieża, która musi dotrzeć do prawego dolnego rogu szachownicy. Wieża może wykonywać ruchy w prawo lub
# w dół szachownicy i nie może zbijać pionków. Proszę napisać funkcję rook(N,L), która zwróci minimalną
# liczbę ruchów jakie musi wykonać wieża aby dotrzeć do celu. Do funkcji należy przekazać wyłącznie dwa
# parametry: rozmiar szachownicy N oraz listę L zawierającą położenia pionków. Jeżeli dotarcie do celu nie
# jest możliwe funkcja powinna zwrócić wartość None.

def rook(N, L):
    l = len(L)
    min_moves = float('inf')

    def rek(cnt = 0, r = 0, c = 0):
        nonlocal min_moves
        if r == c == N - 1:
            min_moves = min(min_moves, cnt)
            return
        
        for r1 in range(r + 1, N):
            flag = False
            for el in L:
                if el[0] == r1 and el[1] == c:
                    flag = True
                    break

            if flag:
                break
            else:
                rek(cnt + 1, r1, c)
        
        for c1 in range(c + 1, N):
            flag = False
            for el in L:
                if el[0] == r and el[1] == c1:
                    flag = True
                    break

            if flag:
                break
            else:
                rek(cnt + 1, r, c1)

        return
    
    rek()

    return min_moves if min_moves < float('inf') else None

L = [(2, 0), (2, 1), (0, 2), (3, 2), (1, 3)]
print(rook(4, L))