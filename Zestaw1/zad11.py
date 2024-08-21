#Proszę napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.
#Suma dzielników num1 ma być równa num2

from math import sqrt

num1 = 1

while num1 < 1000000:
    i = 1
    sum1 = 0
    while i <= sqrt(num1):
        if num1 % i == 0:
            sum1 += i
            sum1 += num1 // i

        i += 1

    sum1 -= num1
    i2 = 1
    sum2 = 0

    while i2 <= sqrt(sum1):
        if sum1 % i2 == 0:
            sum2 += i2
            sum2 += sum1 // i2
        
        i2 += 1
    
    sum2 -= sum1
    
    if sum2 == num1 and num1 > sum1: # by nie definiować sum1 jeszcze przed pierwszym while
        print(sum1, num1)
    
    num1 += 1