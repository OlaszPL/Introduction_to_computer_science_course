# Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w drugiej. Do funkcji należy
# przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wartość logiczną.

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next


def is_one_in_another(a, b):
    p, q = Node(None, a), Node(None, b)
    start_p, start_q = p, q

    while p.next != None:
        if p.next == start_q.next:
            return True
        p = p.next
    
    while q.next != None:
        if q.next == start_p.next:
            return True
        q = q.next
    
    return False

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

e = Node(1)
f = Node(2)
g = a
h = Node(3)

e.next = f
f.next = g
g.next = h

print(is_one_in_another(a, e))