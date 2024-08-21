# Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami naturalnymi po spirali.
# od zewnątrz do środka

def spiral(T):
    n = len(T)
    num, lim = 1, 0
    row, column = 0, 0

    for row in range(n // 2 + 1):
        for column in range(lim, n - lim): # ostatnie column zostanie przekazane do nastepnego fora, nie jest to zmiana izolowana w obrebie petli
            T[row][column] = num
            num += 1

        for row in range(lim + 1, n - lim): # w kazdej kolejnej przy num = 50 juz sie nie wypelniaja bo jest przedzial w range jakby (1,1) i to juz sie nie wykona
            T[row][column] = num
            num += 1

        for column in range(n - lim - 2, lim - 1, -1):
            T[row][column] = num
            num += 1

        for row in range(n - lim - 2, lim, -1):
            T[row][column] = num
            num += 1
    
        lim += 1

        
    # return t

T = [[0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]]

# T = [[0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0]]

spiral(T)

print(*T, sep='\n')