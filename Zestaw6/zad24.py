# Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów
# przed cyklem.

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next


def len_before_cycle(p):
    slow = p
    fast = p

    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    cnt = 0
    start = p
    while start != fast: # jak się spotkają to jeden zaczyna od początku a drugi dalej krąży w cyklu ale o 1
        start = start.next
        fast = fast.next
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

print(len_before_cycle(a))