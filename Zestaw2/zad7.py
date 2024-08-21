# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie,
# czy liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = n ∗ n + n + 1
# n to N+

def zad7(num):
    a = 3
    n = 2
    while a <= num:
        if num % a == 0:
            print(a)
            return True
        else:
            a = n * n + n + 1
            n += 1
    
    return False

print(zad7(int(input())))