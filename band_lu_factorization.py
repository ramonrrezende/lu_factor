import numpy as np
from copy import deepcopy
from band_matrix import BandMatrix

def print_matrix(matrix):
        for line in matrix:
            print("|{}|".format("\t".join(list(map(lambda item: "{:7.2f}".format(item), line)))))
        print('\n\n')

def set_diagonal(m, n = 1):
    for i in range(m.dimension_x):
        m.set(i, i, n)

def find_pivo(matrix, col):
    maior = matrix.get(col, col)
    index = col
    for i in range(col, matrix.dimension_x):
        if(abs(matrix.get(i, col)) > abs(maior)):
            maior = matrix.get(i, col)
            index = i
    return index, maior

def lu_factor(matrix):
    u = deepcopy(matrix)
    l = BandMatrix(12, 12, matrix.lower_bandwidth, 0)
    for k in range(matrix.dimension_x - 1):
        # pivoteamento #
        """ print('L:')
        print_matrix(l._matrix)
        print('U:')
        print_matrix(u._matrix)
        index, maior = find_pivo(u, k)
        print("Swap line {} with line {}".format(k, index))
        u.swap_lines(k, index)
        l.swap_lines(k, index)
        print('L:')
        print_matrix(l._matrix)
        print('U:')
        print_matrix(u._matrix) """
        ##
        print(f"Pivo - {u.get(k, k)}")
        for j in range(k + 1, matrix.dimension_x):
            l.set(j, k, u.get(j, k)/u.get(k, k))
            for i in range(k, matrix.dimension_x):
                u.set(j, i, u.get(j, i) - l.get(j, k)*u.get(k, i))
        print('L:')
        print_matrix(l._matrix)
        print('U:')
        print_matrix(u._matrix)
    set_diagonal(l)
    return l, u

if __name__ == "__main__":

    normal_matrix = [
        [ 1,    0,    0,   0,    1],
        [-1,    1,    0,   0,    1],
        [-1,   -1,    1,   0,    1],
        [-1,   -1,   -1,   1,    1],
        [-1,   -1,   -1,  -1,    1]
    ]

    normal_matrix = [
        [ 10,   5,   6,   7,   0,   0,   0,   0,   0,   0,   0,  0],
        [ 20,  20,  21,  14,   4,   0,   0,   0,   0,   0,   0,  0],
        [ 90,  65,  82,  64,  10,   3,   0,   0,   0,   0,   0,  0],
        [  0,  90, 101,  12,  49,  14,   7,   0,   0,   0,   0,  0],
        [  0,   0,  90,  29,  46,  48,  20,   7,   0,   0,   0,  0],
        [  0,   0,   0,  90, 101,  92,  83,  20,   4,   0,   0,  0],
        [  0,   0,   0,   0,  90,  65,  80,  84,  15,   5,   0,  0],
        [  0,   0,   0,   0,   0,  90,  92,  82,  53,  11,   2,  0],
        [  0,   0,   0,   0,   0,   0,  90, 101,  79,  47,   5,  9],
        [  0,   0,   0,   0,   0,   0,   0,  90,  47,  19,  28, 20],
        [  0,   0,   0,   0,   0,   0,   0,   0,  90,  20,  35, 86],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,  90,  92, 30]
    ]

    m = BandMatrix(12, 12, 2, 3)
    m.convert(normal_matrix)

    l, u = lu_factor(m)

    print("L:")
    print_matrix(l._matrix)
    print('\n\nU:')
    print_matrix(u._matrix)