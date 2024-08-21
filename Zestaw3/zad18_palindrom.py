# Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Proszę napisać funkcję, która zwraca długość najdłuższego
# spójnego podciągu będącego palindromem złożonym wyłącznie z liczb nieparzystych. Do funkcji należy przekazać tablicę,
# funkcja powinna zwrócić długość znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.

def is_odd(n):
    return n % 2 != 0

def palindrom(tab, tab_len, a, b):
    i = 0 # przeskok
    cnt = 0
    while a - i >= 0 and b + i < tab_len: # bo mozemy dojsc przeciez do poczatku tablicy, a prawy ostatni index jest mniejszy od dlugosci tablicy
        if tab[a - i] != tab[b + i]:
            return cnt
        if is_odd(tab[a - i]) and is_odd(tab[b + i]):
            cnt += 2 # bo jedna jest po prawej a druga po lewej
            i += 1
        else:
            return cnt
        
    return cnt

def zad18(tab):
    tab_len = len(tab)
    max_cnt = 0
    for i in range(1, tab_len - 1): #bo nie interesuje nas sytuacja gdzie nie ma już nic po lewej ani po prawej stronie tablicy
        if is_odd(tab[i]):
            if is_odd(tab[i + 1]) and tab[i] == tab[i + 1]: # parzysta liczba cyfr i 2 te same i rochodzimy sie na boki
                max_cnt = max(max_cnt, palindrom(tab, tab_len, i, i + 1))
            # nieparzysta liczba cyfr i jeden element w srodku
            max_cnt = max(max_cnt, palindrom(tab, tab_len, i - 1, i + 1) + 1) # +1 bo pominiemy ten srodkowy element

    return max_cnt


print(zad18([1, 3, 5, 7, 5, 3, 1,]))