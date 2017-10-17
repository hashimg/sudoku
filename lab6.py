################# Warm-up #################

###### Part 1

def matrix(n, init):
    my_matrix = []
    while len(my_matrix) != n:
        my_matrix.append([init])
        for i in range(len(my_matrix)):
            while len(my_matrix[i]) != n:
                my_matrix[i].append(init)

    return my_matrix

print(matrix(5,6))
print(matrix(2,4))




######## Part 2

sq_matrix = matrix(3,6)
sq_matrixV2 = matrix(2,8)


def order(matrix):
    print('This is a', len(matrix),'x', len(matrix), 'matrix')


print(order(sq_matrix))
print(order(sq_matrixV2))



############# Stretch

def identity(n):
    id_matrix = matrix(n, 0)

    index = 0
    for row in id_matrix:
        row.pop(index)
        row.insert(index, 1)
        index += 1
    return id_matrix

print(identity(4))
print(identity(6))





############## Populate

def populate(m, n, value):
    my_matrix = matrix(m, 0)

    values_inserted = 0
    index = random.randint(0, len(my_matrix))
    while values_inserted != n:
        for row in copy_matrix:
            row.pop(index)
            row.insert(index, value)
            index = random.randint(0, len(my_matrix))
            values_inserted += 1
    return my_matrix











####################### Workout ############################

import turtle



