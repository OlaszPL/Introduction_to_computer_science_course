
class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next
        

def print_list(head): # podajemy pierwszy węzeł
    print('GUARDIAN -> ', end = '')
    while head.next != None: # do momentu kiedy węzeł istnieje, patrzymy na jeden element wprzód bo pierwszym jest guardian
        print(str(head.next.val) + ' -> ', end = '')
        head = head.next
    print('KONIEC')


def remove_element(p, to_delete): # zakładamy, że usuwamy pierwszy znaleziony element o danej wartości
    # prev zbędny bo mamy guardiana (mamy gwarancję, żę element do usunięcia nigdy nie jest pierwszy)
    start = p # pointer

    while p.next != None:
        if p.next.val == to_delete:
            p.next = p.next.next # przepina wskaźnik do przodu
            return start
        
        p = p.next
    
    return start # przypadku gdy nie było tej wartości


def add_element(p, to_add):
    # prev znowu nie jest potrzebny
    start = p
    while p.next != None:
        p = p.next
    
    p.next = Node(to_add) # bo wskaźnik prev.next nie wskazywał już na nic

    return start # zwraca początkowy wskaźnik



c = Node(3) # tutaj wskaźnik na następny == None
b = Node(2, c) # drugi argument to wskaźnik to następnego elementu
a = Node(1, b)

g = Node(None, a) # sztuczny początek listy (guardian)

print_list(g)
g = add_element(g, 4)
print_list(g)
g = remove_element(g, 3)
print_list(g)