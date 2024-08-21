# Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze struktury listy odsyłaczowej.
# 1. czy element należy do zbioru
# 2. wstawienie elementu do zbioru
# 3. usunięcie elementu ze zbioru

class Node:
    def __init__(self, value = None, next = None):
        self.val = value
        self.next = next


def print_list(a):
    p = Node(None, a) # dodanie guardiana

    while p.next != None:
        print(str(p.next.val) + ' -> ', end = '')
        p = p.next
    
    print('END')


def add(a, el):
    p = Node(None, a) # dodanie guardiana
    start = p

    while p.next != None:
        if p.next.val == el: # bo ma to być bez powtarzających się elementów
            return start
        p = p.next
    
    p.next = Node(el) # jak p.next był None to tworzymy tu nowy węzeł z value = el

    return start.next # zwrócenie bez guardiana


def is_in_list(a, el):
    p = Node(None, a)

    while p.next != None:
        if p.next.val == el:
            return True
        p = p.next
        
    return False


def remove_iter(a, el):
    p = Node(None, a)
    start = p
    while p.next != None:
        if p.next.val == el:
            p.next = p.next.next
            return start.next
        p = p.next
    
    return start.next


def remove_rek(p, el): # rekurencyjnie

    if p == None:
        return None
    if p.val == el:
        return p.next
    
    p.next = remove_rek(p.next, el)

    return p

a = Node(1)

add(a, 7)
add(a, 8)

print_list(a)
a = remove_iter(a, 8)
# a = remove_rek(a, 8)

print_list(a)