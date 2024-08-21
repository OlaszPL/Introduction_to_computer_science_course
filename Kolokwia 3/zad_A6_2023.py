# Dana jest niepusta lista cykliczna, zbudowana z elementów zawierających pola val i next, której węzły
# przechowują liczby naturalne. Liczby przechowywane w liście spełniają warunek ”łączności”, tzn. dla każdego
# węzła ostatnia cyfra liczby jest identyczna z pierwszą cyfrą liczby z następnego węzła. Proszę napisać
# funkcję insert(p, n), która wstawia do listy wskazywanej przez wskaźnik p, liczbę n, metodą zastąpienia
# co najmniej dwóch elementów jednym zawierającym wstawioną liczbę. Po wstawieniu nowej liczby nadal
# zachowany powinien być warunek ”łączności”. Funkcja powinna zwrócić o ile skrócona została lista albo
# wartość 0 gdy elementu nie można wstawić do listy.
# Na przykład dla listy zawierającej elementy: 2023 31 17 703 37 707 72 29 902
# po wstawieniu liczby 303 lista może wyglądać następująco: 2023 303 37 707 72 29 902
# Funkcja powinna zwrócić wartość 2.

from math import log10

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def print_cycle(p):
    start = p
    while True:
        print(str(p.val) + ' -> ', end = '')
        p = p.next
        if p == start:
            print('poczatek cyklu')
            return
        

def count(p):
    cnt = 0
    start = p
    while True:
        cnt += 1
        p = p.next
        if p == start:
            return cnt
        
def first(num):
    return num // 10 ** int(log10(num))

def last(num):
    return num % 10

def insert(p, n):
    len = count(p)

    if len < 2:
        return 0, p
    elif len == 2:
        p = Node(n, p)
        return 2, p

    while True:
        start_p = p
        if last(p.val) == first(n):
            cnt = 0
            q = p.next
            while True:
                if cnt >= 2 and last(n) == first(q.val):
                    new_node = Node(n, q)
                    p.next = new_node
                    return len - count(p), p
                else:
                    q = q.next
                    cnt += 1
                if q == p.next:
                    break
                
        p = p.next
        if p == start_p:
            return 0, p
            

a = Node(2023)
b = Node(31)
c = Node(17)
d = Node(703)
e = Node(37)
f = Node(707)
g = Node(72)
h = Node(29)
i = Node(902)

a.next, b.next, c.next, d.next, e.next, f.next, g.next, h.next, i.next = b, c, d, e, f, g, h, i, a
print_cycle(a)

res = insert(a, 303)

print(res[0])
print_cycle(res[1])