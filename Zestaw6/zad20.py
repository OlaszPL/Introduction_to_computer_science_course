# Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów. Krańce przedziałów
# określa uporządkowana para liczb całkowitych. Proszę napisać stosowne deklaracje oraz funkcję redukującą
# liczbę elementów listy. Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17] powinien zostać
# zredukowany do listy: [13,19] [2,6] [7,12]

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


def reduct(a):
    p = Node(None, a)
    start = p

    while p.next != None:
        p2 = p.next
        while p2.next != None:
            if p.next.val[0] <= p2.next.val[0] <= p.next.val[1] and p2.next.val[1] >= p.next.val[1]:
                p.next.val[1] = p2.next.val[1]
                p2.next = p2.next.next
            elif p2.next.val[0] <= p.next.val[0] and p.next.val[0] <= p2.next.val[1] <= p.next.val[1]:
                p.next.val[0] = p2.next.val[0]
                p2.next = p2.next.next
            else:
                p2 = p2.next
        
        p = p.next

    return start.next

t = [[15,19], [2,5], [7,11], [8,12], [5,6], [13,17]]
p = list_to_linked_list(t)
print_list(p)

print_list(reduct(list_to_linked_list(t)))