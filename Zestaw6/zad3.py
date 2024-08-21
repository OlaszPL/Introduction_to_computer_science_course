# Proszę napisać funkcję scalającą dwie posortowane listy w jedną posortowaną listę.
# Do funkcji należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna, - funkcja rekurencyjna.


class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def print_list(a):
    p = Node(None, a)
    while p.next != None:
        print(str(p.next.val) + ' -> ', end = '')
        p = p.next
    print('END')

def list_to_linked_list(t):
    p = Node()
    for i in range(len(t) - 1, -1, -1):
        new_node = Node(t[i], p.next)
        p.next = new_node

    return p.next


def combine_iter(a1, a2):
    p1 = Node(None, a1)
    p2 = Node(None, a2)
    c = Node() # guardian # combined list
    start = c

    if p1.next == None:
        return p2.next
    if p2.next == None:
        return p1.next

    while p1.next != None and p2.next != None:
        if p1.next.val <= p2.next.val: # słaba nierówność bo jak równe to i tak to kiedyś przepnie w dobre miesjce
            rem = p1.next # do usunięcia z p1
            p1.next = p1.next.next # przepinamy dalej
            rem.next = None # wywalamy wskaźnik odziedziczony
            c.next = rem
            c = c.next
        elif p1.next.val > p2.next.val:
            rem = p2.next
            p2.next = p2.next.next
            rem.next = None
            c.next = rem
            c = c.next

    if p1.next != None: # jakby się okazało, że któraś z list się skończyła a druga nie
        c.next = p1.next
    elif p2.next != None:
        c.next = p2.next

    return start.next


def combine_rek(p1, p2):

    if p1 == None:
        return p2
    if p2 == None:
        return p1
    
    if p1.val <= p2.val:
        p1.next = combine_rek(p1.next, p2)
        return p1
    elif p1.val > p2.val:
        p2.next = combine_rek(p1, p2.next)
        return p2



t1 = [1, 2, 3, 3, 5, 10, 15, 23, 24, 56]
t2 = [0, 2, 7, 9, 16]

combined = combine_rek(list_to_linked_list(t1), list_to_linked_list(t2))
print_list(combined)
