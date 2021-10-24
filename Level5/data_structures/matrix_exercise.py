import numpy

# creation
matrix = numpy.array([
    ['First', 1, 2, 3],
    ['Second', 4, 5, 6],
    ['Third', 7, 8, 9]
         ])
print(matrix)


# access
print(matrix[0])
print(matrix[1][0])


# add row
new_matrix = numpy.append(matrix, [['Fourth', 10, 11, 12]], 0)
print(new_matrix)


# add col
new_matrix = numpy.append(matrix, [[4], [7], [10]], 1)
print(new_matrix)


# delete col
new_matrix = numpy.delete(matrix, [2], 1)
print(new_matrix)


# delete row
new_matrix = numpy.delete(matrix, [1], 0)
print(new_matrix)


# update
matrix[0] = ['Zeroth', 0, 1, 2]
print(matrix)


