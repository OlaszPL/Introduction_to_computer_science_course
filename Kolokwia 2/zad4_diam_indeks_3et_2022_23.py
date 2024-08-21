# Dany jest zestaw N rur o długościach wyrażonych całkowitą liczbą metrów L1 , L2, ...Ln. Spośród tego zesta-
# wu chcemy zbudować rurociąg, którego długość wyniesie S metrów. Proszę napisać program, który wyznacza
# minimalna liczbę rur niezbędną do zbudowania rurociągu.

# Dla:
# T = [2, 7, 4, 3, 11]
# S = 16
# Poprawną odpowiedzią jest
# 3
# Są to rury o długościach: 2, 3, 11

def ruraciag(T, S):
    n = len(T)
    min_cnt = float('inf')

    def rek(S, i = 0, cnt = 0):
        nonlocal min_cnt
        if S < 0:
            return
        if S == 0:
            min_cnt = min(min_cnt, cnt)
            return
        if i == n:
            return
        
        rek(S - T[i], i + 1, cnt + 1)
        rek(S, i + 1, cnt)

        return
    
    rek(S)

    return min_cnt if min_cnt < float('inf') else "BRAK"

T = [2, 7, 4, 3, 11]
print(ruraciag(T, 16))