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
        dp = [sys.maxint] * (amount+1)

        for i in range(amount+1):
            for j in range(i):
                if i-j in coins:
                    dp[i] = min(dp[i], dp[j+1])
                
                
        return dp[-1]
                
