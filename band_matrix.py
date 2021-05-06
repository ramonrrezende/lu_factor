

class BandMatrix:

    def __init__(self, dimension_x, dimension_y, lower_bandwidth, superior_bandwidth):
        self.dimension_x = dimension_x
        self.dimension_y = dimension_y
        self.lower_bandwidth = lower_bandwidth
        self.superior_bandwidth = superior_bandwidth
        self.width = lower_bandwidth + superior_bandwidth + 1
        self._matrix = [[0]*self.width for i in range(self.dimension_y)]

    def print(self):
        for line in self._matrix:
            print("|{}|".format("\t".join(list(map(lambda item: "{:6.2f}".format(item), line)))))

    def convert(self, normal_matrix):
        for i in range(len(normal_matrix)):
            if (self.width - self.lower_bandwidth + i <= len(normal_matrix[i])):
                sup_lim = self.width - self.lower_bandwidth + i
            else:
                sup_lim = len(normal_matrix[i])
            for j in range(i - self.lower_bandwidth, sup_lim):
                if j < 0:
                    self._matrix[i][self.lower_bandwidth + j - i] = 0
                else:
                    self._matrix[i][self.lower_bandwidth + j - i] = normal_matrix[i][j]

    def _valid_position(self, i, j):
        if(i < 0 or i >= self.dimension_x or j < 0 or j >= self.dimension_y):
            return False
        return True

    def get(self, i, j):
        if not self._valid_position(i, j):
            return False
        if(self.lower_bandwidth + j - i) < 0 or (self.lower_bandwidth + j - i) >= len(self._matrix[0]) or i >= len(self._matrix):
            return 0
        return self._matrix[i][self.lower_bandwidth + j - i]

    def set(self, i, j, new_val):
        print(i, j)
        if not self._valid_position(i, j):
            raise ValueError('Position ({}, {}) is not a valid position'.format(i, j))
        if(self.lower_bandwidth + j - i) < 0 or (self.lower_bandwidth + j - i) >= len(self._matrix[0]) or i >= len(self._matrix):
            if new_val != 0:
                raise ValueError()
        else:
            self._matrix[i][self.lower_bandwidth + j - i] = new_val

    def swap_lines(self, l1, l2):
        if(l1 != l2 and l1 < len(self._matrix) and l1 >=0 and l2 < len(self._matrix) and l2 >=0):
            aux = self._matrix[l1]
            self._matrix[l1] = self._matrix[l2]
            self._matrix[l2] = aux

    def to_normal(self):
        m = []
        for i in range(self.dimension_x):
            m.append([0]*self.dimension_x)
        for i in range(self.dimension_x):
            for j in range(self.dimension_y):
                m[i][j] = self.get(i, j)
        return m