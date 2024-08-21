# ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
# waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
# naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory
# o równych wagach. Do funkcji należy przekazać wyłącznie tablicę,
# funkcja powinna zwrócić wartość typu Bool.

def waga(num):
    if num <= 1:
        return 0
    else:
        cnt = 0
        i = 2
        while num > 1:
            if num % i == 0:
                cnt += 1
                while num % i == 0:
                    num //= i
                
            i += 1
    
    return cnt

def zad2(T):
    n = len(T)
    
    def rek(i = 0, a = 0, b = 0, c = 0):
        if i == n:
            return a == b == c
        
        return rek(i + 1, a + waga(T[i]), b, c) or rek(i + 1, a, b + waga(T[i]), c) or rek(i + 1, a, b, c + waga(T[i]))
    
    return rek()

T = [2, 16, 32, 64, 128, 5, 25, 125, 512]

print(zad2(T))