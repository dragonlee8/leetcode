class Solution(object):
    def isValid(self, i, j, m, n):
        return i >= 0 and j >= 0 and i < n and j < m

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return None

        n = len(board)
        m = len(board[0])

        moves = [[-1, -1], [0, -1], [1, -1],[-1, 0],[1, 0],[1, 1],[-1, 1],[0, 1]]
        for i in range(n):
            for j in range(m):
                
                lives = 0
                dies = 0
                for move in moves:
                    if self.isValid(move[0]+i, move[1]+j, m, n):
                        if board[move[0]+i][move[1]+j] & 1:
                            lives += 1
                        else:
                            dies += 1
                            

                if board[i][j] & 1 and lives >= 2 and lives <= 3:
                    board[i][j] += 2
                elif board[i][j] & 1 == 0 and lives == 3:
                    board[i][j] += 2
                    
        for i in range(n):
            for j in range(m):
                if board[i][j] & 2:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
                    
        

