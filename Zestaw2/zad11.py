# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie,
# czy jej cyfry stanowią ciąg rosnący.

from math import log10

def zad11(n):
    if n == 0 or int(log10(n) + 1 ) == 1:
        return False

    while n > 0:
        a = n % 10 # ta bardziej na prawo
        n //= 10
        b = n % 10
        if a < b:
            return False
    
    return True

print(zad11(int(input())))