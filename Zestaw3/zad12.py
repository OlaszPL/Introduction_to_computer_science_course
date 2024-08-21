# Proszę napisać program, który wypełnia N-elementową tablicę t pseudolosowymi
# liczbami nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy
# długością najdłuższego znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy,
# a długością najdłuższego ciągu arytmetycznego o ujemnej różnicy, przy założeniu,
# że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych indeksach.

from random import randrange

def zad12(n):
    t = [randrange(1, 99 + 1, 2) for _ in range(n)]
    max_len_plus, max_len_minus = 0, 0

    for i in range(n):
        j = i
        tmp_len_plus, tmp_len_minus = 0, 0
        if j + 1 < n:
            r = t[j + 1] - t[j]
            j += 1
            if r > 0:
                tmp_len_plus = 2 # bo sa 2 wyrazy juz
                while j + 1 < n and t[j + 1] == t[j] + r:
                    tmp_len_plus += 1
                    j += 1
                
                max_len_plus = max(max_len_plus, tmp_len_plus)
            elif r < 0:
                tmp_len_minus = 2
                while j + 1 < n and t[j + 1] == t[j] + r:
                    tmp_len_minus += 1
                    j += 1
                
                max_len_minus = max(max_len_minus, tmp_len_minus)

    return abs(max_len_plus - max_len_minus)

print(zad12(1000))