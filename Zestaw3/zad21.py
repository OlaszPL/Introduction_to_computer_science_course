# Dana jest tablica T[N] wypełniona niepowtarzającymi się liczbami naturalnymi. Proszę zaimplementować
# funkcję trojki(T) która zlicza wszystkie trójki liczb, które spełniają następujące warunki:
# (1) największym wspólnym dzielnikiem trzech liczb jest liczba 1,
# (2) pomiędzy dwoma kolejnymi elementami trójki może być co najwyżej jedna przerwa.
# Funkcja powinna zwrócić liczbę znalezionych trójek.

def nwd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

def trojki(T):
    n = len(T)
    cnt = 0

    for i in range(n):
        j = i
        if j + 1 < n and nwd(T[j], T[j + 1]) == 1:
            j += 1
            if j + 1 < n and nwd(T[j], T[j + 1]) == 1:
                cnt += 1
        else:
            j += 1
            if j + 1 < n and -1 < j - 1 and nwd(T[j - 1], T[j + 1]) == 1:
                j += 1
                if j + 1 < n and nwd(T[j], T[j + 1]) == 1:
                    cnt += 1
                else:
                    j += 1
                    if j + 1 < n and -1 < j - 1 and nwd(T[j - 1], T[j + 1]) == 1:
                        cnt += 1

    return cnt

T = [20, 22, 2, 3, 5, 100, 17, 1 ]
# T = [2, 4, 6, 8, 2, 6, 3, 15, 5]

print(trojki(T))