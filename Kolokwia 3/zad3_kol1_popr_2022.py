# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej przechowującej liczby
# naturalne:
# class Node:
# def __init__(self):
# self.val = None
# self.next = None
# Proszę napisać funkcję Two(p), która otrzymuje wskazanie na listę i rozdziela elementy listy do dwóch
# list. W pierwszej powinny znaleźć się elementy, które w liście wejściowej występowały dokładnie dwa
# razy, a w drugiej wszystkie pozostałe. Funkcja powinna zwrócić wskaźniki do powstałych dwóch list.

class Node:
    def __init__(self):
        self.val = None
        self.next = None

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

def two(a):
    p = Node()
    p.next = a
    two = Node()
    other = Node()
    start_two = two
    start_other = other

    while p.next != None:
        cnt = 1
        q = p.next

        while q.next != None:
            if p.next.val == q.next.val:
                cnt += 1
            q = q.next
        
        k = p.next

        while k.next != None:
            if k.next.val == p.next.val:
                rem = k.next
                k.next = k.next.next
                rem.next = None
                if cnt == 2:
                    two.next = rem
                    two = two.next
                else:
                    other.next = rem
                    other = other.next
            else:
                k = k.next
        
        rem = p.next
        p.next = p.next.next
        rem.next = None
        if cnt == 2:
            two.next = rem
            two = two.next
        else:
            other.next = rem
            other = other.next

    return start_two.next, start_other.next


t = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 16, 17, 20, 30, 20, -10, 20]

a = list_to_linked_list(t)

print_list(a)
print()
res = two(a)

print_list(res[0])
print()
print_list(res[1])