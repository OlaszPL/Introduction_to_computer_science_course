# Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do 10 list, według ostatniej cyfry pola val.
# W drugim kroku powstałe listy należy połączyć w jedną listę odsyłaczową, która jest posortowana niemalejąco według ostatniej cyfry pola val.


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


def podziel_na_10(a):
    p = Node(None, a)
    T = [Node() for _ in range(10)] # tablica wskaźników do jak na razie pustych list
    start = tuple(T) # zachowa początkowe wskaźniki
    
    while p.next != None:
        rem = p.next # do odpięcia
        p.next = p.next.next
        rem.next = None # bardzo ważne jest odpięcie wskaźnika z tego co wypięliśmy i wpinamy gdzie indziej
        q = T[rem.val % 10] # odczyt wskaźnika z tablicy
        q.next = rem
        q = q.next
        T[rem.val % 10] = q # zapis wskaźnika następnego do tablicy
    
    return start # zwraca wskaźniki z guardianem bo wygodniej


def polacz(start):
    res = Node()
    res_start = res

    i = 0 # indeks do tablicy wskaźników

    while i < len(start):
        p = start[i]
        if p.next != None:
            res.next = p.next # aby nie przepinać guardiana i przepinamy całe listy bo taka kolejność jest dobra
            while res.next != None: # musimy się dostać na koniec listy by dodawać dalej
                res = res.next
        i += 1
    
    return res_start.next # zwróci już bez guardiana


t = [1, 2, 3, 11, 12, 13, 14, 24, 21]

podzielone = podziel_na_10(list_to_linked_list(t))

print_list(polacz(podzielone))