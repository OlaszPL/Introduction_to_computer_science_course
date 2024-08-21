#Proszę napisać program wyszukujący liczby doskonałe mniejsze od miliona.

n = 1
while n < 1000000:
    i = 1
    sum = 0
    while i < n ** 0.5:
        if n % i == 0:
            sum += i
            sum += n // i #Dla i=1 też odda n, więc suma będzie 2x większa
        i += 1
    if sum == 2*n:
        print(n)
    n += 1