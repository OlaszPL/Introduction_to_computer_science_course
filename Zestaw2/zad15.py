# Proszę napisać program znajdujący wszystkie liczby N-cyfrowe dla których suma N-tych
# potęg cyfr liczby jest równa tej liczbie, np. 153 = 1^3 + 5^3 + 3^3

from math import log10

def find_num(n):
    for num in range(10 ** (n - 1), 10 ** n):
        num_len = int(log10(num) + 1)
        sum = 0
        num_bak = num
        while num_bak > 0:
            sum += (num_bak % 10) ** num_len
            num_bak //= 10
        
        if sum == num:
            print(sum)
        
    return ''

print(find_num(int(input())))