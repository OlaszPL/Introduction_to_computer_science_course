
class Node:
    def __init__(self, data = None): # zawsze się dzieje podczas inicjalizacji nowego węzła
        self.data = data
        self.next = None # domyślnie każdy węzeł będzie miał nastawiony wskaźnik na następny element na None

class linked_list:
    def __init__(self):
        self.head = Node() # guardian

    def append(self, data):
        new_node = Node(data)
        cur = self.head #startujemy od pierwszego wskaźnika listy, którym tutaj jest guardian
        while cur.next != None: # dopóki istnieje następny element listy
            cur = cur.next
        
        cur.next = new_node # type: ignore

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None: # gdy mamy guardiana to następny == None, więc go nie zliczy
            total += 1
            cur = cur.next
        
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next # najpierw przestawiamy a potem dodajemy bo mamy guardiana na początku
            elems.append(cur_node.data)
        
        print(elems)

    def get(self, index):
        if index >= self.length():
            print('ERROR: "Get" Index out of range!')
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next # type: ignore # najpierw dajemy na następny bo pierwszy jest guardian
            if cur_idx == index:
                return cur_node.data # type: ignore
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print('ERROR: "Erase" Index out of range!')
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next # type: ignore
            if cur_idx == index:
                last_node.next = cur_node.next # type: ignore
                return
            cur_idx += 1


my_list = linked_list()

my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.display()

print(my_list.get(2))

my_list.erase(1)

my_list.display()