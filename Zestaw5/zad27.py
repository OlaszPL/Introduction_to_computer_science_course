# Kwadrat jest opisywany czwórką liczb całkowitych (x1, x2, y1, y2), gdzie x1, x2, y1, y2 oznaczają
# proste ograniczające kwadrat x1 < x2, y1 < y2. Dana jest tablica T zawierająca opisy N kwadratów.
# Proszę napisać funkcję, która zwraca wartość logiczną True, jeśli danej tablicy można znaleźć
# 13 nienachodzących na siebie kwadratów, których suma pól jest równa 2012
# i False w przeciwnym przypadku.

def are_in_collision(sq1, sq2):
    if sq2[0] >= sq1[1]:
        return False
    if sq1[0] >= sq2[1]:
        return False
    if sq2[2] >= sq1[3]:
        return False
    if sq1[2] >= sq2[3]:
        return False
    return True

def zad27(T):
    n = len(T)

    def rek(T, n, suma_pol = 0, i = 0, collisions = [False] * n, cnt = 0):
        if suma_pol > 2012 or cnt > 13:
            return False
        if suma_pol == 2012 and cnt == 13:
            return True
        if i == n:
            return False
        
        collisions_copy = collisions[:]

        for j in range(i + 1, n):
            if not collisions[j] and are_in_collision(T[i], T[j]):
                collisions_copy[j] = True
        
        if not collisions[i]:
            if rek(T, n, suma_pol + (T[i][1] - T[i][0]) * (T[i][3] - T[i][2]), i + 1, collisions_copy, cnt + 1):
                return True
            
        return rek(T, n, suma_pol, i + 1, collisions, cnt)
        
    return rek(T, n)

