# Dana jest lista, który być może zakończona jest cyklem. Napisać funkcję, która sprawdza ten fakt.

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def has_a_cycle(p):
    if p == None or p.next == None:
        return False
    
    fast = p
    slow = p

    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
        
    return False

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

print(has_a_cycle(a))