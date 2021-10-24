# DATA STRUCTURES

import time
import random


# --------------------LINKED LIST--------------------
# linked list: a linear data structure with successive elements connected by pointers
class Node():
    def __init__(self):
        self.__data = None
        self.__next = None
    
    def set_data(self, data):
        self.__data = data
    
    def get_data(self):
        return self.__data
    
    def set_next(self, nxt):
        self.__next = nxt
    
    def get_next(self):
        return self.__next
    
    def has_next(self):
        return self.__next is not None


class LinkedList():
    
    def __init__(self):
        self.__head = None
        self.__length = 0
        self.__start = 0
        self.__started = False
        self.__op = ''
        self.__end = 0
            
    def get_length(self):
        return self.__length

    def calc_length(self):
        current = self.__head
        count = 1
        while current.has_next():
            count += 1
            current = current.get_next()
        return count

    def get_node(self, index):
        current = self.__head
        count = 0
        while count != index:
            current = current.get_next()
            count += 1
        return current

    def display(self):
        for i in range(0, self.__length):
            current = self.get_node(i)
            print('index: {}, value: {}'.format(i, current.get_data()))

    def insert(self, index, node):
        if index == 0:
            node.set_next(self.__head)
            self.__head = node
        elif index == self.__length:
            current = self.get_node(self.__length - 1)
            current.set_next(node)
        else:
            current = self.get_node(index - 1)
            node.set_next(current.get_next())
            current.set_next(node)
        self.__length += 1

    def pop(self, index):
        if index == 0:
            self.__head = self.__head.get_next()
        elif index == self.__length - 1:
            current = self.get_node(self.__length - 2)
            current.set_next(None)
        else:
            before = self.get_node(index - 1)
            tgt = before.get_next()
            after = tgt.get_next()
            before.set_next(after)
        self.__length -= 1

    def search(self, tgt):
        self.__op = 'linear search'
        self.__started = True
        self.__start = time.time()
        count = 0
        current = self.__head
        while current.has_next():
            if current.get_data() == tgt:
                return count
            current = current.get_next()
            count += 1
        self.__end = time.time()
        return None

    def get_min_index(self, index):
        current = self.get_node(index)
        min_val = current.get_data()
        min_index = index
        for i in range(index + 1, self.__length):
            current = self.get_node(i)
            if current.get_data() < min_val:
                min_val = current.get_data()
                min_index = i
        return min_index

    def sort(self):
        self.__op = 'insertion sort'
        self.__started = True
        self.__start = time.time()
        for i in range(0, self.__length):
            index = self.get_min_index(i)
            current = self.get_node(index)
            self.pop(index)
            self.insert(i, current)
        self.__end = time.time()

    def time_analysis(self):
        if self.__started:
            print('length: {}'.format(self.__length))
            print('operation: {}'.format(self.__op))
            print('runtime: {}'.format(self.__end - self.__start))
        else:
            print('please execute an operation to perform time analysis')
            

l = LinkedList()
node = Node()
node.set_data(0)
l.insert(0, node)
for n in range(1, 5):
    node = Node()
    node.set_data(n)
    l.insert(n, node)
l.display()
print()
print(l.get_length())
print(l.calc_length())
print()

node = Node()
node.set_data(8)
l.insert(5, node)
l.display()
print()
node = Node()
node.set_data(9)
l.insert(4, node)
l.display()
print()
l.pop(3)
l.display()
print()
print(l.search(2))
print(l.search(10))
print()
l.sort()
l.display()
print(l.get_node(4).get_next().get_data())



import random

l = LinkedList()

for n in range(10):
    node = Node()
    node.set_data(random.randint(-20, 20))
    l.insert(n, node)

print()
l.display()

l.sort()

print()
l.display()

print()
print('time analysis')
l.time_analysis()
