class Node:

    def __init__(self, val=None):
        self.__val = val
        self.__prev = None
        self.__next = None

    def get_val(self):
        return self.__val

    def set_val(self, val):
        self.__val = val

    def get_prev(self):
        return self.__prev

    def set_prev(self, node):
        self.__prev =  node

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node


class DoubleLinkedList:

    def __init__(self):
        self.__head = Node()
        self.__tail = Node()
        self.__head.set_next(self.__tail)
        self.__tail.set_prev(self.__head)

    def get_size(self):
        count = 0
        current = self.__head
        while current is not None:
            current = current.get_next()
            count += 1
        return count

    def get_head(self):
        return self.__head

    def set_head(self, val):
        if self.__head is not None:
            input_head = Node(val=val)
            input_head.set_next(self.__head)
            self.__head.set_prev(input_head)
            self.__head = input_head
        else:
            self.__head.set_val(val=val)

    def get_tail(self):
        return self.__tail

    def set_tail(self, val):
        if self.__tail is not None:
            input_tail = Node(val=val)
            input_tail.set_prev(self.__tail)
            self.__tail.set_next(input_tail)
            self.__tail  = input_tail
        else:
            self.__tail.set_val(val=val)

    def insert(self, index, val):
        size = self.get_size
        if 0 < index < size - 1:
            count = 0
            current = self.__head
            node = Node(val=val)
            while current is not self.__tail:
                if count == index - 1:
                    node.set_prev(current)
                    node.set_next(current.get_next())
                    current.set_next(node)
                    current.get_next().set_prev(node)
                    break
                else:
                    current = current.get_next()
                    count += 1
        elif index == 0:
            self.set_head(val)
        elif index == size - 1:
            self.set_tail(val)
        else:
            raise IndexError()

    def pop(self, index):
        count = 0
        current = self.__head
        while current is not self.__tail:
            if count == index:
                current.get_prev().set_next(current.get_next())
                current.get_next().set_prev(current.get_prev())
                return current
            else:
                current = current.get_next()
                count += 1

    def search(self, val):
        current = self.__head
        count = 0
        while current is not None:
            if current.get_val() == val:
                return count
            current = current.get_next()
            count += 1
        return -1

    def get_min(self, start_point=0):
        count = 0
        current = self.__head
        while count < start_point:
            current = current.get_next()
            count += 1
            
        min_val = current.get_val()
        min_index = count
        while current is not None:
            if current.get_val() < min_val:
                min_val = current.get_val()
                min_index = count
            current = current.get_next()
            count += 1
        return min_index

    def sort(self):
        size = self.get_size()
        for n in range(size):
            min_index = self.get_min(start_point=n)
            min_node = self.pop(min_index)
            if min_node is self.__head:
                self.__head = self.__head.get_()
                self.__head.set_next(
            self.insert(n, min_node.get_val())


    
