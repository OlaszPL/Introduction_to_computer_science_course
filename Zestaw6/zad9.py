# Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne elementy listy przechowują kolejne cyfry.
# Proszę napisać funkcję zwiększającą taką liczbę o 1.

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

# bez sentinela bo rekurencja i lista niepusta to zbędne

def print_list(p):
    while p != None:
        print(str(p.val) + ' -> ', end = '')
        p = p.next
    print('END')

def append(p, el): # specyficzny przypadek bo p istnieje zawsze
    start = p
    while p.next != None:
        p = p.next
    
    p.next = Node(el)

    return start


def increase_by_one(p):
    def rek(p):
        if p.next == None:
            if p.val != 9:
                p.val += 1
                return p, 0
            else:
                p.val = 0
                return p, 1

        tmp = rek(p.next)

        p.next = tmp[0]

        if p.val == 9 and tmp[1] == 1:
            p.val = 0
            return p, 1
        elif tmp[1] == 1:
            p.val += 1
            
        return p, 0
        

    tmp = rek(p)

    if tmp[1] == 0:
        return tmp[0]
    else:
        a = Node(1, tmp[0])
        return a


a = Node(9)
b = append(a, 9)
a = append(a, 9)
a = append(a, 9)
a = append(a, 9)

print_list(a)

print_list(increase_by_one(a))