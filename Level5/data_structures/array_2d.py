# 2D Array - array made up of arrays
# to access elements: array[row][column]



import random


class Array(list):

    def __init__(self, data, dtype=int):
        self.dtype = dtype
        data = list(data)
        for i in data:
            if not isinstance(i, self.dtype):
                raise TypeError('inappropriate argument type')
        super().__init__(data)
            
    def append(self, item):
        if not isinstance(item, self.dtype):
            raise TypeError('inappropriate argument type')
        else:
            super().append(item)

    def insert(self, index, item):
        if not isinstance(item, self.dtype):
            raise TypeError('inappropriate argument type')
        else:
            super().insert(index, item)


def breakup(l, dtype):
    try:
        l = Array(dtype=dtype, data=l)
    except TypeError as error:
        l = Array(dtype=Array, data=[breakup(l[n], dtype) for n in range(len(l))])
    return l


# creation
arr = [[random.randint(-10, 10) for _ in range(5)] for _ in range(3)]
print(type(arr))
arr = breakup(arr, int)
print(type(arr))


# display
for row in arr:
    for col in row:
        print(col, end=' ')
    print()


# update
arr[0] = Array([1, 2, 3, 4, 5])
arr[0][4] = 32
print(arr)

# insertion
arr.insert(1, Array([6, 7, 8, 9]))
arr[0].insert(0, 0)
print(arr)

# deletion
arr.pop(1)
arr[0].pop(4)
print(arr)
