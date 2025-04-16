"""
Stos (stack) - last in, first out (LIFO)
-odłożenie elementu na stos: O(1)
-zdjęcie elementu ze stosu: O(1)
-odwołanie do elementu: O(n)
-wyszukiwanie elementu: O(n)
"""

# Tworzenie stosu

# Implementacja przy pomocy tablicy:
class Stack:
    def __init__(self):
        self.items = []

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items)==0

    def peek(self):
        return self.items[-1]

# Implementacja przy pomocy linked listy

# klasa wierzchołka listy połączonej
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# klasa Stack, dla definicji początku listy
class Stack1:
    def __init__(self):
        self.head=None

    def push(self,data):
        node = Node(data)
        if self.head is None:
            self.head=node
        else:
            node.next=self.head
            self.head=node

    def pop(self):
        if self.head is None:
            raise IndexError("próba zdjęcia z pustego stosu")
        new_node = self.head
        self.head = self.head.next
        return new_node.data

stack =Stack1()
stack.push(1)
stack.push(2)
stack.push(3)

for i in range(3):
    print(stack.pop())

# head → 20 → 10 → None
# node = Node(30)
# 30.next = head <-> 30.next = 20
# head = 30

# Implementacja stosu w postaci "zwykłej" listy
stack =[]
print(stack)
stack.append("Kanye West")
print(stack)
stack.append("Jaz-Z")
stack.append("Chance the Rapper")
print(stack)
stack.pop()
print(stack)

# Używanie stosów do odwracania kolejnosci znaków w łańcuchach

def reverse_string(a_string):
    stack = []
    string = ""
    for c in a_string:
        stack.append(c)
    for el in a_string:
        string += stack.pop()
    return string

print(reverse_string('Filiżanka'))

class MainStack():
    def __init__(self):
        self.main =[]
        self.min =[]

    def push(self,n):
        if len(self.main)==0:
            self.min.append(n)
        elif n<=self.min[-1]:
            self.min.append(n)
        else:
            self.min.append(self.min[-1])
        self.main.append(n)
