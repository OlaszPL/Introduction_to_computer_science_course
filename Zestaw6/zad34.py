# Proszę napisać funkcję, która usuwa z listy cyklicznej elementy, których klucz występuje
# dokładnie k razy. Do funkcji należy przekazać wskazanie na jeden z elementów listy, oraz liczbę k, funkcja
# powinna zwrócić informację czy usunięto jakieś elementy z listy.

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def print_cycle(p):
    start = p
    while True:
        print(str(p.val) + ' -> ', end = '')
        p = p.next
        if p == start:
            print('poczatek cyklu')
            return
        
    
def values(p):
    T = []
    start = p
    while True:
        T += [p.val]
        p = p.next
        if p == start:
            return T
        
def to_remove(T, k):
    res = []
    n = len(T)

    for i in range(n):
        if T[i] != None:
            cnt = 1
            for j in range(i + 1, n):
                if T[i] == T[j]:
                    cnt += 1
                    T[j] = None

            if cnt == k:
                res += [T[i]]
            T[i] = None
    
    return res

def zad34(p, k):
    to_rem = to_remove(values(p), k)
    flag = False
    
    for el in to_rem:
        cnt = 0
        while cnt != k:
            if p.next.val == el:
                p.next = p.next.next
                flag = True
                cnt += 1
            else:
                p = p.next
    
    return flag, p # zwraca w dowolnej kolejności bo to cykl

f = Node(2)
e=Node(1,f)
d=Node(2,e)
c=Node(3,d)
b=Node(2,c)
a=Node(1,b)
f.next=a

print_cycle(a)

res = zad34(a, 3)

print(res[0])

print_cycle(res[1])