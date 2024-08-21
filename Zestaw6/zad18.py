# Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.

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

def uniq(a):
    p = Node(None, a)
    start = p

    while p.next != None:
        p2 = p.next
        flag = False
        while p2.next != None:
            if p.next.val == p2.next.val:
                flag = True
                p2.next = p2.next.next
            else:
                p2 = p2.next
        
        if flag:
            p.next = p.next.next
        else:
            p = p.next

    return start.next

t = [1, 2, 2, 2, 3, 4, 1, 2, 3, 5, 11, 2, 2, 2]
p = list_to_linked_list(t)
print_list(p)
print_list(uniq(p))