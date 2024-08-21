# W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
# nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra
# liczby na polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze
# do obranego celu (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu.
# Dana jest globalna tablica T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę.

# Zadanie jak powyżej. Funkcja sprawdzająca czy król może dostać się z pola w,k do któregokolwiek z narożników.

# Zadanie jak powyżej. Funkcja powinna dostarczyć drogę króla w postaci tablicy zawierającej
# kierunki (liczby od 0 do 7) poszczególnych ruchów króla do wybranego celu. Zal:

# 0 1 2
# 7   3
# 6 5 4

from math import log10

def make_result(T):
    cnt = 0
    for el in T:
        if el != -1:
            cnt += 1
        else:
            break
    
    res = [0 for _ in range(cnt)]

    for i in range(cnt):
        res[i] = T[i]
    
    return res

def is_possible_move(first_val, next_val):
    return (first_val % 10) < (next_val // 10 ** (int(log10(next_val))))

def zad20(T, w, k):
    n = len(T)
    tmp_route = [-1 for _ in range(n*n)]

    def rek1(T, n, w, k, i = 0):
        if k == w == n - 1:
            return True
        
        if w + 1 < n and k + 1 < n and is_possible_move(T[w][k], T[w + 1][k + 1]):
            tmp_route[i] = 4
            if rek1(T, n, w + 1, k + 1, i + 1):
                return True
            tmp_route[i] = -1
            
        if w + 1 < n and is_possible_move(T[w][k], T[w + 1][k]):
            tmp_route[i] = 5
            if rek1(T, n, w + 1, k, i + 1):
                return True
            tmp_route[i] = -1

        if k + 1 < n and is_possible_move(T[w][k], T[w][k + 1]):
            tmp_route[i] = 3
            if rek1(T, n, w, k + 1, i + 1):
                return True
            tmp_route[i] = -1
            
        return False
    
    def rek2(T, n, w, k, i = 0):
        if w == n - 1 and k == 0:
            return True
    
        if w + 1 < n and is_possible_move(T[w][k], T[w + 1][k]):
            tmp_route[i] = 5
            if rek2(T, n, w + 1, k, i + 1):
                return True
            tmp_route[i] = -1
        
        if w + 1 < n and -1 < k - 1 and is_possible_move(T[w][k], T[w + 1][k - 1]):
            tmp_route[i] = 6
            if rek2(T, n, w + 1, k - 1, i + 1):
                return True
            tmp_route[i] = -1
            
        if -1 < k - 1 and is_possible_move(T[w][k], T[w][k - 1]):
            tmp_route[i] = 7
            if rek2(T, n, w, k - 1, i + 1):
                return True
            tmp_route[i] = -1
        
        return False

    def rek3(T, n, w, k, i = 0):
        if w == 0 and k == 0:
            return True

        if -1 < k - 1 and is_possible_move(T[w][k], T[w][k - 1]):
            tmp_route[i] = 7
            if rek3(T, n, w, k - 1, i + 1):
                return True
            tmp_route[i] = -1
        
        if -1 < w - 1 and -1 < k - 1 and is_possible_move(T[w][k], T[w - 1][k - 1]):
            tmp_route[i] = 0
            if rek3(T, n, w - 1, k - 1, i + 1):
                return True
            tmp_route[i] = -1
        
        if -1 < w - 1 and is_possible_move(T[w][k], T[w - 1][k]):
            tmp_route[i] = 1
            if rek3(T, n, w - 1, k, i + 1):
                return True
            tmp_route[i] = -1
            
        return False
    
    def rek4(T, n, w, k, i = 0):
        if w == 0 and k == n - 1:
            return True
        
        if -1 < w - 1 and -1 < k - 1 and is_possible_move(T[w][k], T[w - 1][k - 1]):
            tmp_route[i] = 0
            if rek4(T, n, w - 1, k - 1, i + 1):
                return True
            tmp_route[i] = -1

        if -1 < w - 1 and k + 1 < n and is_possible_move(T[w][k], T[w - 1][k + 1]):
            tmp_route[i] = 2
            if rek4(T, n, w - 1, k + 1, i + 1):
                return True
            tmp_route[i] = -1

        if k + 1 < n and is_possible_move(T[w][k], T[w][k + 1]):
            tmp_route[i] = 3
            if rek4(T, n, w, k + 1, i + 1):
                return True
            tmp_route[i] = -1
        
        return False
    
    if rek1(T, n, w, k):
        print(make_result(tmp_route))
        return True
    elif rek2(T, n, w, k):
        print(make_result(tmp_route))
        return True
    elif rek3(T, n, w, k):
        print(make_result(tmp_route))
        return True
    elif rek4(T, n, w, k):
        print(make_result(tmp_route))
        return True
    
    return False
    
T =[[52, 2, 6, 2, 3, 3, 16, 5],
    [52, 2, 6, 2, 3, 3, 16, 5],
    [33, 52, 32, 34, 3, 2, 1, 6],
    [44, 2, 52, 4, 17, 13, 11, 33],
    [55, 86, 7, 52, 8, 9, 12, 76],
    [66, 3, 2, 6, 52, 96, 8, 87],
    [77, 31, 39, 76, 52, 52, 82, 22],
    [88, 6, 9, 13, 17, 28, 52, 52]]

print(zad20(T, 3, 2))