# Elementy w liście są uporządkowane według wartości klucza. Proszę napisać funkcję usuwającą z listy elementy o nieunikalnym kluczu.
# Do funkcji przekazujemy wskazanie na pierwszy element listy, funkcja powinna zwrócić liczbę usuniętych elementów.


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
    cnt = 0

    while p.next != None:
        p2 = p.next
        flag = False
        while p2.next != None and p2.next.val <= p.next.val:
            if p.next.val == p2.next.val:
                flag = True
                p2.next = p2.next.next
                cnt += 1
            else:
                p2 = p2.next
        
        if flag:
            p.next = p.next.next
            cnt += 1
        else:
            p = p.next
    
    return cnt

t = [1, 2, 2, 3, 4, 5, 5, 10]
p = list_to_linked_list(t)
print_list(p)
print(uniq(p))
print_list(p)