# Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi
# zawierającymi koszt przebywania na danym polu szachownicy.
# Król szachowy znajduje się w wierszu 0 i kolumnie k. Król musi w dokładnie 7 ruchach
# dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
# koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k.
# Koszt przebywania na polu startowym i ostatnim także wliczamy do kosztu przejścia.

# ma 7 ruchów, więc nie ma sensu by poruszał się w prawo, lewo albo do góry

def zad3(T, k):
    n = len(T)
    min_cost = float('inf')

    def rek(T, n, k, w = 0, cost = T[0][k]):
        nonlocal min_cost

        if cost > min_cost:
            return
        if w == n - 1:
            min_cost = min(min_cost, cost)
            return
        
        if k != 0:
            rek(T, n, k - 1, w + 1, cost + T[w + 1][k - 1])
        if k != n - 1:
            rek(T, n, k + 1, w + 1, cost + T[w + 1][k + 1])
        
        rek(T, n, k, w + 1, cost + T[w + 1][k])
    
    rek(T, n, k)

    return min_cost

T = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 1, 11, 12, 13, 14, 15, 16],
    [1, 1, 19, 20, 21, 22, 23, 24],
    [1, 26, 1, 28, 29, 30, 31, 32],
    [33, 34, 1, 36, 37, 38, 39, 40],
    [41, 42, 2, 44, 45, 46, 47, 48],
    [49, 50, 3, 52, 53, 54, 55, 56],
    [57, 58, 2, 60, 61, 62, 63, 64]
]

print(zad3(T, 3))