# Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji należy przekazać wskazanie na pierwszy element listy.

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


def append(a, el):
    p = Node(None, a)
    start = p

    while p.next != None:
        p = p.next
    
    p.next = Node(el)

    return start.next


def remove_last_el(a):
    p = Node(None, a)
    start = p

    if p.next == None:
        return start

    while p.next != None and p.next.next != None:
        p = p.next

    p.next = p.next.next # type: ignore

    return start.next
    

g = Node(0)

g = append(g, 1)
g = append(g, 2)
g = append(g, 5)
g = append(g, 10)

print_list(g)

g = remove_last_el(g)

print_list(g)