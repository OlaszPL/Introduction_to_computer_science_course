# W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
# nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra
# liczby na polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze
# do obranego celu (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu.
# Dana jest globalna tablica T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę.
# Lewy górny narożnik ma współrzędne w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może
# dostać się z pola w,k do prawego dolnego narożnika.

# nie mozemy sie cofac, wiec tylko 3 ruchy: w prawo, na ukos w prawo, w dol

from math import log10

def is_possible_move(first_val, next_val):
    return (first_val % 10) < (next_val // 10 ** (int(log10(next_val))))

def zad18(T, w, k):
    n = len(T)
    
    def rek(T, n, w, k):
        if k == w == n - 1:
            return True
        if w + 1 < n and k + 1 < n and is_possible_move(T[w][k], T[w + 1][k + 1]):
            if rek(T, n, w + 1, k + 1):
                return True
        if w + 1 < n and is_possible_move(T[w][k], T[w + 1][k]):
            if rek(T, n, w + 1, k):
                return True
        if k + 1 < n and is_possible_move(T[w][k], T[w][k + 1]):
            if rek(T, n, w, k + 1):
                return True
        
        return False
    
    return rek(T, n, w, k)

# T = [
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [9, 2, 11, 12, 13, 14, 15, 16],
#     [1, 1, 33, 20, 21, 22, 23, 24],
#     [1, 26, 42, 28, 29, 30, 31, 32],
#     [33, 34, 1, 36, 37, 38, 39, 40],
#     [41, 42, 2, 44, 75, 46, 47, 48],
#     [49, 50, 3, 52, 53, 64, 55, 56],
#     [57, 58, 2, 60, 61, 62, 53, 64]
# ]

T =[[52, 2, 6, 2, 3, 3, 16, 5],
    [52, 2, 6, 2, 3, 3, 16, 5],
    [33, 52, 32, 34, 3, 2, 1, 6],
    [44, 2, 52, 4, 17, 13, 11, 33],
    [55, 86, 7, 52, 8, 9, 12, 76],
    [66, 3, 2, 6, 52, 96, 8, 87],
    [77, 31, 39, 76, 52, 52, 82, 22],
    [88, 6, 9, 13, 17, 28, 52, 52]]

print(zad18(T, 0, 0))