import numpy as np

def clone_matrix(matrix):
    new_matrix = []
    for line in matrix:
        new_line = []
        for elem in line:
            new_line.append(elem)
        new_matrix.append(new_line)
    return new_matrix


def swap_lines(matrix, l1, l2):
    if(l1 != l2):
        aux = matrix[l1]
        matrix[l1] = matrix[l2]
        matrix[l2] = aux
    return matrix

def print_matrix(matrix):
        for line in matrix:
            print("|{}|".format("\t".join(list(map(lambda item: "{:7.2f}".format(item), line)))))
        print('\n\n')

def build_zero_matrix(size):
    z = []
    for i in range(size):
        z.append([0]*size)
    return z

def set_diagonal(m, n = 1):
    for i in range(len(m)):
        m[i][i] = n
    return m

def buld_intentity_matrix(size):
    i = build_zero_matrix(size)
    set_diagonal(i, 1)
    return i

def find_pivo(matrix, col):
    maior = matrix[col][col]
    index = col
    for i in range(col, len(matrix[0])):
        if(abs(matrix[i][col]) > abs(maior)):
            maior = matrix[i][col]
            index = i
    return index, maior

def lu_factor(matrix):
    u = clone_matrix(matrix)
    l = build_zero_matrix(len(matrix))
    for k in range(len(matrix) - 1):
        # pivoteamento #
        print('L:')
        print_matrix(l)
        print('U:')
        print_matrix(u)
        index, maior = find_pivo(u, k)
        print("Swap line {} with line {}".format(k, index))
        u = swap_lines(matrix, k, index)
        l = swap_lines(l, k, index)
        ##
        for j in range(k + 1, len(matrix)):
            l[j][k] = u[j][k]/u[k][k]
            for i in range(k, len(matrix)):
                u[j][i] = u[j][i] - l[j][k]*u[k][i]
    set_diagonal(l)
    return l, u

if __name__ == "__main__":

    m = [
            [ 1,    0,    0,   0,    1],
            [-1,    1,    0,   0,    1],
            [-1,   -1,    1,   0,    1],
            [-1,   -1,   -1,   1,    1],
            [-1,   -1,   -1,  -1,    1]
        ]

    m = [
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



    l, u = lu_factor(m)

    print("L:")
    print_matrix(l)
    print('\n\nU:')
    print_matrix(u)
    print('\n\nmult:')
    print_matrix(np.dot(l, u))