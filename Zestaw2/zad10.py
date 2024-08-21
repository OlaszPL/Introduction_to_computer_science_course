# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie,
# czy liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = 3 ∗ An−1 + 1, a pierwszy wyraz jest równy 2.

def zad10(n):
    a = 2
    if n < a:
        return False
    
    while a <= n:
        if n % a == 0:
            return True
        else:
            a = 3 * a + 1
    
    return False

print(zad10(int(input())))