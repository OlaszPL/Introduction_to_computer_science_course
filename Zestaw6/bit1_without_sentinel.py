
class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def print_list(head): # podajemy pierwszy węzeł
    while head != None: # do momentu kiedy węzeł istnieje
        print(str(head.val) + ' -> ', end = '')
        head = head.next
    print('KONIEC')

def remove_element(p, to_delete): # zakładamy, że usuwamy pierwszy znaleziony element o danej wartości
    prev = None # trzyma poprzedni wskaźnik
    start = p # pointer

    while p != None:
        if p.val == to_delete:
            if prev == None: # jeżeli to pierwszy element
                return p.next
            else:
                prev.next = prev.next.next # przepnie nexta z poprzedniego wskaźnika tak aby ominął element, który usuwamy
                return start
        
        prev = p
        p = p.next
    
    return start # przypadku gdy nie było tej wartości


def add_element(p, to_add):
    start = p
    prev = None
    while p != None:
        prev = p
        p = p.next
    
    if prev == None: # przekażemy do funkcji pustą listę
        return Node(to_add)
    
    prev.next = Node(to_add) # bo wskaźnik prev.next nie wskazywał już na nic

    return start # zwraca początkowy wskaźnik



c = Node(3) # tutaj wskaźnik na następny == None
b = Node(2, c) # drugi argument to wskaźnik to następnego elementu
a = Node(1, b)

print_list(a)

a = add_element(a, 4)
print_list(a)