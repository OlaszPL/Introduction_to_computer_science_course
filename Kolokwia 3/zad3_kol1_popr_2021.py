# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
# ..def init(self,val,next=None):
# ....self.val = val
# ....self.next = next
# Lista zawierała wartości stanowiące kolejne wyrazy ciągu arytmetycznego. Z wnętrza listy usunięto
# pewną liczbę elementów. Proszę napisać funkcję repair(p), (p wskazuje na pierwszy element listy) która
# uzupełnia listę elementami, tak aby ponownie zawierała kolejne wyrazy ciągu arytmetycznego. Funkcja
# powinna zwrócić liczbę wstawionych elementów.
# Komentarz: Można założyć, że lista wejściowa liczy więcej niż 2 elementy

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def list_to_linked_list(t):
    g = Node() # guardian
    for i in range(len(t) - 1, -1, -1):
        new_node = Node()
        new_node.val = t[i]
        new_node.next = g.next  # type: ignore
        g.next = new_node # type: ignore

    return g.next

def print_list(a):
    p = Node()
    p.next = a
    while p.next != None:
        print(str(p.next.val) + ' -> ', end = '')
        p = p.next
    print('END')

def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    
    return a

def find_r(a):
    p = Node(None, a)
    r = 0
    while p.next != None and p.next.next != None:
        r = nwd(r, p.next.next.val - p.next.val)
        p = p.next
    
    return r

def repair(p):
    r = find_r(p)
    q = Node(None, p)
    start = q

    while q.next != None and q.next.next != None:
        if q.next.next.val != q.next.val + r:
            new_node = Node(q.next.val + r, q.next.next)
            q.next.next = new_node
        q = q.next

    return start.next


t = [1,129,409]
p = list_to_linked_list(t)

print_list(p)

print_list(repair(p))