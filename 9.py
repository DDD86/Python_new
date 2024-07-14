# import numpy as np

# def matrix_transp(matrix):
#     new_matrix = np.array(matrix)
#     return new_matrix.T


# matrix = [[1, 2, 3], [5, 6, 7]]
# print(matrix_transp(matrix))


def matrix_transp(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) 

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

matrix = [[1, 2, 3], [5, 6, 7]]
transposed_matrix = matrix_transp(matrix)
for row in transposed_matrix:
    print(row)
