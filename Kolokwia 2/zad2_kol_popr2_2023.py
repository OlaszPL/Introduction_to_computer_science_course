# Aby otrzymać nagrodę trzeba przejść kolejno przez N komnat. W każdej komnacie znajduje się
# skrzynia (mogąca pomieścić maksymalnie 100 sztabek), w której umieszczono pewną liczbę sztabek
# złota. Będąc w danej komnacie możemy zabrać ze skrzyni pewną liczbę sztabek albo dołożyć do
# skrzyni wcześniej zebrane sztabki. Liczba sztabek przenoszona do następnej komnaty nie może
# przekraczać 6. Drzwi do kolejnej komnaty otwierają się wtedy, gdy liczba sztabek pozostawiona
# w skrzyni będzie liczbą pierwszą. Z ostatniej komnaty nie wolno wynieść żadnej sztabki. Proszę
# napisać funkcję, która zwraca informację, czy jest możliwe przejście przez komanty. Do funkcji
# należy przekazać tablicę zawierającą liczby sztabek w kolejnych komnatach. Na przykład:
# T = [10, 20, 30] −→ funkcja powinna zwrócić False
# T = [10, 20, 35] −→ funkcja powinna zwrócić True, w komnatach pozostanie [5, 23, 37]

# 1 skrzynia - max 100
# na raz można zabrać/ dołożyć
# można max przenosić 6
# drzwi otwieraja sie gdy liczba w skrzyni jest pierwsza
# po ostatniej komnacie nie można mieć ze sobą żadnych sztabek

from math import isqrt

def is_prime(a):
    if a <= 1:
        return False
    if a == 2 or a == 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False
    i = 5
    while i <= isqrt(a):
        if a % i == 0:
            return False
        i += 2
        if a % i == 0:
            return False
        i += 4

    return True

def roguelike(T):
    n = len(T)

    def rek(i = 0, backpack = 0):
        if i == n:
            return True

        elif i != n - 1:
        
            for j in range(0, 6 - backpack + 1):
                if T[i] - j >= 2:
                    if is_prime(T[i] - j):
                        if rek(i + 1, backpack + j):
                            return True
                        
            for k in range(0, backpack + 1):
                if T[i] + k <= 97:
                    if is_prime(T[i] + k):
                        if rek(i + 1, backpack - k):
                            return True

        elif is_prime(T[i] + backpack): # musimy wszystkie 
            return True
        
        return False

    return rek()

T = [10, 20, 35]
print(roguelike(T))