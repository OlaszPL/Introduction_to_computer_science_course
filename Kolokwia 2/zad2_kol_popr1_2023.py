# Odcinek leżący na osi liczbowej jest opisywany parą liczb całkowitych (a, b). Dana jest tablica
# opisująca zbiór takich odcinków. Proszę napisać funkcję zwracającą wartość True, jeżeli z tablicy
# można wybrać zbiór odcinków, z których dwa nie zachodzą na siebie, a łączna ich długość wynosi
# 2022 lub False w przeciwnym wypadku.

def size(odc):
    return abs(odc[0] - odc[1])

def infer_with_rest(odc, used, n, T):
    for i in range(n):
        if used[i] and infer(odc, T[i]):
            return True
    
    return False

def infer(odc1, odc2):
    return odc1[0] <= odc2[0] <= odc1[1] or odc1[0] <= odc2[1] <= odc1[1] or odc2[0] <= odc1[0] <= odc2[1] or odc2[0] <= odc1[1] <= odc2[1]

def zad(T, k): # k  - łączna długość
    n = len(T)
    used = [False for _ in range(n)] # które odcinki były użyte

    def rek(T, n, k, used, i = 0):
        if k < 0:
            return False
        if k == 0:
            return True
        if i == n:
            return False
        
        if not infer_with_rest(T[i], used, n, T):
            used[i] = True
            if rek(T, n, k - size(T[i]), used, i + 1):
                return True
            used[i] = False

        return rek(T, n, k, used, i + 1)
        
    return rek(T, n, k, used)

T = [(0, 100), (250, 1000), (2000, 3172)]


print(zad(T, 2022))