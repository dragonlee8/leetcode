class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        # write your code here
        n = len(A)
            
        minSum = [0, -1]
        ret = None
        maxInterval = None
        accSum = 0
        for i in range(0, n):
            accSum += A[i]
            if not ret or maxInterval < accSum - minSum[0]:
                ret = [minSum[1] + 1, i]
                maxInterval = accSum - minSum[0]

            if accSum < minSum[0]:
                minSum = [accSum, i]
                
            
        return ret
