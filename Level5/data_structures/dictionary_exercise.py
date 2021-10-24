# DICTIONARIES
# dictionary- a data structure in which keys define/hold reference to certain values
# values must be accessed from keys

class Dictionary:

    def __init__(self):
        self.__keys = []
        self.__vals = []

    def items(self):
        return [(self.__keys[n], self.__vals[n]) for n in range(len(self.__keys))]

    def keys(self):
        return self.__keys.copy()

    def values(self):
        return self.__vals.copy()

    def clear(self):
        self.__keys = []
        self.__vals = []

    def pop(self, key):
        i = self.__keys.index(key)
        self.__keys.pop(i)
        self.__vals.pop(i)
        
    def __getitem__(self, key):
        if key not in self.__keys:
            raise KeyError('key not found')
        else:
            i = self.__keys.index(key)
            return self.__vals[i]

    def __setitem__(self, key, value):
        if key in self.__keys:
            i = self.__keys.index(key)
            self.__vals[i] = value
        else:
            self.__keys.append(key)
            self.__vals.append(value)

    def __delitem__(self, key, value):
        if key not in self.__keys:
            raise KeyError('key not found')
        else:
            self.__keys.remove(key)
            self.__vals.remove(value)

    def __str__(self):
        return '{' + ', '.join([str(self.__keys[n]) + ': ' + str(self.__vals[n]) for n in range(len(self.__keys))]) + '}'

    def __len__(self):
        return len(self.__keys)

    def __dict__(self):
        return {key: val for key, val in self.items()}


d = Dictionary()
d[0] = 'a'
d[1] = 'b'
d[2] = 'c'
d[0] = 'abc'
print(d)





