# Stack: ordered data structure with first in last out. Insertions and deletions are done at the end

import random


class Node:

    def __init__(self, val):
        self.__val = val
        self.__next = None

    def get_val(self):
        return self.__val

    def set_val(self, val):
        self.__val = val

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node

    def has_next(self):
        return self.__next is not None


class LinkedStack:

    def __init__(self, limit):
        self.__top = None
        self.__limit = limit

    def get_limit(self):
        return self.__limit

    def get_size(self):
        count = 0
        if self.__top is not None:
            count = 1
            current = self.__top
            while current.has_next():
                current = current.get_next()
                count += 1
        return count

    def get_top(self):
        if self.__top is not None:
            return self.__top
        else:
            raise IndexError("Stack Underflow!")

    def is_empty(self):
        return self.__top is None

    def is_full(self):
        return self.get_size() == self.__limit

    def push(self, val):
        if self.get_size() == 0:
            self.__top = Node(val)
        elif 0 < self.get_size() < self.__limit:
            current = self.__top
            while current.has_next():
                current = current.get_next()
            current.set_next(Node(val))
        else:
            raise IndexError("Stack Overflow!")

    def pop(self):
        size = self.get_size()
        if size == 0:
            raise IndexError("Stack Underflow!")
        elif size == 1:
            node = Node(self.__top.get_val())
            self.__top = None
        else:
            count = 1
            current = self.__top
            while count < size - 1:
                current = current.get_next()
                count += 1
            node = current.get_next()
            current.set_next(None)
        return node

    def display(self):
        size = self.get_size()
        if size == 0:
            print()
        else:
            index = 0
            current = self.__top
            while current is not None:
                print('index: {}; val: {}'.format(index, current.get_val()))
                current = current.get_next()
                index += 1
                
    def __contains__(self, key):
        current = self.__top
        while current != None:
            if current is key:
                return True
        return False

    def get_count(self, val):
        current = self.__top
        count = 0
        while current is not None:
            if current.get_val() == val:
                count += 1
            current = current.get_next()
        return count

    def sort(self):
        output = LinkedStack(self.__limit)
        size = self.get_size()
        if size > 0:
            for _ in range(size):
                min_node = self.__top
                current = self.__top
                while current is not None:
                    if (
                            self.get_count(min_node.get_val()) == output.get_count(min_node.get_val()) or
                            (current.get_val() <= min_node.get_val() and output.get_count(current.get_val()) < self.get_count(current.get_val()))
                        ):
                        min_node = current
                    current = current.get_next()
                output.push(min_node.get_val())
        return output


class ArrayStack:

    def __init__(self, limit):
        self.__limit = limit
        self.__array = []

    def push(self, val):
        if len(self.__array) < self.__limit:
            self.__array.append(val)
        else:
            raise IndexError("Stack Overflow!")

    def pop(self):
        if len(self.__array) > 0:
            x = self.__array[-1]
            self.__array.pop()
            return x
        else:
            raise IndexError('Stack Underflow!')

    def get_limit(self):
        return self.__limit

    def get_size(self):
        return len(self.__array)

    def get_top(self):
        if len(self.__array) > 0:
            return self.__array[0]
        else:
            raise IndexError('Stack Underflow!')

    def is_empty(self):
        return len(self.__array) == 0

    def is_full(self):
        return len(self.__array) == self.__limit

    def __str__(self):
        return str(self.__array)

    def sort(self):
        copy = self.__array.copy()
        output = ArrayStack(self.__limit)
        for _ in range(self.get_size()):
            output.push(min(copy))
            copy.remove(min(copy))
        return output


stack = ArrayStack(100)
for n in range(100):
    stack.push(random.randint(-2000, 2000))
print(stack)
print()
sorted_stack = stack.sort()
print(sorted_stack)

