#stalinsort

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


def stalinsort(a):
    p = Node(None, a)
    start = p

    while p.next != None and p.next.next != None:
        if p.next.next.val < p.next.val:
            p.next.next = p.next.next.next
        else:
            p = p.next

    return start.next

t = [1, 2, 3, 4, 5, 1, 2, 3, 4, 11, 12, 13, 10, 15, 16, 1]

print_list(stalinsort(list_to_linked_list(t)))