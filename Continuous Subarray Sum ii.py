class Solution:
    def __init__(self):
        pass

    def findInterval(self, A):
        n = len(A)
        if n == 0:
            return [None, None, None]

        # find the non-rotate value
        minSum = [0, -1]
        largestInterval = None
        largestSum = 0
        accSum = 0
        for i in range(n):
            accSum += A[i]
            localMax = accSum - minSum[0]
            if i == 0 or localMax > largestSum:
                largestSum = localMax
                largestInterval = [minSum[1] + 1, i]

            if accSum < minSum[0]:
                minSum = [accSum, i]

        return [largestInterval, largestSum, accSum]

    def run(self, A):
        if len(A) == 1:
            return [0, 0]

        largestInterval, largestSum, accSum = self.findInterval(A)
        smallestInterval, smallestSum, _ = self.findInterval(map(
            lambda x: -1 * x, A[1: -1]
        ))

        if not smallestInterval or largestSum > accSum + smallestSum:
            return largestInterval
        else:
            return [smallestInterval[1] + 2, smallestInterval[0]]
