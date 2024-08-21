# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy dwukierunkowej,
# usuwa z niej wszystkie elementy, w których wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.

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


def to_remove(num):
    sum = 0
    while num > 0:
        sum += num % 2
        num //= 2
    
    return sum % 2 != 0

def zad17(a):
    p = Node(None, a)
    start = p

    while p.next != None:
        if to_remove(p.next.val):
            p.next = p.next.next
        else:
            p = p.next

    return start.next

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

p = list_to_linked_list(t)
print_list(p)
print_list(zad17(p))