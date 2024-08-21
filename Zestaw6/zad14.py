# Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o
# wartościach typu int, usuwającą wszystkie elementy, których wartość dzieli bez reszty wartość bezpośrednio
# następujących po nich elementów.

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

def strange_remove(a):
    p = Node(None, a)
    start = p
    while p.next != None and p.next.next != None:
        if p.next.next.val % p.next.val == 0:
            p.next = p.next.next
        else:
            p = p.next
    
    return start.next

t1 = [2, 3, 6, 7, 10, 5, 15, 20, 40]

print_list(strange_remove(list_to_linked_list(t1)))