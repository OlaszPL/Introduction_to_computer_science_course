# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta zawiera cyfrę równą liczbie swoich cyfr

from math import log10

def zad12(n):
    if n == 0:
        return False
    num_len = int(log10(n) + 1)
    while n > 0:
        if n % 10 == num_len:
            return True
        else:
            n //= 10
    
    return False


print(zad12(int(input())))