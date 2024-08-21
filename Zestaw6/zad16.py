# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jednokierunkowej, przenosi na początek listy te z nich,
# które mają parzystą ilość piątek w zapisie ósemkowym.

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


def to_move(num):
    cnt = 0
    while num > 0:
        if num % 8 == 5:
            cnt += 1
        num //= 8
    
    return cnt != 0 and cnt % 2 == 0

def zad16(a):
    p = Node(None, a)
    start = p

    while p.next != None:
        if to_move(p.next.val):
            rem = p.next
            p.next = p.next.next
            rem.next = start.next
            start.next = rem
        else:
            p = p.next
    
    return start.next

t = [1, 2, 4, 5, 325, 20, 20845]

p = list_to_linked_list(t)
print_list(p)
print_list(zad16(p))
