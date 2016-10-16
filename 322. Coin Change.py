import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or amount == 0:
            return 0
        
        n = len(coins)
        dp = [-1] * (amount+1)
        dp[0] = 0
        
        for i in range(amount+1):
            if dp[i] == -1:
                continue
            for coin in coins:
                if i + coin <= amount:
                    if dp[i+coin] == -1:
                        dp[i+coin] = dp[i] + 1
                    else:
                        dp[i+coin] = min(dp[i+coin], dp[i]+1)
                    
        return dp[-1]
                    
