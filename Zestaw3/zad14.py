# Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego,
# że w grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku.
# Wyznaczyć wartości prawdopodobieństwa dla N z zakresu 20-40.

from random import randint

def probability(n):
    days = [randint(1, 365) for _ in range(n)]
    same_day = 0

    for i in range(n):
        for j in range(n):
            if i != j and days[i] == days[j]:
                same_day += 1 # doda 1 osobe a potem druga z pary znowu doda 1 wiec beda 2

    return same_day / n # z automatu beda co najmniej 2 osoby z warunku wyzej (albo zero osob)

def zad14():
    probabilities = [0] * 21
    i = 0
    for n in range(20, 41):
        probabilities[i] = round(probability(n), 2) # type: ignore
        i += 1
    
    return probabilities

print(zad14())