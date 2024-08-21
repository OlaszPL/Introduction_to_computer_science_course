# Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci jednokierunkowej listy.
# Napisy w łańcuchu są uporządkowane leksykograficznie. Proszę napisać stosowne definicje typów oraz funkcję
# dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy oraz wstawiany napis, funkcja
# powinna zwrócić wartość logiczną wskazującą, czy w wyniku operacji moc zbioru uległa zmianie.

# w pythonie można porównywac stringi i to daje porządek leksykograficnzy

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

def add(a, el):
    p = Node(None, a)
    while p.next != None:
        if p.next.val == el:
            return False
        if p.next.val > el:
            new_node = Node(el, p.next)
            p.next = new_node
            return True
        p = p.next

    p.next = Node(el)
    return True

g = Node('0')
print(add(g, 'b'))
print(add(g, 'a'))
print(add(g, 'c'))
print(add(g, 'z'))
print(add(g, 'd'))
print(add(g, 'a'))
print(add(g, 'ala'))
print(add(g, 'ula'))
print(add(g, 'ela'))
print(add(g, 'Zosia'))
print(add(g, '123'))
print(add(g, 'Amelia'))
print_list(g)