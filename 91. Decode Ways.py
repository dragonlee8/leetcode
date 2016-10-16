class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
            
        n = len(s)
        dp = [0] * 2
        dp[1] = 1
        
        for i in range(n):
            a1 = dp[i%2]
            a2 = dp[(i+1)%2]
            count = 0
            if int(s[i]) != 0:
                count += a2
            if i > 0 and (s[i-1] == '1' or (s[i-1] == '2' and s[i] in {'0', '1', '2', '3', '4', '5', '6'})):
                count += a1
            
            dp[i%2] = count
        
        
        return dp[(n-1)%2]
