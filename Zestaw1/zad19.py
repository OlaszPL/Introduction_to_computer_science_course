#Proszę napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! +
# 1/1! + 1/2! + 1/3! + ...

eps = 1e-12
def wyznacz_e():

    e = 2  # bo pierwsze 2 wyrazy to 1+1=2
    fact = 1
    i = 2

    while True:
        fact *= i
        i += 1

        next_elem = 1 / fact
        e += next_elem

        if next_elem < eps:
            break

    return(e)

print(wyznacz_e())