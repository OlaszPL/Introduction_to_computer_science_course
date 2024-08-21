# Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy.
# Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach.
# Poprzednie zadanie. Program powinien wypisywać wybrane odważniki.

def is_possible_to_weigh(T, weight):
    n = len(T)
    
    def rek(T, n, weight, weight2 = 0, i = 0):

        if weight == weight2:
            return True
        if i == n:
            return False
        
        if rek(T, n, weight, weight2, i + 1):
            return True
        elif rek(T, n, weight + T[i], weight2, i + 1):
            print(-T[i], end =' ')
            return True
        elif rek(T, n, weight, weight2 + T[i], i + 1):
            print(T[i], end =' ')
            return True
        else:
            return False
    
    return rek(T, n, weight)


T = [10, 1, 1, 2, 3]
weight = 13

print(is_possible_to_weigh(T, weight))