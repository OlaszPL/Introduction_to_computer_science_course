# Proszę napisać program, który oblicza pole ﬁgury pod wykresem funkcji y = 1/x w przedziale od 1 do k, metodą prostokątów

def area(k, base = 1e-3): # base to dlugosc jednej podstawy, jest doscy duzy bo program by sie wykonywal dlugo
    area = 0
    x = 1 # od 1
    while x <= k:
        area += base * 1/x
        x += base

    return area

print(area(99999))