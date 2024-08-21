# Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi element listy. Do funkcji należy przekazać wskazanie na pierwszy element listy.

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


# def usun_co_druga(p):
#     start = p
#     cnt = 0
#     while p.next != None:
#         if cnt == 1:
#             p.next = p.next.next
#             cnt = 0
#         else:
#             cnt += 1
#             p = p.next

#     return start

def usun_co_druga(a):
    p = Node(None, a)
    start = p
    while p.next != None and p.next.next != None:
        p.next.next = p.next.next.next
        p = p.next
        
    return start.next


t = [1, 2, 3, 4, 5, 6, 7, 8, 9]

g = list_to_linked_list(t)

g = usun_co_druga(g)

print_list(g)