# Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
# liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów
# tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów
# znalezionego podzbioru.
# Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.
# 8 też jest poprawne, po prostu pojawia sie wczesniej niz 10 w rekurencji

def zad6(T):
    n = len(T)
    min_el_num = float('inf')
    res_sum = 0

    def rek(T, n, i = 0, el_num = 0, i_sum = 0, sum = 0):
        nonlocal min_el_num, res_sum

        if i_sum == sum and 0 < el_num < min_el_num:
            min_el_num = el_num
            res_sum = sum
            return True
        if i == n:
            return False
        
        return rek(T, n, i + 1, el_num + 1, i_sum + i, sum + T[i]) or rek(T, n, i + 1, el_num, i_sum, sum)
    
    rek(T, n)

    return res_sum

T = [1,7,3,5,11,2]

print(zad6(T))
