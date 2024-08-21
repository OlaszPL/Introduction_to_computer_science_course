# Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnymi wyznacza długość najdłuższego, spójnego podciągu rosnącego.

def zad9(t):
    n = len(t)
    max_len = 0

    for i in range(n): # od ktorego liczymy podciag
        j = i
        tmp_len = 1 # bo sam jeden element tez ma dlugosc
        while j + 1 < n and t[j + 1] > t[j]:
            tmp_len += 1
            j += 1
        
        max_len = max(max_len, tmp_len)
    
    return max_len

t = [6, 7, 0, 2, 3, 4, 6, 8, 9, 12, 33, 5, 6]

print(zad9(t))