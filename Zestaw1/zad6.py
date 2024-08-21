#Proszę napisać program rozwiązujący równanie x^x = 2020 metodą bisekcji
# trzeba założyć sobie coś: startujemy od 2 a kończymy na 10
# bo 2^2 = 4; 10^10=dużo

eps = 1e-10
min = 2
max = 10

while abs(max - min) > eps:
    x = (min + max) / 2  # środek
    if x ** x > 2020:
        max = x
    else:
        min = x

print(x)
