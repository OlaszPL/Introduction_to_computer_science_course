# Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne. W obu listach
# liczby są posortowane rosnąco. Proszę napisać funkcję usuwającą z każdej listy liczby nie występujące w
# drugiej. Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić łączną liczbę
# usuniętych elementów.

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

def zad29(a, b): # wykonuje polecenie i zwraca krotkę z liczbą usuniętych elemtów i wskazaniami na pierwsze elementy obu list
    p, q = Node(None, a), Node(None, b)
    start_p, start_q = p, q
    cnt = 0

    while p.next != None and q.next != None:
        if p.next.val < q.next.val:
            p.next = p.next.next
            cnt += 1
        elif p.next.val > q.next.val:
            q.next = q.next.next
            cnt += 1
        else:
            p = p.next
            q = q.next
    
    while p.next != None:
        cnt += 1
        p.next = p.next.next

    while q.next != None:
        cnt += 1
        q.next = q.next.next
    
    return cnt, start_p.next, start_q.next

t1 = [1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 45]
t2 = [4, 6, 8, 10, 20, 34, 56]

a = list_to_linked_list(t1)
b = list_to_linked_list(t2)

print_list(a)
print_list(b)

res = zad29(a, b)
print(res[0])
a = res[1]
b = res[2]

print_list(a)
print_list(b)