# Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza powinna zawierać klucze
# parzyste dodatnie, drugi klucze nieparzyste ujemne, pozostałe elementy należy usunąć z pamięci. Do funkcji
# należy przekazać wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja powinna zwrócić
# liczbę usuniętych elementów.

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

def zad31(data, pos_even, neg_odd): # 2 ostatnie muszą być przekazane jako puste listy -> mają guardiana
    p = Node(None, data)
    start_pos_even, start_neg_odd = pos_even, neg_odd
    cnt = 0

    while p.next != None:
        if p.next.val > 0 and p.next.val % 2 == 0:
            rem = p.next
            p.next = p.next.next
            rem.next = None
            pos_even.next = rem
            pos_even = pos_even.next
        elif p.next.val < 0 and p.next.val % 2 != 0:
            rem = p.next
            p.next = p.next.next
            rem.next = None
            neg_odd.next = rem
            neg_odd = neg_odd.next
        else:
            p.next = p.next.next
            cnt += 1

    return cnt

t1 = [1, 2, -3, 4, 5, 6, -7, 8, -13, 45, 12, 16, 87, 90]
data = list_to_linked_list(t1)
pos_even = Node()
neg_odd = Node()

print(zad31(data, pos_even, neg_odd))

print_list(pos_even.next)
print_list(neg_odd.next)