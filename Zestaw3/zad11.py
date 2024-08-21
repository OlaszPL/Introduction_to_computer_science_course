# Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza długość najdłuższego, spójnego podciągu geometrycznego.

def zad11(t):
    n = len(t)
    max_len = 0

    for i in range(n):
        tmp_len = 0
        j = i
        if j + 1 < n and t[j] != 0:
            q = t[j + 1] / t[j]
            tmp_len = 2
            j += 1
            while j + 1 < n and t[j + 1] == q * t[j]:
                    tmp_len += 1
                    j += 1
            
            max_len = max(max_len, tmp_len)
    
    return max_len

t = [5, 24, 656, 12, 36, 108, 346, 6567, 2134]

print(zad11(t))