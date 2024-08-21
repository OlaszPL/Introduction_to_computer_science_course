# Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne. W pierwszej liście
# liczby są posortowane rosnąco, a w drugiej nie. Proszę napisać funkcję usuwającą z obu list liczby występujące
# w obu listach. Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić łączną liczbę
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

# a - posortowana, b - nie

def remove_common_elem(a, b):
    p = Node(None, a)
    q = Node(None, b)
    cnt = 0
    start_p = p
    start_q = q

    while q.next != None:
        p = start_p
        flag = False
        while p.next != None and p.next.val <= q.next.val:
            if p.next.val == q.next.val:
                cnt += 2
                p.next = p.next.next
                q.next = q.next.next
                flag = True
                break
            else:
                p = p.next
        if not flag:
            q = q.next
    
    return cnt, start_p.next, start_q.next

t1 = [1, 2, 3, 4, 5, 6, 7, 10, 15]
t2 = [1, 12, 3, 6, 20, 10]

a = list_to_linked_list(t1)
b = list_to_linked_list(t2)

res = remove_common_elem(a, b)
print(res[0])
print_list(res[1])
print_list(res[2])