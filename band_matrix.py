

class BandMatrix:

    def __init__(self, dimension_x, dimension_y, lower_bandwidth, superior_bandwidth, matrix=None):
        self.dimension_x = dimension_x
        self.dimension_y = dimension_y
        self.lower_bandwidth = lower_bandwidth
        self.superior_bandwidth = superior_bandwidth
        self.width = lower_bandwidth + superior_bandwidth + 1
        if not matrix:
            self._matrix = [[0]*self.width for i in range(self.dimension_y)]
        else:
            self._matrix = matrix

    def print(self):
        for line in self._matrix:
            print("|{}|".format("\t".join(list(map(lambda item: "{:6.2f}".format(item), line)))))
    
    def print_complete_matrix(self):
        for i in range(0, self.dimension_x):
            line = self.get_line(i)
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
        if(self.lower_bandwidth + j - i) < 0 or (self.lower_bandwidth + j - i) >= len(self._matrix[0]) or i >= len(self._matrix):
            return
        self._matrix[i][self.lower_bandwidth + j - i] = new_val
    
    def get_line(self, n, aux=None):
        if aux is None:
            aux = self.dimension_y-1
            self.get_line(n, aux)
        
        if aux == -1:
            return []
        
        return self.get_line(n, aux-1) + [self.get(n, aux)]

    def get_col(self, n, aux=None):
        if aux is None:
            aux = self.dimension_y-1
            self.get_col(n, aux)
        
        if aux == -1:
            return []
        
        return self.get_col(n, aux-1) + [self.get(aux, n)]

    def swap_lines(self, l1, l2):
        temp = []
        for i in range(0, self.dimension_y):
            temp.append(self.get(l1, i))
        
        for i in range(0, self.dimension_y):
            self.set(l1, i, self.get(l2, i))
        
        for i in range(0, self.dimension_y):
            self.set(l2, i, temp[i])

