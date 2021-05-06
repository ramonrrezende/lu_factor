import numpy as np
from copy import deepcopy
from band_matrix import BandMatrix

def mult(m1: BandMatrix, m2: BandMatrix):
    matRes = []
    
    for i in range(0, m1.dimension_x):           
        matRes.append([])

        for j in range(0, m2.dimension_y):
            # multiplica cada linha de mat1 por cada coluna de mat2;
            listMult = [x*y for x, y in zip(m1.get_line(i), m2.get_col(j))]

            # e em seguida adiciona a matRes a soma das multiplicações
            matRes[i].append(sum(listMult))
    
    return matRes

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
        """index, maior = find_pivo(u, k)
        print("Swap line {} with line {}".format(k, index))
        u.swap_lines(k, index)
        l.swap_lines(k, index)"""
        ##
        for j in range(k + 1, matrix.dimension_x):
            l.set(j, k, u.get(j, k)/u.get(k, k))
            for i in range(k, matrix.dimension_x):
                u.set(j, i, u.get(j, i) - l.get(j, k)*u.get(k, i))
    set_diagonal(l)
    return l, u


def solvingl(l, b):
    n = l.dimension_x
    for i in np.arange(n):
        pivo = b[i]

        for j in np.arange(n):
            if(j > i):
                b[j] = b[j] + round((l.get(j,i)*-1),2) * pivo # Multiplica l *multiplicadores* com o pivo e soma com b

    return(np.copy(b))

def solvingu(A, b):
    n = A.dimension_x
    x = np.zeros(n)
    x[n-1] = b[n-1]/A.get(n-1, n-1)

    for k in range(n-1, -1, -1): # linha
        soma = 0
        for j in range(0,n): # coluna
            soma = soma + A.get(k,j) * x[j]
        x[k]=(b[k] - soma)/A.get(k,k)
    
    return(x)

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

    b = [28, 79,  314, 273, 240, 390, 339, 330, 331, 204, 231, 212]

    m = BandMatrix(12, 12, 2, 3)
    m.convert(normal_matrix)

    l, u = lu_factor(m)

    print("l (banda):")
    l.print() # printa  a matriz de banda
    print('\n\nu (banda):')
    u.print() # printa  a matriz de banda


    print("\n\nl (completo):")
    l.print_complete_matrix() # printa  a matriz completa
    print('\n\nu (completo):')
    u.print_complete_matrix() # printa  a matriz completa

    print_matrix(mult(l, u))

    # i) ly = b
    y = solvingl(l, b)
    # ii) ux = y
    x = solvingu(u,y)

    print("\n\nResolvendo ly = b..")
    print("y: ")
    print(list(y))
    print("\n\nResolvendo ux = y..")
    print("x: ")
    print(list(x))