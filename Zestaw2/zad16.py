# Liczba Smitha to taka, której suma cyfr jest równa sumie cyfr wszystkich liczb występujących w jej rozkładzie na czynniki pierwsze.
# Na przykład: 85 = 5 ∗ 17, 8 + 5 = 5 + 1 + 7. Proszę napisać program wypisujący liczby Smitha mniejsze od 1000000
# rozklad na czynniki pierwsze
# liczba smitha to liczba zlozona - wystarczy napisac is prime

from math import isqrt

def is_prime(n):
    if n == 1 or n == 0:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5

    while i <= isqrt(n):
        if n % i == 0:
            return False
        
        i += 2

        if n % i == 0:
            return False
        
        i += 4

    return True

def smiths_numbers(n = 1000000):
    # bo 1,2,3 nia nie jest
    num = 4
    # count = 0

    while num <= n:
        if not is_prime(num):
            sum_digits = 0
            sum_factors = 0
            num_bak1 = num_bak2 = num
            while num_bak1 > 0:
                sum_digits += num_bak1 % 10
                num_bak1 //= 10

            while num_bak2 % 2 == 0:
                sum_factors += 2
                num_bak2 //= 2

            while num_bak2 % 3 == 0:
                sum_factors += 3
                num_bak2 //= 3

            i = 5

            while num_bak2 > 1 and i <= isqrt(num): # trzeba uwzglednic, ze czynnik moze byc liczba wiecej niz 1 cyfrowa
                while num_bak2 % i == 0:
                    i_bak = i
                    while i_bak > 0:
                        sum_factors += i_bak % 10
                        i_bak //= 10
                    num_bak2 //= i
                
                i += 2

                while num_bak2 % i == 0:
                    i_bak = i
                    while i_bak > 0:
                        sum_factors += i_bak % 10
                        i_bak //= 10
                    num_bak2 //= i

                i += 4
            
            if num_bak2 > i: # czyli kiedy dany czynnik nie zostal sprawdzony powyzej przez co caly zostal do dodania
                while num_bak2 >= 1:
                    sum_factors += num_bak2 % 10
                    num_bak2 //= 10

            if sum_digits == sum_factors:
                print(num)
                # count += 1

        num += 1

    return ''
    # return count
    
print(smiths_numbers())