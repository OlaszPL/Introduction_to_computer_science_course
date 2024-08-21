#  Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która w
# poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
# narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
# czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.

# bedzie nieparzysta jak potraktujemy punkt z tablicy jako srodek od ktorego startujemy

def zad9(T, k):
    n = len(T)

    for row in range(n - 1): # bo nie ma sensu sprawdzac punktow w krawedziach
        for column in range(n - 1):
            i = 1
            while -1 < row + i < n and -1 < row - i < n and -i < column + i < n and -i < column - i < n:
                if (T[row - i][column - i] * T[row + i][column + i] * T[row + i][column - i] * T[row - i][column + i]) == k:
                    return True, row, column
                else:
                    i += 1
        
    return False
    
T = [
[1,     2,  3,  4, 5, 6, 7 ],
[24, 25, 26, 27, 28, 29, 8 ],
[23, 40, 41, 42, 43, 30, 9 ],
[22, 39, 48, 49, 44, 31, 10],
[21, 38, 47, 46, 45, 32, 11],
[20, 37, 36, 35, 34, 33, 12],
[19, 18, 17, 16, 15, 14, 13]]

print(zad9(T, int(input('Podaj iloczyn k: '))))