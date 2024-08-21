# Dana jest niepusta lista cykliczna, zbudowana z elementów zawierających pola key i next, której węzły
# przechowują liczby całkowite. Proszę napisać funkcję separate(p) która rozdziela listę cykliczną na dwie
# listy cykliczne. Pierwsza powinna zawierać klucze parzyste dodatnie, druga klucze nieparzyste ujemne,
# pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać wskaźniki na listę z danymi.
# Funkcja powinna zwrócić wskaźniki na powstałe listy oraz liczbę usuniętych elementów.


class Node:
    def __init__(self, key = None, next = None):
        self.key = key
        self.next = next

def print_cycle(p):
    start = p
    while True:
        print(str(p.key) + ' -> ', end = '')
        p = p.next
        if p == start:
            print('poczatek cyklu')
            return

def separate(p):
    cnt = 0
    pos_even, neg_odd = None, None
    start_pos_even, start_neg_odd = None, None

    while p.next != p:
        if p.next.key > 0 and p.next.key % 2 == 0:
            if not pos_even:
                rem = p.next
                p.next = p.next.next
                pos_even = rem
                pos_even.next = None
            else:
                rem = p.next
                p.next = p.next.next
                rem.next = None
                pos_even.next = rem
                pos_even = pos_even.next
            if not start_pos_even:
                start_pos_even = pos_even
        elif p.next.key < 0 and p.next.key % 2 != 0:
            if not neg_odd:
                rem = p.next
                p.next = p.next.next
                neg_odd = rem
                neg_odd.next = None
            else:
                rem = p.next
                p.next = p.next.next
                rem.next = None
                neg_odd.next = rem
                neg_odd = neg_odd.next
            if not start_neg_odd:
                start_neg_odd = neg_odd
        else:
            p.next = p.next.next
            cnt += 1
        
    if p.key > 0 and p.key % 2 == 0 and pos_even:
        rem = p
        rem.next = None
        pos_even.next = rem
        pos_even = pos_even.next
    elif p.key < 0 and p.key % 2 != 0 and neg_odd:
        rem = p
        rem.next = None
        neg_odd.next = rem
        neg_odd = neg_odd.next
    else:
        p.next = None

    if pos_even:
        pos_even.next = start_pos_even
    if neg_odd:
        neg_odd.next = start_neg_odd

    return start_pos_even, start_neg_odd, cnt


a = Node(0)
b = Node(-2)
c = Node(6)
d = Node(24)
e = Node(-15)

a.next, b.next, c.next, d.next, e.next = b, c, d, e, a

print_cycle(a)

res = separate(a)

print(res[2])

print_cycle(res[0])
print_cycle(res[1])