# W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
# nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra
# liczby na polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze
# do obranego celu (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu.
# Dana jest globalna tablica T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę.

# Zadanie jak powyżej. Funkcja sprawdzająca czy król może dostać się z pola w,k do któregokolwiek z narożników.

from math import log10

def is_possible_move(first_val, next_val):
    return (first_val % 10) < (next_val // 10 ** (int(log10(next_val))))

def zad19(T, w, k):
    n = len(T)
    # można było zrobić z tablicą krotek

    def rek1(T, n, w, k): # wk - wiersz koncowy, kk - kolumna koncowa
        if k == w == n - 1:
            return True
        
        if w + 1 < n and k + 1 < n and is_possible_move(T[w][k], T[w + 1][k + 1]):
            if rek1(T, n, w + 1, k + 1):
                return True
            
        if w + 1 < n and is_possible_move(T[w][k], T[w + 1][k]):
            if rek1(T, n, w + 1, k):
                return True
            
        if k + 1 < n and is_possible_move(T[w][k], T[w][k + 1]):
            if rek1(T, n, w, k + 1):
                return True
            
        return False
    
    def rek2(T, n, w, k):
        if w == n - 1 and k == 0:
            return True
    
        if w + 1 < n and is_possible_move(T[w][k], T[w + 1][k]):
            if rek2(T, n, w + 1, k):
                return True
        
        if w + 1 < n and -1 < k - 1 and is_possible_move(T[w][k], T[w + 1][k - 1]):
            if rek2(T, n, w + 1, k - 1):
                return True
            
        if -1 < k - 1 and is_possible_move(T[w][k], T[w][k - 1]):
            if rek2(T, n, w, k - 1):
                return True
        
        return False

    def rek3(T, n, w, k):
        if w == 0 and k == 0:
            return True

        if -1 < k - 1 and is_possible_move(T[w][k], T[w][k - 1]):
            if rek3(T, n, w, k - 1):
                return True
        
        if -1 < w - 1 and -1 < k - 1 and is_possible_move(T[w][k], T[w - 1][k - 1]):
            if rek3(T, n, w - 1, k - 1):
                return True
        
        if -1 < w - 1 and is_possible_move(T[w][k], T[w - 1][k]):
            if rek3(T, n, w - 1, k):
                return True
            
        return False
    
    def rek4(T, n, w, k):
        if w == 0 and k == n - 1:
            return True
        
        if -1 < w - 1 and -1 < k - 1 and is_possible_move(T[w][k], T[w - 1][k - 1]):
            if rek4(T, n, w - 1, k - 1):
                return True

        if -1 < w - 1 and k + 1 < n and is_possible_move(T[w][k], T[w - 1][k + 1]):
            if rek4(T, n, w - 1, k + 1):
                return True

        if k + 1 < n and is_possible_move(T[w][k], T[w][k + 1]):
            if rek4(T, n, w, k + 1):
                return True
        
        return False
    
    if rek1(T, n, w, k):
        return True
    elif rek2(T, n, w, k):
        return True
    elif rek3(T, n, w, k):
        return True
    else:
        return rek4(T, n, w, k)
    
T =[[52, 2, 6, 2, 3, 3, 16, 5],
    [52, 2, 6, 2, 3, 3, 16, 5],
    [33, 52, 32, 34, 3, 2, 1, 6],
    [44, 2, 52, 4, 17, 13, 11, 33],
    [55, 86, 7, 52, 8, 9, 12, 76],
    [66, 3, 2, 6, 52, 96, 8, 87],
    [77, 31, 39, 76, 52, 52, 82, 22],
    [88, 6, 9, 13, 17, 28, 52, 52]]

print(zad19(T, 0, 0))