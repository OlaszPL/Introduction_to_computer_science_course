# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca liczbę par elementów, o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka
# szachowego.


def zad19(T, k):
    n = len(T)
    moves = [(1, 2), (-1, 2), (-2, 1), (-2, -1)] # bierzemy tylko polowe ruchow skoczka by zagwaranowac ze sie nie powtorza
    cnt = 0

    for row in range(n):
        for column in range(n):
            for move in moves:
                if -1 < row + move[0] < n and -1 < column + move[1] < n and T[row + move[0]][column + move[1]] * T[row][column] == k:
                    cnt += 1
    
    return cnt

T = [
[1,     2,  3,  4, 5, 6, 7 ],
[24, 25, 26, 27, 28, 29, 8 ],
[23, 40, 41, 42, 43, 30, 9 ],
[22, 39, 48, 49, 44, 31, 10],
[21, 38, 47, 46, 45, 32, 11],
[20, 37, 36, 35, 34, 33, 12],
[19, 18, 17, 168, 15, 14, 13]]

print(zad19(T, 1372))