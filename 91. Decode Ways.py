class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        from sets import Set
        allowlist = Set();
        
        for i in range(1, 27):
            allowlist.add(str(i));
        n = len(s)
        dp = [0] * 2
        
        for i in range(n):
            a1 = dp[i%2]
            a2 = dp[(i+1)%2]
            if i > 0 and s[i-1:i+1] in allowlist:
                a2 += a2
            
            if s[i] in allowlist:
                a2 += a1
        
        return dp[(i+1)%2]
