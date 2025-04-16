"""
Lista połączona (Linked List)
-odwołanie do elementu: O(n) -  wymaga przejścia przez listę
-dodawanie elementów: O(1)
-usuwanie elementów: O(1)
-przeszukiwanie linked list: O(n)
"""

# Tworzenie list połączonych

# Klasa Node reprezentująca wierzchołek listy
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Klasa LinkedList reprezentująca listę połączoną

class LinkedList:
    def __init__(self):
        self.head = None

    # definicja metody append, która dodaje do listy nowy wierzchołek
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    # definicja metody string, która pozwoli łątwo wyświetlić wszystkie wierzchołki listy
    def __str__(self):
        node = self.head
        values=[]
        while node is not None:
            values.append(str(node.data))
            node=node.next
        return ' -> '.join(values)

        # n=len(values)
        # for val in range(n):
        #     values[val]=str(values[val])
        # return values

    # przeszukiwanie list połączonych
    def search(self, target):
        current=self.head
        while current:
            if current.data == target:
                return True
            else:
                current=current.next
        return False

    def remove(self,target):
        if self.head and self.head.data == target:
            self.head = self.head.next
            return

        current=self.head
        previous = None
        while current:
            if current.data == target:
                previous.next = current.next
                return
            previous = current
            current=current.next

    def reverse_list(self):
        current=self.head
        previous = None
        while current:
            next=current.next
            current.next=previous
            previous = current
            current=next
        self.head=previous

    def is_cycle(self):
        slow=self.head
        fast=self.head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False




a_list = LinkedList()
a_list.append("wtorek")
a_list.append("środa")
print(a_list)

# Wbudowana struktura danych deque, która korzysta z list połączonych
from collections import deque
d = deque()
d.append('Harry')
d.append('Potter')

for item in d:
    print(item)

###########
# Przeszukiwanie listy:
from random import randint
T1 = LinkedList()

for i in range(20):
    j = randint(1,30)
    T1.append(j)

print(T1)
print(T1.search(10))

