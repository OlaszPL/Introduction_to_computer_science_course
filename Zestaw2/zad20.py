# Dwie liczby naturalne są różno-cyfrowe jeżeli nie posiadają żadnej wspólnej cyfry. Proszę napisać program,
# który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy systemu (w zakresie
# 2 − 16) w którym liczby są różno-cyfrowe. Program powinien wypisać znalezioną podstawę, jeżeli podstawa
# taka nie istnieje należy wypisać komunikat o jej braku. Na przykład: dla liczb 123 i 522 odpowiedzią jest
# podstawa 11 bo 123(10) = 102(11) i 522(10) = 435(11).

# nie trzeba zamieniac calych liczb tylko sprawdzic czy cyfry sie nie powtarzaja

# nie da sie bez tablic

def diff_digits(a, b, sys):
    t = [False for _ in range(sys)] # tablica tak jakby tego czy istnieje dana liczba z systemu czy nie
    while a > 0:
        t[a % sys] = True
        a //= sys
    
    while b > 0:
        if t[b % sys]:
            return False
        b //= sys
    
    return True

def zad20(a, b):
    for sys in range(2, 16 + 1):
        if diff_digits(a, b, sys):
            return sys
        

print(zad20(int(input()), int(input())))