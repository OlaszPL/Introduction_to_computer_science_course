# Mamy zdeﬁniowaną n-elementową tablicę liczb całkowitych. Proszę napisać funkcję zwracającą wartość
# typu bool oznaczającą, czy w tablicy istnieje dokładnie jeden element najmniejszy i dokładnie jeden element największy
# (liczba elementów najmniejszych oznacza liczbę takich elementów o tej samej wartości).

def zad16(t):
    n = len(t)
    biggest = -float('inf')
    lowest = float('inf')

    for i in range(n): # szuka
        if t[i] > biggest:
            biggest = t[i]
        elif t[i] < lowest:
            lowest = t[i]

    cnt_b, cnt_l = 0, 0
    for j in range(n): # sprawdza ilosc
        if t[j] == biggest:
            cnt_b += 1
        elif t[j] == lowest:
            cnt_l += 1
        if cnt_b > 1 or cnt_l > 1:
            return False
    
    return True

t = [0, 1, 2, 3, 8, 5, 6, 7]

print(zad16(t))