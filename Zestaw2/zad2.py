# Proszę napisać program wczytujący trzy liczby naturalne a, b, n i wypisujący rozwinięcie dziesiętne
# ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. (n jest rzędu 100)
# implementacja dzielenia pisemnego

def fraction(a, b, n = 100):

    print(a // b, end = ".")
    i = 1

    while i <= n:
        a %= b
        a *= 10
        print(a // b, end = "")
        i += 1

    return ""

print(fraction(int(input()), int(input())))