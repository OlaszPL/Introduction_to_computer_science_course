# Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów
# jest równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna
# zwrócić długość znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.

def zad19(t):
    t_len = len(t)
    max_len = 0

    for i in range(t_len - 1): # bo podciag 1 elementowy nie jest rosnacy
        sum = t[i]
        cnt = 1
        sum_i = i

        if t[i] < t[i + 1]: # kiedy jest rosnacy
            for j in range(i + 1, t_len):
                if t[j - 1] > t[j]: #wtedy wskoczy kolejne i bo nie jest rosnacy, a tak bo nie wyskoczymy poza index tablicy
                    break
                else:
                    sum += t[j]
                    cnt += 1
                    sum_i += j
                if sum == sum_i: # to tutaj w tym momencie jest wazne
                    max_len = max(max_len, cnt)

    return max_len

t = [1, 2, 1, 3, 5, 6, 7, 7, 8, 9, 13, 4]
print(zad19(t))