#Dany jest ciąg określony wzorem: An+1 = (An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
#Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Proszę napisać program, który znajdzie
#wyraz początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków.

lim = 1

def steps_number(a):
    cnt = 0

    while a != lim:
        cnt += 1 #liczba kroków
        a = (a % 2) * (3 * a + 1) + (1 - a % 2) * a / 2
    return cnt

def start_value():

    max_steps = 0
    max_start = None

    for a in range(2, 10000 + 1):
        steps = steps_number(a)
        if steps > max_steps:
            max_steps = steps
            max_start = a

    print('Liczba kroków: ' + str(max_steps))
    print('Wyraz poczatkowy: ' + str(max_start))

start_value()