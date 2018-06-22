class Solution(object):
    dp = None
    directions = [[0, 1], [1, 0]]
    def allPaths(self, startX, startY, m, n, obstacleGrid):
        count = 0
        if startX >= m or startX < 0 or startY >=n or startY < 0 or obstacleGrid[startY][startX] != 0:
            return count
        if startX == m-1 and startY == n-1:
            return 1
        
        if self.dp[startY][startX] != -1:
            return self.dp[startY][startX]
        
        for d in self.directions:
            count += self.allPaths(startX+d[0], startY+d[1], m, n, obstacleGrid)
        
        self.dp[startY][startX] = count
        return count
        
        
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        n = len(obstacleGrid)
        if not obstacleGrid[0]:
            return 0
        m = len(obstacleGrid[0])
        
        self.dp = [[-1 for x in range(m)] for x in range(n)]
        
        return self.allPaths(0, 0, m, n, obstacleGrid)
