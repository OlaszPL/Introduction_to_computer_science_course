# 30. Dane są dwie niepuste listy, z których każda zawiera niepowtarzające się elementy.
# Elementy w pierwszej liście są uporządkowane rosnąco, w  drugiej elementy występują w
# przypadkowej kolejności. Proszę napisać funkcję, która z dwóch takich list stworzy jedną,
# w której uporządkowane elementy będą stanowić sumę mnogościową elementów z list wejściowych. 
# Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić wskazanie na listę wynikową.
# Na przykład dla list:
# 2 -> 3 -> 5 ->7-> 11
# 8 -> 2 -> 7 -> 4
# powinna pozostać lista:
# 2 -> 3 -> 4 -> 5 ->7-> 8 -> 11

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


# zał: a - posortowana, b - nieposortowana

def merge_lists(a, b):
    p, q = Node(None, a), Node(None, b)
    start_p = p

    while q.next != None: # bierzemy element z nieposortowanej i szukamy za każdym razem dla niego miescja w posortowanej
        p = start_p
        flag = False
        while p.next != None:
            if q.next.val < p.next.val:
                rem = q.next
                q.next = q.next.next
                rem.next = p.next
                p.next = rem
                flag = True
                break
            if q.next.val > p.next.val:
                p = p.next
            else: # równe
                q.next = q.next.next
                flag = True
                break
        if p.next == None:
            rem = q.next
            q.next = q.next.next
            rem.next = None
            p.next = rem
            flag = True
        if not flag:
            q = q.next

    return start_p.next

t1 = [2, 3, 5, 7, 11]
t2 = [8, 2, 7, 4]

a = list_to_linked_list(t1)
b = list_to_linked_list(t2)

print_list(a)
print_list(b)

print_list(merge_lists(a, b))