import numpy as np
import fileinput
from copy import deepcopy
import sys
import time 
start = time.time()
L = [list(map(int , l.strip())) for l in fileinput.input('tung.txt')]
L = np.array(L)
L = np.expand_dims(L, axis = [0,1])
# print('1', L.shape)
matrix = np.pad(np.array(L), 1, 'constant', constant_values = 0)
# print('2', matrix.shape)
def make_border(L):
    matrix = np.pad(L, 1, 'constant', constant_values = 0)
    return matrix

for _ in range(6):
    copy_matrix = np.zeros_like(matrix)
    X, Y, Z, W = matrix.shape
    for x in range(0,X):
        for y in range(0, Y):
            for z in range(0, Z):
                for w in range(0, W):
                    xmin = 0 if x - 1 <= 0 else x - 1
                    xmax = X if x + 2 >= X else x + 2
                    ymin = 0 if y - 1 <= 0 else y - 1
                    ymax = Y if y + 2 >= Y else y + 2
                    zmin = 0 if z - 1 <= 0 else z - 1
                    zmax = Z if z + 2 >= Z else z + 2
                    wmin = 0 if w - 1 <= 0 else w - 1
                    wmax = W if w + 2 >= W else w + 2
                    sub_matrix = matrix[xmin: xmax, ymin:ymax, zmin:zmax, wmin:wmax]
                    if matrix[x,y,z,w] == 0 and np.sum(sub_matrix) == 3:
                        copy_matrix[x, y, z, w] = 1
                    elif matrix[x,y,z,w] == 1 and np.sum(sub_matrix) - matrix[x,y,z,w] in [2, 3]:
                        copy_matrix[x, y, z, w] = 1
    # print(copy_matrix)
    matrix = make_border(copy_matrix)
    # print(matrix.shape)
print(np.sum(copy_matrix))
print(time.time() - start)