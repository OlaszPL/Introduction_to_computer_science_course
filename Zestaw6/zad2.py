# Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej. Proszę napisać trzy funkcje:
# – inicjalizującą tablicę,
# – zwracającą wartość elementu o indeksie n,
# – podstawiającą wartość value pod indeks n.

class Node:
    def __init__(self, value = None, index = None, next = None):
        self.val = value
        self.index = index
        self.next = next


def init(val, index = 0):
    return Node(val, index)


def get(a, index):
    p = Node(None, None, a)

    while p.next != None and p.next.index < index:
        p = p.next

    if p.next != None and p.next.index == index:
        return p.next.val 
    
    return 0


def insert(a, index, el):
    p = Node(None, None, a)
    start = p
    while p.next != None and p.next.index < index:
        p = p.next

    if p.next != None and p.next.index == index:
        p.next.val = el # wstawiamy w zamian za innego jeżeli istniał węzeł
    else:
        new_node = Node(el, index, p.next) # przypisujemy next jako p.next jakby się okazało, że p.next.index > index i chcemy przepchnąć tablicę w prawo
        p.next = new_node

    return start.next


def print_list(a):
    p = Node(None, None, a)
    while p.next != None:
        print(str(p.next.index) + ' : ' + str(p.next.val) + ' -> ', end = '')
        p = p.next
    print('END')


g = init(1)

insert(g, 0, 20)
insert(g, 6, 25)
insert(g, 23, 33)
insert(g, 7, 3)

print_list(g)

insert(g, 23, 600100100)

print(get(g, 23))

print_list(g)