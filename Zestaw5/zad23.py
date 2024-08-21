# Dana jest tablica T[N] zawierająca oporności N rezystorów wyrażonych całkowitą liczbą
# kΩ. Proszę napisać funkcję, która sprawdza czy jest możliwe uzyskanie wypadkowej rezystancji R (równej
# całkowitej liczbie kΩ) łącząc dowolnie 3 wybrane rezystory.

def zad23(T, k, num_of_resistors):
    n = len(T)

    def rek(T, n, k, num_of_resistors, i = 0, resist = 0):
        if num_of_resistors == 0:
            return resist == k
        if i == n:
            return False
        
        if resist != 0 and rek(T, n, k, num_of_resistors - 1, i + 1, 1 / ((1 / resist) + (1 / T[i]))) or rek(T, n, k, num_of_resistors, i + 1, resist):
            return True
        if rek(T, n, k, num_of_resistors - 1, i + 1, resist + T[i]) or rek(T, n, k, num_of_resistors, i + 1, resist):
            return True
        
        return False
    
    return rek(T, n, k, num_of_resistors)

T = [1, 2, 5, 8, 3, 0.5, 4]
print(zad23(T, 8/19, 3))