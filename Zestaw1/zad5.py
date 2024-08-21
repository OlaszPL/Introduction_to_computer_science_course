#Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.

s = float(input())

a = 1 #bo trzeba od czegoś zacząć
r = 1 #różnica (później w wartości bezwzględnej bo obchodzi nas jakby delta z nich)
eps = 1E-10

while r > eps:
    b = (s / a + a) / 2.0
    r = abs(b - a) #różnica następnej i poprzedniej (gdy będzie znikoma to można przestać dalej liczyć)
    a = b

print(a)