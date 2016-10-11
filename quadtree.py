class Node(object):
    val = 0

    def __init__(self, x0, x1, y0, y1, matrix):
        if not matrix:
            return
        n = len(matrix)
        m = len(matrix[0])

        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1

        if x0 == x1 and y0 == y1:
            self.val = matrix[y0][x0]
            return

        midx = x0 + (x1-x0)/2
        midy = y0 + (y1-y0)/2

        self.d0 = self.d1 = self.d2 = self.d3 = None
        if x0 < x1 and y0 < y1:
            self.d0 = Node(x0, midx, y0, midy, matrix)
            self.d1 = Node(midx+1, x1, y0, midy, matrix)
            self.d2 = Node(x0, midx, midy+1, y1, matrix)
            self.d3 = Node(midx+1, x1, midy+1, y1, matrix)
        elif x0<x1 and y0 == y1:
            self.d0 = Node(x0, midx, y0, y1, matrix)
            self.d1 = Node(midx+1, x1, y0, y1, matrix)
        else:
            self.d0 = Node(x0, x1, y0, midy, matrix)
            self.d2 = Node(x0, x1, midy+1, y1, matrix)


    def getSum(self, x0, y0, x1, y1):
        print x0, y0, x1, y1
        ret = 0

        if x0 < self.x0 or x1 > self.x1 or y0 < self.y0 or y1 > self.y1:
            return 0

        if x0 == x1 == self.x0 == self.x1 and y0 == y1 == self.y0 == self.y1:
            return self.val

        midx = self.x0 + (self.x1-self.x0)/2
        midy = self.y0 + (self.y1-self.y0)/2
        print self.x0, self.y0, self.x1, self.y1, midx, midy
        if self.d0 and x0 <= midx and y0 <= midy:
            ret += self.d0.getSum(x0, y0, min(x1, midx), min(y1, midy))
        if self.d1 and x1 > midx and y0 <= midy:
            ret += self.d1.getSum(max(midx+1, x0), y0, x1, min(y1, midy))
        if self.d2 and x0 <= midx and y1 > midy :
            ret += self.d2.getSum(x0, max(midy+1, y0), min(x1, midx), y1)
        if self.d3 and x1 > midx and y1 > midy:
            ret += self.d3.getSum(max(x0, midx+1), max(y0, midy+1), x1, y1)

        return ret

    def update(self, x, y, val):
        if x < self.x0 or x > self.x1 or y < self.y0 or y > self.y1:
            return 0

        if self.x0 == self.x1 and self.y0 == self.y1:
            self.val += val
            return self.val

        midx = self.x0 + (self.x1-self.x0)/2
        midy = self.y0 + (self.y1-self.y0)/2

        self.val += val
        if x <= midx and y <= midy:
            self.d0.update(x, y, val)
        elif x > midx and y <= midy:
            self.d1.update(x, y, val)
        elif x <= midx and y > midy:
            self.d2.update(x, y, val)
        else:
            self.d3.update(x, y, val)



class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.Node = None
            return

        n = len(matrix) - 1
        m = len(matrix[0]) - 1
        self.root = Node(0, m, 0, n, matrix)


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.root.getSum(col1, row1, col2, row2)

