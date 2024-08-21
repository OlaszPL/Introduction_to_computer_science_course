# Proszę napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb.

def nwd2(a, b):
    while b != 0:
        a, b = b, a % b
        
    return a

def nwd3(a, b, c):
    return nwd2(nwd2(a, b), c)

print(nwd3(32, 1024, 76))