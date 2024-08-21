# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# zakończona jest unikalną cyfrą.

def is_unique(n):
    last_num = n % 10
    n //= 10
    while n > 0:
        if n % 10 == last_num:
            return False
        else:
            n //= 10
    
    return True

print(is_unique(int(input())))