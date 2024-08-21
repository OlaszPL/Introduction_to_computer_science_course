# Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów
# w cyklu.

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def len_of_cycle(p):
    cnt = 1
    fast = p
    slow = p

    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    slow = slow.next
    while slow != fast:
        slow = slow.next
        cnt += 1

    return cnt

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

print(len_of_cycle(a))