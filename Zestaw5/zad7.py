# Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy.
# Odważniki można umieszczać tylko na jednej szalce. Zał (odczywiste): odważników można użyć raz.

def is_possible_to_weigh(T, weight):
    n = len(T)

    def rek(T, n, weight, i = 0):
        if weight < 0:
            return False
        if weight == 0:
            return True
        if i == n:
            return False
        
        return rek(T, n, weight, i + 1) or rek(T, n, weight - T[i], i + 1)

    return rek(T, n, weight)

T = [2, 3, 5, 8, 13]
weight = 31

print(is_possible_to_weigh(T, weight))