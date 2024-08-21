# Kolejne (co najmniej dwa) elementy listy o identycznej wartości pola val nazywamy podlistą stałą.
# Proszę napisać  funkcję, która usuwa z listy wejściowej najdłuższą podlistę stałą. Warunkiem jej
# usunięcia jest istnienie w liście  dokładnie jednej najdłuższej podlisty stałej. Do funkcji należy
# przekazać wskaźnik na pierwszy element listy. Funkcja powinna zwrócić liczbę usuniętych elementów. 
# Na przykład z listy [ 1 3 3 3 5 7 11 13 13 1 2 2 2 2 3 ] należy usunąć podlistę [ 2 2 2 2 ], 
# a z listy [ 1 3 3 3 3 5 7 11 13 13 1 2 2 2 2 3 ] nie należy nic usuwać.

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


def remove(a):
    p = Node(None, a)
    start = p
    cnt = 1
    tmp_cnt = 1
    to_rem_start = p.next
    flag = False
    prev_val = None

    while p.next != None:
        q = p.next
        while q.next != None and q.next.val != prev_val:
            if p.next.val == q.next.val:
                tmp_cnt += 1
            else:
                prev_val = p.next.val
                break
            q = q.next
        
        if tmp_cnt >= 2 and tmp_cnt > cnt:
            flag = False
            cnt = tmp_cnt
            to_rem_start = p.next
        elif tmp_cnt >= 2 and tmp_cnt == cnt:
            flag = True
        tmp_cnt = 1
        p = p.next

    if cnt == 1 or flag:
        return 0, start.next
    
    p = start
    while p.next != None and p.next != to_rem_start:
        p = p.next

    cnt_bak = cnt
    while p.next != None and cnt > 0:
        p.next = p.next.next
        cnt -= 1

    return cnt_bak, start.next


a = list_to_linked_list([1, 3, 3, 3, 5, 7, 11, 13, 13, 1, 2, 2, 2, 2, 3])
# a = list_to_linked_list([1, 3, 3, 3, 3, 5, 7, 11, 13, 13, 1, 2, 2, 2, 2, 3])
print_list(a)
res = remove(a)
print(res[0])
print_list(res[1])