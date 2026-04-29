#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]



print("Matrix: {}".format(matrix))
new_m = [list(map(lambda x: x * 2, row) for row in matrix)]
print(new_m)
#    print(list(map(lamba x: x*2, matrix)))
#    return list(map(lambda x: x**2, matrix))