# Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego.

def skoczek(n):
    T = [[0 for _ in range(n)] for _ in range(n)]
    
    def printT(T):
        print(*T, sep='\n')
        print('\n')

    def move(T, n, row, col, i): # sprawdza ruch dla danego i i jak jest możliwy to zwraca krotkę z nastepnym rzedem i kolumna
        dir_row = (-2, -1, 1, 2, 2, 1, -1, -2) # możliwe ruchy w rzędzie
        dir_col = (1, 2, 2, 1, -1, -2, -2, -1) # możliwe ruchy w kolumnach

        new_row = row + dir_row[i]
        new_col = col + dir_col[i]

        if -1 < new_row < n and -1 < new_col < n and T[new_row][new_col] == 0:
            return new_row, new_col
        
        return False
    
    def rek(T, n, row, col, cnt = 1):
        if cnt == n*n: # zapisane wszystkie pola
            T[row][col] = cnt # bo nie printowalo ostatniej liczby
            printT(T)
            T[row][col] = 0 # bo zepsuje bez tego backtracking
            return True

        for i in range(8):
            if r := move(T, n, row, col, i):
                T[row][col] = cnt
                if rek(T, n, r[0], r[1], cnt + 1):
                    return True

                T[row][col] = 0 # backtracking
        
    rek(T, n, 0, 0)

skoczek(8)