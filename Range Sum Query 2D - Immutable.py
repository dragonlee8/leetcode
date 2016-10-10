class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.matrix = []
            return 
            
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    matrix[i][j] += matrix[i][j-1]
                elif j == 0:
                    matrix[i][j] += matrix[i-1][j]
                else:
                    matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]

        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.matrix:
            return 0
        
        if row1 > 0 and col1 > 0:
            return self.matrix[row2][col2] + self.matrix[row1-1][col1-1] - self.matrix[row1-1][col2] - self.matrix[row2][col1-1]
        elif row1 == 0 and col1 > 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1-1]
        elif row1 > 0 and col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2]
        else:
            return self.matrix[row2][col2]
        




        # Your NumMatrix object will be instantiated and called as such:
        # numMatrix = NumMatrix(matrix)
        # numMatrix.sumRegion(0, 1, 2, 3)
        # numMatrix.sumRegion(1, 2, 3, 4)
