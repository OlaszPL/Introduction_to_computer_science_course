# Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać funkcję dodającą dwie takie liczby.
# W wyniku dodawania dwóch liczb powinna powstać nowa lista.


class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def list_to_linked_list(t):
    p = Node()
    for i in range(len(t) - 1, -1, -1):
        new_node = Node(t[i], p.next)
        p.next = new_node
    
    return p.next

def print_list(a):
    p = Node(None, a)
    while p.next != None:
        print(str(p.next.val) + ' -> ', end = '')
        p = p.next
    print('END')


def reverse(p):
    prev = None
    cur = p

    while cur != None:
        next_node = cur.next
        cur.next = prev
        prev, cur = cur, next_node

    return prev

def add_two_numbers(a1, a2):
    a1 = reverse(a1)
    a2 = reverse(a2)

    p1, p2 = Node(None, a1), Node(None, a2)

    res = Node()
    res_start = res
    rest = 0

    while p1.next != None and p2.next != None:
        tmp_sum = p1.next.val + p2.next.val + rest
        rest = 0
        if tmp_sum <= 9:
            new_node = Node(tmp_sum, res.next)
        else:
            rest = tmp_sum // 10
            new_node = Node(tmp_sum % 10, res.next)
        res.next = new_node
        p1 = p1.next
        p2 = p2.next

    while p1.next != None:
        tmp_sum = p1.next.val + rest
        rest = 0
        if tmp_sum <= 9:
            new_node = Node(tmp_sum, res.next)
        else:
            rest = tmp_sum // 10
            new_node = Node(tmp_sum % 10, res.next)
        res.next = new_node
        p1 = p1.next

    while p2.next != None:
        tmp_sum = p2.next.val + rest
        rest = 0
        if tmp_sum <= 9:
            new_node = Node(tmp_sum, res.next)
        else:
            rest = tmp_sum // 10
            new_node = Node(tmp_sum % 10, res.next)
        res.next = new_node
        p2 = p2.next
    
    if rest != 0:
        new_node = Node(rest, res.next)
        res.next = new_node

    return res_start.next


t1 = [1, 2, 3, 4, 5, 6]
t2 = [9, 9, 9, 9, 9, 9]

print_list(add_two_numbers(list_to_linked_list(t1), list_to_linked_list(t2)))