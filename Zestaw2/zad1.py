# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.
# 1 1 2 3 5 8 13 21

def part_of_fib(n):

    a, b = 1, 1

    while a <= n:
        a2, b2 = a, b
        while a2 <= n:
            if (a * a2) == n:
                return True
            else:
                a2, b2 = b2, a2 + b2
                
        a, b = b, a + b
    
    return False

print(part_of_fib(int(input())))