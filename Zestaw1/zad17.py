# Proszę napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych wyrazów ciągu Fibonacciego.
# Wyznaczyć ten iloraz dla różnych wartości początkowych wyrazów ciągu.

def fib_ratio(a, b, eps = 1e-10):

    fib_prev = b / a
    a, b = b, a + b
    fib_curr = b / a
    
    while abs(fib_prev - fib_curr) > eps:
        fib_prev = fib_curr
        a, b = b, a + b
        fib_curr = b / a

    return fib_curr

print(fib_ratio(1, 1))