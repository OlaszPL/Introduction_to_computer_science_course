# Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o wartościach typu int,
# usuwającą wszystkie elementy, których wartość jest mniejsza od wartości bezpośrednio poprzedzających je elementów.

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


def remove_all_direct_smaller(a):
    p = Node(None, a)
    start = p
    while p.next != None and p.next.next != None:
        if p.next.next.val < p.next.val:
            p.next.next = p.next.next.next # przepinamy
        else:
            p = p.next
    
    return start.next

t1 = [5, 3, 8, 2, 7, 14, 15, 30, 31, 29]
print_list(list_to_linked_list(t1))
print_list(remove_all_direct_smaller(list_to_linked_list(t1)))