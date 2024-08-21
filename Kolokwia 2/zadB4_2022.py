# Na szachownicy o rozmiarach N × N reprezentowanej przez tablicę T[N][N] umieszczono pewną liczbę
# wież szachowych tak, że każde z wolnych pól na szachownicy jest szachowane. Położenie wież w tablicy
# oznaczono wartościami True. Przyszedł zły człowiek i zmienił położenie jednej z wież na szachownicy, tak że
# nie wszystkie wolne pola są szachowane. Proszę zaproponować funkcję move(T), która znajdzie przeniesienie
# jednej wieży, tak aby ponownie wszystkie pola były szachowane. Do funkcji przekazujemy tablicę T zawierającą położenie wież po zmianie położenia wieży.
# Funkcja powinna zwrócić dwa pola (wiersz, kolumna) – skąd i dokąd należy przenieść wieżę.

def check_table(T, n): # dostaje tablicę wież i sprawdza czy wszystkie pola szachowane poza tymi gdzie stoją wieże
    for r in range(n):
        flag1, flag2 = False, False
        for c in range(n):
            if T[r][c]:
                flag1 = True
            if T[c][r]:
                flag2 = True
        
        if not flag1 or not flag2:
            return False
        
    return True

def move(T):
    n = len(T)

    for r in range(n): # szukamy gdzie jest wieża
        for c in range(n):
            if T[r][c]:
                for r2 in range(n): # szukamy dla niej nowego, pustego miejsca
                    for c2 in range(n):
                        if not T[r2][c2]:
                            T[r][c], T[r2][c2] = False, True
                            if check_table(T, n):
                                T[r][c], T[r2][c2] = True, False # wypada zostawic niezmieniona tablice
                                return (r, c), (r2, c2)
                            T[r][c], T[r2][c2] = True, False # cofamy zmiany
    
    return None

T=[[False,True,False,False,True],
   [False,False,False,True,False],
   [True,False,False,False,False],
   [False,False,False,False,False],
   [False,True,False,False,False]]

print(move(T))