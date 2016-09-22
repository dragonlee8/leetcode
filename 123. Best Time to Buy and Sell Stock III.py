class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        
        left = [0] * n
        right = [0] * n
        
        minN = sys.maxint
        
        for i in range(n):
            if prices[i] < minN:
                minN = prices[i]
            
            if i >= 1:
                left[i] = max(left[i-1], prices[i] - minN)
                
        maxN = -1 * sys.maxint
        for i in range(n-1, -1, -1):
            if prices[i] > maxN:
                maxN = prices[i]
             
            if i != n-1:   
                right[i] = max(right[i+1], maxN - prices[i])
        
        ret = 0
        
        for i in range(n):
            ret = max(ret, left[i] + right[i])
            
        return ret
