# Problem 8 Hetmanów - problem polegający na wyznaczeniu liczby różnych rozmieszczeń
# ośmiu hetmanów na tradycyjnej szachownicy 8×8 tak, aby wzajemnie się nie atakowały.

# Wiadomym jest, że każdy z hetmanów musi być w innym wierszu.
# Pozycję hetmanów przedstawi się jako tablicę 1 wymiarową, gdzie indeks = wierszowi, a wartość kolumnie.

def zad15(n): # n - wymiar szachownicy, hetmanów jest też tyle co n

    def isPossible(n, r, c, pos):
        for i in range(n):
            if pos[i] != -1:
                vector_x = abs(r - i)
                vector_y = abs(pos[i] - c)
                if pos[i] == c or vector_x == vector_y: # bo wartosci to kolumny
                    return False
            
        return True

    def rek(n, pos = [-1] * n, r = 0):
        cnt = 0
        if r == n:
            return 1

        for c in range(n):
            if isPossible(n, r, c, pos):
                pos[r] = c
                cnt += rek(n, pos, r + 1)
                pos[r] = -1
        
        return cnt
    
    return rek(n)

print(zad15(8))