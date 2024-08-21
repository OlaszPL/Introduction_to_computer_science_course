#Dane są ciągi: An+1 = √(An ∗ Bn) oraz Bn+1 = (An + Bn)/2.0.
# Ciągi te są zbieżne do wspólnej granicy nazywanej
#średnią arytmetyczno-geometryczną. Proszę napisać program wyznaczający średnią
#arytmetyczno-geometryczną dwóch liczb.

from math import sqrt

eps = 1E-10

def avg(a, b):
    while abs(a - b) > eps:
        print(a, b)
        a, b = sqrt(a * b), (a + b) / 2.0

    return a

if __name__ == '__main__':
    a, b = float(input()), float(input())
    print(avg(a, b))

