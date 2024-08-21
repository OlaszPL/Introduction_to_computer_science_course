# Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
# na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory o
# jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
# wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.

def zad32(T, k):
    n = len(T)

    def rek(T, k, n, cnt = 0, sum1 = 0, sum2 = 0, i = 0):
    
        if cnt == k and sum1 == sum2:
            return True
        if i == n:
            return False
        
        return rek(T, k, n, cnt, sum1, sum2, i + 1) or rek(T, k, n, cnt + 1, sum1 + T[i], sum2, i + 1) or rek(T, k, n, cnt + 1, sum1, sum2 + T[i], i + 1)

    return rek(T, k, n)

T = [2,1,3,7,0]
k = 3

print(zad32(T, k))