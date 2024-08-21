# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
# def __init__(self):
# self.val = None
# self.next = None
# Zbiór mnogościowy liczb naturalnych reprezentowanych jest przez listę o uporządkowanych rosnąco
# elementach. Proszę napisać funkcję iloczyn(z1, z2, z3), która przekształca 3 listy (zbiory) z1, z2,
# z3 w jedną listę (zbiór) zawierającą elementy będące częścią wspólną zbiorów z1, z2, z3. Funkcja
# powinna zwrócić wskazanie do listy wynikowej.

class Node:
    def __init__(self):
        self.val = None
        self.next = None

def list_to_linked_list(t):
    g = Node() # guardian
    for i in range(len(t) - 1, -1, -1):
        new_node = Node()
        new_node.val = t[i]
        new_node.next = g.next  # type: ignore
        g.next = new_node # type: ignore

    return g.next

def print_list(a):
    p = Node()
    p.next = a
    while p.next != None:
        print(str(p.next.val) + ' -> ', end = '')
        p = p.next
    print('END')

def iloczyn2(z1, z2):
    p = Node()
    p.next = z1
    q = Node()
    q.next = z2
    res = Node()
    start = res

    while p.next != None and q.next != None:
        if p.next.val == q.next.val:
            rem = p.next
            p.next = p.next.next
            q.next = q.next.next
            rem.next = None
            res.next = rem
            res = res.next 
        elif p.next.val < q.next.val:
            p = p.next
        else:
            q = q.next
    
    return start.next

def iloczyn(z1, z2, z3):
    return iloczyn2(iloczyn2(z1, z2), z3)

t1 = [1, 2, 3, 4, 5, 6, 7, 10, 11, 13, 15, 20]
t2 = [2, 4, 6, 7, 13, 30, 40]
t3 = [2, 6, 13, 14, 20]

a, b, c = list_to_linked_list(t1), list_to_linked_list(t2), list_to_linked_list(t3)
print_list(a)
print_list(b)
print_list(c)
print()
print_list(iloczyn(a, b, c))