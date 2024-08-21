# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która odpowiada na pytanie,
# czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie z nieparzystych cyfr.

def are_digits_odd(num):
    while num > 0:
        if num % 2 == 0:
            return False
        else:
            num //= 10

    return True

def zad2(T):
    n = len(T)

    for row in range(n):
        flag = False
        for column in range(n):
            if are_digits_odd(T[row][column]):
                flag = True
                break
        
        if not flag:
            return False
        
    return True

T = [[13, 4, 3, 3],
     [3, 3, 4, 5],
     [4, 2, 10, 8],
     [12,6, 9, 27]]

print(zad2(T))