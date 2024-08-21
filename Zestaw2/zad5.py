# Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera.
# Ile różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie. Np. dla 2315 będą to 21, 35, 231, 315.
# kolejnosc cyfr zachowana

from math import log10

def apply_mask(num, mask): # dostaje juz gotowa maske i generuje na podstawie niej liczbe, maske traktujemy binarnie pomimo tego, ze to liczba dziesietna
    new_num = 0
    i = 0
    while mask > 0: 
        if mask % 2 == 1:  # spr ostatnia cyfre maski potraktowanej binarnie, jak 1 to przepisuje, jak 0 to nie
            new_num += (10 ** i) * (num % 10)
            i += 1
        num //= 10
        mask //= 2 # bo traktujemy ja binarnie

    return new_num
    
def zad5(num):
    num_len = int(log10(num) + 1)
    count = 0
    # generujemy maski i wykonujemy apply_mask
    # range od 1 bo 0 chyba nas nie interesuje z przykladu w tresci
    for mask in range(1, 2 ** num_len): # 2^num_len - 1 to jest wartosc maksymalnej maski bitowej (1111....111) w postaci dziesietnej
        tmp = apply_mask(num, mask)
        if tmp % 7 == 0:
            count += 1
            print(tmp)

    return count

print('Liczba: ' + str(zad5(int(input()))))