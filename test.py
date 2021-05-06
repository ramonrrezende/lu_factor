from band_matrix import BandMatrix


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
m.print()
print(m.get(3, 4))#49
print(m.get(1, 1))#20
print(m.get(3, 4))#29