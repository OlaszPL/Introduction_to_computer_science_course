# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jednokierunkowej, usuwa z niej wszystkie elementy,
# w których wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek.

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


def to_remove(num):
    cnt1, cnt2 = 0, 0
    
    while num > 0:
        if num % 3 == 1:
            cnt1 += 1
        elif num % 3 == 2:
            cnt2 += 1
        num //= 3
    
    return cnt1 > cnt2


def zad15(a):
    p = Node(None, a)
    start = p
    while p.next != None:
        if to_remove(p.next.val):
            p.next = p.next.next
        else:
            p = p.next
    
    return start.next


t = [1, 2, 3, 4, 15, 16, 10, 8, 13]

a = list_to_linked_list(t)

print_list(a)
print_list(zad15(a))