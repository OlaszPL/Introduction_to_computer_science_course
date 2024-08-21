# Na szachownicy o wymiarach N × N wypełnionej liczbami naturalnymi > 1 odbywają się wyścigi
# wież. Pierwsza wieża startuje z lewego górnego rogu i ma dotrzeć do prawego dolnego rogu szachownicy.
# Pierwsza wieża może wykonywać tylko ruchy w prawo lub w dół szachownicy. Druga wieża
# startuje z prawego górnego rogu i ma dotrzeć do lewego dolnego rogu szachownicy. Druga wieża
# może wykonywać tylko ruchy w lewo lub w dół szachownicy. Wygrywa wieża, która dotrze do mety
# w mniejszej liczbie ruchów. Wieże mogą wykonać ruch z jednego pola na drugie tylko wtedy, gdy
# liczby na obu polach są względnie pierwsze.
# Proszę napisać funkcję, która dla danej tablicy zwraca numer wieży, która wygra wyścig lub 0, jeżeli
# wyścig będzie nierozstrzygnięty. Można założyć, że podczas wyścigu wieże nie spotkają się na jednym
# polu. Po wykonaniu funkcji zawartość tablicy nie może ulec zmianie.

from random import randint

def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    
    return a

def czy_wzglednie_pierwsze(num1, num2):
    return nwd(num1, num2) == 1

def wyscig(T):
    n = len(T)
    min_cnt1 = float('inf')
    min_cnt2 = float('inf')

    def rek1(r = 0, c = 0, cnt = 0):
        nonlocal min_cnt1
        if r == c == n - 1:
            min_cnt1 = min(min_cnt1, cnt)
            return
        
        for r2 in range(r + 1, n):
            if czy_wzglednie_pierwsze(T[r2][c], T[r][c]):
                rek1(r2, c, cnt + 1)
        
        for c2 in range(c + 1, n):
            if czy_wzglednie_pierwsze(T[r][c2], T[r][c]):
                rek1(r, c2, cnt + 1)
        
        return
    
    def rek2(r = 0, c = n - 1, cnt = 0):
        nonlocal min_cnt2
        if r == n - 1 and c == 0:
            min_cnt2 = min(min_cnt2, cnt)
            return
        
        for r2 in range(r + 1, n):
            if czy_wzglednie_pierwsze(T[r2][c], T[r][c]):
                rek2(r2, c, cnt + 1)

        for c2 in range(c - 1, -1, -1):
            if czy_wzglednie_pierwsze(T[r][c2], T[r][c]):
                rek2(r, c2, cnt + 1)
        
        return
    
    rek1()
    rek2()

    if min_cnt1 < min_cnt2:
        return 1
    elif min_cnt2 < min_cnt1:
        return 2
    else:
        return 0

T = [[randint(2, 10) for _ in range(5)] for _ in range(5)]
print(*T, sep='\n', end='\n\n')
print(wyscig(T))