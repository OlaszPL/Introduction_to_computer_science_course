# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
# ..def init (self,val,next=None):
# ....self.val = val
# ....self.next = next
# Lista zawiera wartości będące liczbami naturalnymi Proszę napisać funkcję repair(p), (p wskazuje
# na pierwszy element listy) która przekształca listę tak aby liczby parzyste znalazły się na końcu listy.
# Funkcja powinna zwrócić wskazanie na przekształconą listę.
# Komentarz: Można założyć, że lista wejściowa liczy więcej niż 2 element.

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


def repair(p):
    a = Node(None, p)
    not_even = Node()
    start_not_even = not_even
    even = Node()
    start_even = even

    while a.next != None:
        rem = a.next
        a.next = a.next.next
        rem.next = None
        if rem.val % 2 == 0:
            even.next = rem
            even = even.next
        else:
            not_even.next = rem
            not_even = not_even.next
    
    not_even.next = start_even.next

    return start_not_even.next

t = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 14, 17, 20, 34, 67]
p = list_to_linked_list(t)
print_list(p)

print_list(repair(p))
