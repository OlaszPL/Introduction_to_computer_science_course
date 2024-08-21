#Proszę napisać program wypisujący podzielniki liczby

n = int(input())

i = 1

while i < n ** 0.5:
    if n % i == 0:
        print(i, n // i)
    i += 1
if n == i*i:
    print(i)