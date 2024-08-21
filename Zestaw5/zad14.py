# Problem wież w Hanoi (treść oczywista)

def hanoi(n, a, b, c): # a - z ktorego, b - pomocnicza, c - na ktora
    if n > 0:
        hanoi(n - 1, a, c, b)
        print(a, '->', c)
        hanoi(n - 1, b, a, c)

hanoi(3, 'A', 'B', 'C')