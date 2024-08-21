# Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym iloczynie.

def zad11(T, k):
    n = len(T)
    cnt = 0

    def rek(T, n, k, i = 0, ratio = 1):
        nonlocal cnt
        if k == ratio:
            cnt += 1
            return
        if i == n:
            return
        
        rek(T, n, k, i + 1, ratio * T[i])
        rek(T, n, k, i + 1, ratio)

        return
    
    rek(T, n, k)

    return cnt

T = [1,2,4,8,9,10,13,3,24]
print(zad11(T, 24))