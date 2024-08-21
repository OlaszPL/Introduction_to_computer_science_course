# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.
    
def palindrom(n, sys = 10):
    if n == 0 or n == 1:
        return True
    else:
        num = n
        rev = 0

        while num > 0:
            rev *= sys # patrz nizej, poprzednia razy 10
            rev += num % sys # musialem rozdzielic te 2 bo cos sie psulo
            num //= sys

        return rev == n
    
n = int(input())

print(palindrom(n))
print(palindrom(n, 2))