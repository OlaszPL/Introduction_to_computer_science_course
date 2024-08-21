# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node
# ..def init(self,val):
# ....self.val = val
# ....self.next = None

# Zbiór mnogościowy liczb naturalnych reprezentowany jest przez listę o uporządkowanych rosnąco elementach. Proszę napisać funkcję iloczyn(z1,z2,z3),
# która przekształca 3 listy (zbiory) z1,z2,z3 w jedną listę (zbiór) zawierającą elementy będące częścią wspólna zbiorów z1,z2,z3. Funkcja powinna zwrócić
# wskazanie do listy wynikowej.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def list_to_linked_list(t):
    g = Node(None) # guardian
    for i in range(len(t) - 1, -1, -1):
        new_node = Node(t[i])
        new_node.next = g.next  # type: ignore
        g.next = new_node # type: ignore

    return g.next

def print_list(a):
    p = Node(None)
    p.next = a
    while p.next != None:
        print(str(p.next.val) + ' -> ', end = '')
        p = p.next
    print('END')


def iloczyn2(a1, a2):
    z1, z2 = Node(None), Node(None)
    z1.next, z2.next = a1, a2
    p = Node(None) # guardian
    start = p

    while z1.next != None and z2.next != None:
        if z1.next.val < z2.next.val:
            z1 = z1.next
        elif z1.next.val > z2.next.val:
            z2 = z2.next
        else:
            rem = z1.next # el do odpięcia z z1
            z1.next = z1.next.next # odpinamy rem z z1 i przechodzimy dalej
            rem.next = None # wywalamy wskaźnik, który odziedziczył
            p.next = rem
            p = p.next
            z2 = z2.next
    
    return start.next


def iloczyn(z1, z2, z3):
    return iloczyn2(iloczyn2(z1, z2), z3)

t1 = [1, 2, 3, 5, 10, 15, 45, 60, 78]
t2 = [0, 1, 3, 5, 10, 15, 60]
t3 = [5, 10, 15, 7, 8, 9]

print_list(iloczyn(list_to_linked_list(t1), list_to_linked_list(t2), list_to_linked_list(t3)))