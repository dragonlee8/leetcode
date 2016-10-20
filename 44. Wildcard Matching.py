class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # write your code here
        if not s and not p:
            return True
 
        idxs = idxp = 0
        star = None
        idxss = 0
        while idxs < len(s):
            #print idxs, idxp, star, idxss, len(p), p[idxp]
            if idxp < len(p):
                if p[idxp] == s[idxs] or p[idxp] == '?':
                    idxp += 1
                    idxs += 1
                    continue
                elif p[idxp] == '*':
                    star = idxp
                    idxp += 1
                    idxss = idxs
                    continue
            
            if star is not None:
                idxp = star + 1
                idxss += 1
                idxs = idxss
            else:
                return False
            
            
        for i in range(idxp, len(p)):
            if p[i] != '*':
                return False
                
        return True

    
    
    class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        if not s and not p:
            return False
        
        n = len(s)
        m = len(p)
        
        dp = [[False for x in range(m+1)] for x in range(n+1)]
        
        dp[0][0] = True
        if n == 0 and p.count('*') == m:
            return True
    
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1]
                else:
                    if s[i-1] == p[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    
        return dp[n][m]
            
