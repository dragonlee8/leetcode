from __builtin__ import False
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if not p:
            return False
        
        pattern = ""
        signMap = {}
        for i in range(len(p)):
            if p[i] != '*':
                pattern += p[i]
            else:
                signMap[len(pattern)-1] = '*'
            
        
        n = len(s)
        m = len(pattern)
        
        dp = [[False for x in range(m+1)] for x in range(n+1)]
        dp[0][0] = True
        
        for i in range(m):
            if dp[0][i] == False:
                break
            if i in signMap:
                dp[0][i+1] = True
                
            
        for i in range(n):
            for j in range(m):
                #print i, j, signMap, dp
                if dp[i][j+1] and j in signMap and (pattern[j] == s[i] or (pattern[j] == '.')):
                    dp[i+1][j+1] = True 
                elif dp[i][j] and (pattern[j] == s[i] or pattern[j] == '.'):
                    dp[i+1][j+1] = True
                elif dp[i+1][j] and j in signMap:
                    dp[i+1][j+1] = True
                    
                    
        return dp[-1][-1]
                
