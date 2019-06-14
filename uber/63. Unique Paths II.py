class Solution(object):
    def helper(self, grid, x, y, m, n):
        count = 0
        if self.dp[y][x] != -1:
            return self.dp[y][x]
        for a, b in self.dirs:
            xi = x+a
            yi = y+b
            if xi >=0 and yi >=0 and xi < m and yi < n and grid[yi][xi]!= 1:
                count += self.helper(grid, xi, yi, m, n)
        
        self.dp[y][x] = count
        return count
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        n = len(obstacleGrid)
        if n == 0:
            return 0
        m = len(obstacleGrid[0])
        if obstacleGrid[n-1][m-1] or obstacleGrid[0][0] == 1:
            return 0
        
        self.dp = [[-1] * m for x in range(n)]
        self.dp[n-1][m-1] = 1
        self.dirs = [[1, 0], [0, 1]]
        return self.helper(obstacleGrid, 0, 0, m, n)
                
