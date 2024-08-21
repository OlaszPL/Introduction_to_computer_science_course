# W tablicy o rozmiarze N × N wypełnionej liczbami naturalnymi umieszczono dokładnie jeden fragment ciągu
# Fibonacciego o długości co najmniej 3 elementów. Cały fragment leży w jednym z wierszy
# lub kolumn w kierunku rosnącym lub malejącym. Prosze napisać funkcję, która dla zadanej tablicy
# odszuka ten fragment i zwróci jego wartość (sumę).

def is_part_of_fib(num):
    a, b = 1, 1
    while a < num:
        a, b = b, a + b
    
    return a == num

def find_sum_of_fib(T):
    n = len(T)

    for r in range(n):
        for c in range(n - 2):
            if T[r][c] + T[r][c + 1] == T[r][c + 2]:
                cnt = 3
                i = 3
                while c + i < n and T[r][c + i] == T[r][c + i - 1]+ T[r][c + i - 2]:
                    cnt += 1
                    i += 1
                
                if is_part_of_fib(T[r][c]):
                    sum = 0
                    for j in range(cnt):
                        sum += T[r][c + j]
                    
                    return sum
            
            if T[c][r] + T[c + 1][r] == T[c + 2][r]:
                cnt = 3
                i = 3
                while c + i < n and T[c + i][r] == T[c + i - 1][r] + T[c + i - 2][r]:
                    cnt += 1
                    i += 1
                
                if is_part_of_fib(T[c][r]):
                    sum = 0
                    for j in range(cnt):
                        sum += T[c + j][r]
                    
                    return sum
    
    for r in range(n - 1, -1, -1):
        for c in range(n - 1, 1, -1):
            if T[r][c] + T[r][c - 1] == T[r][c - 2]:
                cnt = 3
                i = -3
                while -1 < c + i and T[r][c + i] == T[r][c + i + 1]+ T[r][c + i + 2]:
                    cnt += 1
                    i -= 1
                
                if is_part_of_fib(T[r][c]):
                    sum = 0
                    for j in range(cnt):
                        sum += T[r][c - j]

                    return sum
            
            if T[c][r] + T[c - 1][r] == T[c - 2][r]:
                cnt = 3
                i = -3
                while -1 < c + i and T[c + i][r] == T[c + i + 1][r] + T[c + i + 2][r]:
                    cnt += 1
                    i -= 1
                
                if is_part_of_fib(T[c][r]):
                    sum = 0
                    for j in range(cnt):
                        sum += T[c - j][r]

                    return sum
                    
T = [
    [1, 1, 8, 1, 1],
    [1, 1, 5, 1, 1],
    [1, 1, 3, 1, 1],
    [1, 3, 2, 3, 1],
    [1, 1, 3, 1, 1]
]

print(find_sum_of_fib(T))