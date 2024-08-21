# Napisać program wypełniający N-elementową tablicę t liczbami pseudolosowymi z zakresu
# 1-1000 i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste.

from random import randint

def not_even(n):

    t = [randint(1, 1000) for _ in range(n)]
    print(t)

    for i in t:
        while i > 0:
            if (i % 10) % 2 == 0:
                break
            else:
                i //= 10

        if i == 0:
            return True
    
    return False

print(not_even(int(input())))