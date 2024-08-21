# Proszę napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb
# NWD * NWW = a * b
# dla 3 tez powinno dzialac

def nwd2(a, b):
    while b != 0:
        a, b = b, a % b
    
    return a

def nww2(a, b):
    return (a * b) // nwd2(a, b)

def nww3(a, b, c):
    return nww2(nww2(a, b), c)

print(nww3(32, 1024, 76))