# Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca wskaźnik do
# ostatniego elementu przed cyklem.

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def last_el_bef_cycle(p):
    slow = p
    fast = p

    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    start = p
    while start.next != fast.next:
        start = start.next
        fast = fast.next
    
    return start

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = c

print(last_el_bef_cycle(a).val) # type: ignore