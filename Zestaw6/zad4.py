# Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca kolejność jej elementów.

class Node:
    def __init__(self, value = None, next = None):
        self.val = value
        self.next = next

def print_list(a):
    p = Node(None, a)
    while p.next != None:
        print(str(p.next.val) + ' -> ', end = '')
        p = p.next
    print('END')


def list_to_linked_list(list):
    p = Node()
    for i in range(len(list) - 1, -1, -1):
        new_node = Node(list[i], p.next)
        p.next = new_node # przepchnie dalej w prawo

    return p.next


def reverse(p):
    prev = None
    cur = p

    while cur != None:
        next_node = cur.next
        cur.next = prev
        prev, cur = cur, next_node # przechodzimy dalej
    
    return prev


t = [1, 2, 3, 4, 5, 6, 7]

a = list_to_linked_list(t)

print_list(a)

a = reverse(a)

print_list(a)