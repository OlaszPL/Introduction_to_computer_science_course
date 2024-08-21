# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która odpowiada na pytanie,
# czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę parzystą.

def any_digit_even(num):
    while num > 0:
        if num % 2 == 0:
            return True
        else:
            num //= 10

    return False

def zad3(T):
    n = len(T)

    for row in range(n):
        flag = True
        for column in range(n):
            if not any_digit_even(T[row][column]):
                flag = False
                break

        if flag:
            return True
        
    return False

T = [[13, 4, 3, 3],
     [3, 3, 4, 5],
     [4, 2, 32, 2],
     [12,6, 9, 27]]

print(zad3(T))