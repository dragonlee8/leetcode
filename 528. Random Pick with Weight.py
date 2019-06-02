class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.sum = 0
        self.weights = [0]
        for weight in w:
            self.sum += weight
            self.weights.append(self.sum)
            
        

    def pickIndex(self):
        """
        :rtype: int
        """
        if not self.weights:
            return None
        toss = random.randint(1, self.sum)
        idx = bisect.bisect_left(self.weights, toss)
        return idx -1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
