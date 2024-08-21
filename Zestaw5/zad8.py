# Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy.
# Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach.

def is_possible_to_weigh(T, weight):
    n = len(T)

    def rek(T, n, weight, weight2 = 0, i = 0):
        
        if weight == weight2:
            return True
        if i == n:
            return False
        
        return rek(T, n, weight, weight2, i + 1) or rek(T, n, weight + T[i], weight2, i + 1) or rek(T, n, weight, weight2 + T[i], i + 1)

    return rek(T, n, weight)

T = [2, 3, 5, 8, 13]
weight = 17

print(is_possible_to_weigh(T, weight))