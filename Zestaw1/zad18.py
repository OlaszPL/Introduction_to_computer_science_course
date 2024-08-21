# Proszę zmodyﬁkować wzór Newtona aby program z zadania 5 obliczał pierwiastek stopnia 3.

s = float(input())

a = 1 #bo trzeba od czegoś zacząć
r = 1 #różnica (później w wartości bezwzględnej bo obchodzi nas jakby delta z nich)
eps = 1E-10

while r > eps:
    b = (2 * a + (s / (a * a))) / 3.0
    r = abs(b - a) #różnica następnej i poprzedniej (gdy będzie znikoma to można przestać dalej liczyć)
    a = b

print(a)