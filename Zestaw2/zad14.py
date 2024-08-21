# Dane są dwie liczby naturalne z których budujemy trzecią liczbę.
# W budowanej liczbie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych.
# Wzajemna kolejność cyfr każdej z liczb wejścio-wych musi być zachowana.
# Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523, 75123, 17253, itd.
# Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch zadanych liczb.
# maska bitowa
# zalozmy, ze liczby sa roznocyfowe, bo nie idzie sprawdzic bez tablic

from math import isqrt, log10

def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5

    while i <= isqrt(n):
        if n % i == 0:
            return False
        else:
            i += 2
            if n % i == 0:
                return False
            else:
                i += 4

    return True

def check_mask(mask, num1_len): # sprawdzamy czy ilosc 1 nie przekracza num1_len
    sum = 0
    while mask > 0:
        sum += mask % 2
        mask //= 2
    
    return sum == num1_len

def apply_mask(num1, num2, whole_num_len, mask):
    new_num = 0
    i = 0
    while i < whole_num_len:
        if mask % 2 == 1:
            new_num += (10 ** i) *  (num1 % 10)
            num1 //= 10
        else:
            new_num += (10 ** i) * (num2 % 10)
            num2 //= 10
        mask //= 2
        i += 1
    
    return new_num

def zad14(n1, n2): # zalozenie num1_len > num2_len  ==> num1 > num2
    print('---')
    num1 = max(n1, n2)
    num2 = min(n1, n2)
    num1_len = int(log10(num1) + 1)
    num2_len = int(log10(num2) + 1)
    whole_num_len = num1_len + num2_len
    count = 0

    for mask in range((2 ** num1_len) - 1, (2 ** whole_num_len) - (2 ** num2_len) + 1): # trzba jeszcze sprawdzic maske bo moze wywalic za duza liczbe 1 lub 0
        if check_mask(mask, num1_len):
            tmp = apply_mask(num1, num2, whole_num_len, mask)
            if is_prime(tmp):
                print(tmp)
                count += 1

    return count


print('Liczba: ' + str(zad14(int(input()), int(input()))))