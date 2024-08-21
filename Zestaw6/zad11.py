# Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do której przekazujemy
# wskaźnik na początek oraz wartość klucza. Jeżeli element o takim kluczu występuje w liście należy go usunąć
# z listy. Jeżeli elementu o zadanym kluczu brak w liście należy element o takim kluczu wstawić do listy.

class Node:
    def __init__(self, val = None, key = None, next = None):
        self.val = val
        self.key = key
        self.next = next


def print_key_list(a):
    p = Node(None, None, a)
    while p.next != None:
        print(str(p.next.key) + ' : ' + str(p.next.val) + ' -> ', end = '')
        p = p.next
    print('END')


def add(a, key, el):
    p = Node(None, None, a)
    start = p
    while p.next != None:
        if p.next.key == key:
            p.next = p.next.next
            return start.next
        if p.next.val == el: # jeżeli element już istnieje to tylko przepnie index
            p.next.key = key
            return start.next
        p = p.next
    
    p.next = Node(el, key)
    return start.next

g = Node(0, 0)
g = add(g, 1, 1)
g = add(g, 2, 3)
g = add(g, 3, 13)
g = add(g, 16, 23)
print_key_list(g)
g = add(g, 3, 15)
print_key_list(g)
g = add(g, 17, 3)
print_key_list(g)