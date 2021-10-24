# SET EXERCISES

# set - collection of items. order does not matter
# no duplicates
# immutable in set, mutable in a whole set
# no indices

# Operations
#   1. union - combines all distinct elements in two sets
#   2. intersection - selects only elements prenset in both sets
#   3. difference - selects only elements unique to the first set
#   4. complement


# Built-in Implementation

# creation
lang1 = set(['Python', 'java', 'c'])
lang2 = {'HTML', 'JS', 'CSS', 'Python'}


# display
for l in lang1:
    print(l)

# adding elements
lang1.add('c++')
print(lang1)


# removing elements
lang1.discard('c++')
print(lang1)


# union
new_set = lang1 | lang2
print(new_set)


# intersection
new_set = lang1 & lang2
print(new_set)


# difference
new_set = lang1 - lang2
print(new_set)


# compare - checks if two sets are supersets or subsets of each other
lang3 = {'Python', 'java', 'c', 'rust'}
print(lang3 > lang1)
print(lang1 < lang3)


print()


# Class Implementation


class Set():

    def __init__(self, elements):
        self.__elements = list(elements)
        for e in self.__elements:
            while self.__elements.count(e) > 1:
                self.__elements.remove(e)

    def add(self, val):
        if val not in self.__elements:
            self.__elements.append(val)

    def discard(self, val):
        if val in self.__elements:
            self.__elements.remove(val)

    def count(self):
        return len(self.__elements)

    def __or__(self, other):
        output = Set(self.__elements.copy() + other.get_list())
        return output

    def get_list(self):
        return self.__elements.copy()

    def __str__(self):
        strs = [str(e) for e in self.__elements]
        return '{' + ', '.join(strs) + '}'

    def __contains__(self, key):
        return key in self.__elements

    def __and__(self, other):
        output = []
        set1 = self.get_list()
        set2 = other.get_list()
        for e in set1:
            if e in set2:
                output.append(e)
        return Set(output)

    def __sub__(self, other):
        output = []
        set1 = self.get_list()
        set2 = other.get_list()
        for e in set1:
            if e not in set2:
                output.append(e)
        return Set(output)

    def __eq__(self, other):
        if self.count() == other.count():
            set1 = self.get_list()
            set2 = other.get_list()
            for e in set1:
                if e not in set2:
                    return False
            return True
        return False
    
    def __ne__(self, other):
        union = self | other
        return self == union and other == union

    def __gt__(self, other):
        union = self | other
        intersection = self & other
        return self == union and other == intersection

    def __lt__(self, other):
        union = self | other
        intersection = self & other
        return self == intersection and other == union

    def __ge__(self, other):
        return self == other or self > other

    def __le__(self, other):
        return self == other or self < other


# creation
lang1 = Set(['Python', 'java', 'c'])
lang2 = Set(['HTML', 'JS', 'CSS', 'Python'])


# display
print(lang1)

# adding elements
lang1.add('c++')
print(lang1)


# removing elements
lang1.discard('c++')
print(lang1)


# union
new_set = lang1 | lang2
print(new_set)


# intersection
new_set = lang1 & lang2
print(new_set)


# difference
new_set = lang1 - lang2
print(new_set)


# compare - checks if two sets are supersets or subsets of each other
lang3 = Set(['Python', 'java', 'c', 'rust'])
print(lang3 > lang1)
print(lang1 < lang3)



