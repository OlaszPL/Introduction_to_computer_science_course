# Dana jest tablica T zawierająca liczby naturalne. W tablicy na kolejnych pozycjach ukryto
# pewien ciąg liczb o długości co najmniej 3 elementów. Aby ułatwić odnalezienie tego ciągu,
# zaraz za nim umieszczono ten sam ciąg ale każdy z jego elementów pomnożono przez pewną liczbę.
# Proszę napisać funkcję sequence(T) która odnajdzie ukryty ciąg.
# Funkcja powinna zwrócić indeksy pierwszego i ostatniego elementu ukrytego ciągu.

def sequence(T):
    n = len(T)
    start_inx, end_inx = 0, 0

    for i in range(n-2):
        q = T[i + 1] / T[i]
        for j in range(i + 2, n - 1):
            if T[j + 1] / T[j] == q:
                cnt = 2
                while i + 1 + cnt < n and j + 1 + cnt < n and \
                      T[i + 1 + cnt] / T[i + cnt] == T[j + 1 + cnt] / T[j + cnt]:
                    cnt += 2
                
                if j - cnt == i and cnt >=3:
                    start_inx = i
                    end_inx = j - 1
    
    return start_inx, end_inx

T =  [2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2]

print(sequence(T))