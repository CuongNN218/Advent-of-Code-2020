import numpy as np
import fileinput
from copy import deepcopy
import sys
L = [list(map(int , l.strip())) for l in fileinput.input('tung.txt')]
# L = np.array(L)
L = np.expand_dims(np.pad(np.array(L), 1, 'constant', constant_values = 0), axis = 0)
zeros = np.zeros_like(L)
matrix = np.concatenate((zeros, L, zeros), axis = 0)
def make_border(L):
    matrix = np.pad(np.array(L), 1, 'constant', constant_values = 0)
    return matrix

for _ in range(6):
    print(matrix.shape)
    copy_matrix = np.zeros_like(matrix)
    X, Y, Z = matrix.shape
    for x in range(0,X):
        for y in range(0, Y):
            for z in range(0, Z):
                xmin = 0 if x - 1 <= 0 else x - 1
                xmax = X if x + 2 >= X else x + 2
                ymin = 0 if y - 1 <= 0 else y - 1
                ymax = Y if y + 2 >= Y else y + 2
                zmin = 0 if z - 1 <= 0 else z - 1
                zmax = Z if z + 2 >= Y else z + 2
                sub_matrix = matrix[xmin: xmax, ymin:ymax, zmin:zmax]
                if matrix[x,y,z] == 0 and np.sum(sub_matrix) == 3:
                    copy_matrix[x, y, z] = 1
                elif matrix[x,y,z] == 1 and np.sum(sub_matrix) - matrix[x,y,z] in [2, 3]:
                    copy_matrix[x, y, z] = 1
    matrix = make_border(copy_matrix)
print(np.sum(copy_matrix))
