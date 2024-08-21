#  Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza” 
# od pierwszej litery s2. Według tej zasady rozmieszczono napisy w liście cyklicznej, na przykład:
# ┌─bartek──leszek──marek──ola──zosia─┐
# └───────────────────────────────────┘
# Proszę napisać stosowne definicje typów oraz funkcję wstawiającą do listy napis z zachowaniem zasady
# poprzedzania. Do funkcji należy przekazać wskaźnik do listy oraz wstawiany napis, funkcja powinna zwrócić
# wartość logiczną wskazującą, czy udało się wstawić napis do listy. Po wstawieniu elementu wskaźnik do
# listy powinien wskazywać na nowo wstawiony element.

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def print_cycle(p):
    start = p
    while True:
        print(str(p.val) + ' -> ', end = '')
        p = p.next
        if p == start:
            print('poczatek cyklu')
            return

def insert(p, text):
    if p == None:
        p = Node(text)
        p.next = p
        return p
    
    if p.next == p:
        if p.val[-1] < text[0] and text[-1] < p.val[0]:
            new_node = Node(text, p.next)
            p.next = new_node
            return True
    
    start = p
    
    while p.next.val != None:
        if p.val[-1] < text[0] and text[-1] < p.next.val[0]:
            new_node = Node(text, p.next)
            p.next = new_node
            return True
        else:
            p = p.next
        if p == start:
            break
    
    return False


a = Node('bartek')
b = Node('leszek')
c = Node('marek')
d = Node('ola')
e = Node('zosia')

a.next = b
b.next = c
c.next = d
d.next = a

print_cycle(a)
print(insert(a, 'tomek'))
print_cycle(a)


