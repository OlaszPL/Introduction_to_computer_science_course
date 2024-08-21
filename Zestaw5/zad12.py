# Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym iloczynie.

# Proszę zmodyfikować poprzedni program aby wypisywał znalezione n-ki.

def gen_res_enki(T, n):
    res = [0] * n

    for j in range(n):
        res[j] = T[j]

    return res

def zad11(T, k):
    n = len(T)
    cnt = 0
    enki = [0] * n

    def rek(T, n, k, enki, i = 0, j = 0, ratio = 1):
        nonlocal cnt
        if k == ratio:
            cnt += 1
            print(gen_res_enki(enki, j))
            return
        if i == n:
            return
        
        enki[j] = T[i]
        rek(T, n, k, enki, i + 1, j + 1, ratio * T[i])
        enki[j] = 0 # backtracking
        rek(T, n, k, enki, i + 1, j, ratio)

        return
    
    rek(T, n, k, enki)

    return cnt

T = [1,2,4,8,9,10,13,3,24]
print(zad11(T, 24))