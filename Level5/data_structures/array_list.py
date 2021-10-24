# --------------------ARRAYS--------------------
# array: a list of elements with a datatype contraint; all elements in an array must be of the same datatype
import time
import random
from array import *


def get_min(arr, index):
    min_val = arr[index]
    min_index = index
    for i in range(index, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_index = i
    return min_index


def sort(arr):
    for i in range(0, len(arr)):
        min_index = get_min(arr, i)
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp


arr = array('i', [random.randint(-20, 20) for _ in range(10)])
print(arr)



# traversal
for x in arr:
    print(x)
print()

# indexing
print(arr[0])
print(arr[3])
print()

# insertion
arr.insert(2, 6)
for x in arr:
    print(x)
print()

# deletion by value
arr.remove(5)
for x in arr:
    print(x)
print()

# deletion by index
arr.pop(0)
for x in arr:
    print(x)
print()

#search
print(arr.index(4))
print()

# update operation
arr[2] = 8
for x in arr:
    print(x)
print()



start = time.time()
sort(arr)
end = time.time()
print(arr)
print('sort time: {}'.format(end - start))




'''
Typecode |                  Value                 |     Definition
---------|-------------------------------------|
    b    |   signed integer size 1 bytes/td>|   1 bit used for +/- and 7 bits used to store numerical value. range is -127 to +127, inclusive
---------|-------------------------------------|
    B    |   unsigned integer of size 1 byte |   8 bits used to store numerical value. only positive values exist. range is 0 to 255, inclusive
---------|-------------------------------------|
    c    |   character of size 1 byte            |    stores single characters. can represent unicode values from ordinal 0 to ordinal 255, inclusive
---------|-------------------------------------|
     i   |    signed integer of size 2 bytes   |   1 bit used for +/- and 15 bits used to store numerical value. range is -2^15 to +2^15, inclusive
---------|-------------------------------------|
     I   |  unsigned integer of size 2 bytes |   16 bits used to store numerical value. only positive values exist. range is from 0 to 2^16
---------|-------------------------------------|
     f   |  floating point of size 4 bytes      |    4 bytes used to represent signed floating point values.
---------|-------------------------------------|
     d  |  floating point of size 8 bytes      |     8 bytes are used to represent signed floating point values.
---------|-------------------------------------|


'''




class Array(list):

    def __init__(self, typ, data=None):
        self.typ = typ
        if data is None:
            super().__init__()
        else:
            data = list(data)
            for i in data:
                if type(i) != typ:
                    raise TypeError('inappropriate argument type')
            super().__init__(data)

    def append(self, item):
        if type(item) != self.typ:
            raise TypeError('inappropriate argument type')
        else:
            super().append(item)

    def insert(self, index, item):
        if type(item) != self.typ:
            raise TypeError('inappropriate argument type')
        else:
            super().insert(index, item)
