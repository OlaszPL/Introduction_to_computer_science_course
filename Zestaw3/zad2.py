# Napisać funkcje sprawdzającą czy dwie liczby naturalne są one zbudowane z takich samych
# cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.
# ilosc ma znaczenie

def same_digits(a, b):
    t  = [0] * 10

    while a > 0:
        t[a % 10] += 1
        a //= 10

    while b > 0:
        t[b % 10] -= 1
        b //= 10

    for i in range(10):
        if t[i] != 0:
            return False
    
    return True


print(same_digits(int(input()),int(input())))