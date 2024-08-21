# Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.

from math import log

def change_system(num, sys):
    new_num = None
    if sys == 10:
        print(num)

    if sys < 10 and sys >= 2:
        i = 1
        new_num = 0
        while num > 0:
            new_num += i * (num % sys)
            num //= sys
            i *= 10

        print(new_num)
    
    if sys > 10 and sys <= 16:
        new_num_len = int(log(num, sys) + 1)
        new_num = [0] * new_num_len
        k = 1
        tmp = 0
        val = ['A', 'B', 'C', 'D', 'E', 'F']
        while num > 0:
            tmp = num % sys
            if tmp > 9:
                i = tmp % 10
                new_num[-k] = val[i] # bo modulo działa od prawej i ta cyfra ma zostać po prawej
                k += 1
            else:
                new_num[-k] = tmp
                k += 1
            num //= sys

        for j in range(new_num_len): # w ten sposob ominalem stringa
            print(new_num[j], end='')

    return ''

print(change_system(int(input('Liczba: ')), int(input('System: '))))