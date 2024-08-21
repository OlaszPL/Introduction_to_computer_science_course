# Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza długość najdłuższego, spójnego podciągu arytmetycznego.

def zad10(t):
    n = len(t)
    max_len = 0

    for i in range(n):
        j = i
        tmp_len = 0
        if j + 1 < n:
            r = t[j + 1] - t[j]
            j += 1
            tmp_len = 2 # bo do wyznaczenia r potrzebne sa 2 wyrazy
            while j + 1 < n and t[j + 1] == t[j] + r:
                tmp_len += 1
                j += 1
        
        max_len = max(max_len, tmp_len)

    return max_len

t = [4, 5, 7, 10, 13, 16, 7, 43, 6]

print(zad10(t))