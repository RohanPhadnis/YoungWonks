# Queue: ordered FIFO data structure. insertions done at the end, deletions done at the begining

import random

class Queue:

    def __init__(self, limit):
        self.__array = []
        self.__limit = limit

    def get_limit(self):
        return self.__limit

    def get_size(self):
        return len(self.__array)

    def get_head(self):
        if self.get_size() > 0:
            return self.__array[0]
        else:
            raise IndexError('Queue Underflow!')
        
    def en_queue(self, val):
        if self.get_size() < self.__limit:
            self.__array.append(val)
        else:
            raise IndexError ('Queue Overflow!')

    def de_queue(self):
        if self.get_size() > 0:
            x = self.get_head()
            self.__array.pop(0)
            return x
        else:
            raise IndexError('Que Underflow!')

    def is_empty(self):
        return self.get_size == 0

    def is_full(self):
        return self.get_size() == self.get_limit()

    def __str__(self):
        return str(self.__array)



queue = Queue(100)
for n in range(100):
    queue.en_queue(n)

print(queue)

for _ in range(5):
    popped = queue.de_queue()
    queue.en_queue(popped)


print(queue)
