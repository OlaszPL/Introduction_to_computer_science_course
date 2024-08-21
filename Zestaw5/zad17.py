# Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić
# wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
# wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
# 75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
# zadanych liczb.

# Zał: cyfry się nie powtarzają

from math import isqrt, log10

def is_prime(a):
    if a <= 1:
        return False
    if a == 2 or a == 3:
        return True
    if a % 2 == 0  or a % 3 == 0:
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

def zad17(num1, num2):
    cnt = 0

    def rek(num1, num2, new_num = 0):
        nonlocal cnt
        if num1 == 0 and num2 == 0:
            if is_prime(new_num):
                cnt += 1
            return
        if num1 != 0:
            rek(num1 % (10 ** int(log10(num1))), num2, (new_num * 10) + num1 // 10 ** int(log10(num1)))
        if num2 != 0:
            rek(num1, num2 % (10 ** int(log10(num2))), (new_num * 10) + num2 // 10 ** int(log10(num2)))
        
        return
    
    rek(num1, num2)

    return cnt

print(zad17(123, 75))