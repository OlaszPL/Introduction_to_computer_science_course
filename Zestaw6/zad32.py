# Lista reprezentuje wielomian o współczynnikach całkowitych. Elementy w liście ułożone są
# według rosnących potęg. Proszę napisać funkcję obliczającą różnicę dwóch dowolnych wielomianów.
# Wielomiany reprezentowane są przez wyżej opisane listy. Procedura powinna zwracać wskaźnik do nowo
# utworzonej listy reprezentującej wielomian wynikowy. Listy wejściowe powinny pozostać niezmienione.

# prz. 3 -> 2x -> 14x^2 -> 13x3 -> 0x^4 - > 5x^6 ...

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def print_list(a):
    p = Node(None, a)
    k = 0
    while p.next != None:
        print(str(p.next.val) + 'x^' + str(k) + ' -> ', end = '')
        p = p.next
        k += 1
    print('END')

def list_to_linked_list(t):
    p = Node()
    for i in range(len(t) - 1, -1, -1):
        new_node = Node(t[i], p.next)
        p.next = new_node
    return p.next

def zad32(a, b):
    p, q = Node(None, a), Node(None, b)
    res = Node()
    start_res = res

    while p.next != None and q.next != None:
        res.next = Node(p.next.val - q.next.val)
        res = res.next
        p = p.next
        q = q.next

    if p.next != None:
        res.next = p.next
    elif q.next != None:
        res.next = q.next

    return start_res.next


w1 = [1, 2, 3, 0, 6, 12, 6, 7, 10]
w2 = [1, 3, -1, 1, -6, -3, 6]

a = list_to_linked_list(w1)
b = list_to_linked_list(w2)

print_list(a)
print()
print_list(b)
print()

print_list(zad32(a, b))