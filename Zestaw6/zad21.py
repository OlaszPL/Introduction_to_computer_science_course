# Kolejne elementy listy o zwiększającej się wartości pola val nazywamy podlistą rosnącą.
# Proszę napisać funkcję, która usuwa z listy wejściowej najdłuższą podlistę rosnącą. Warunkiem usunięcia
# jest istnienie w liście dokładnie jednej najdłuższej podlisty rosnącej.

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


def zad21(a):
    p = Node(None, a)
    old_start = p
    flag = False
    total_cnt = 1
    total_first = p

    cnt = 1
    first = p # gdzie p.next dopiero zaczyna nasz podciag, a first jest pointerem tuż przed
    while p.next != None and p.next.next != None:
        if p.next.next.val > p.next.val:
            cnt += 1
        elif cnt != 1 and cnt == total_cnt:
            flag = False
            cnt = 1
            first = p
        elif cnt > total_cnt:
            total_cnt = cnt
            flag = True
            total_first = first
            cnt = 1
            first = p.next
        else:
            cnt = 1
            first = p
        p = p.next
    
    if cnt != 1 and cnt == total_cnt:
        flag = False
    elif cnt > total_cnt:
        total_cnt = cnt
        flag = True
        total_first = first

    if not flag:
        return old_start.next

    while total_first.next != None and total_cnt > 0:
        total_cnt -= 1
        total_first.next = total_first.next.next

    return old_start.next


t = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3]
p = list_to_linked_list(t)
print_list(p)

print_list(zad21(p))