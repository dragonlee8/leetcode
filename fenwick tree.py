class FenwickTree(object):
    def __init__(self, n):
        self.n = n 
        self.sum = [0]* (n + 1)
    
    def lowbit(self, x):
        return -x&x
    
    def add(self, x, val):
        while x <= self.n:
            self.sum[x] += val
            x += self.lowbit(x)
    
    def sums(self, x):
        ret = 0
        while x > 0:
            ret += self.sum[x]
            x -= self.lowbit(x)
        
        return ret
        
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.idxes = {}
        self.nums = nums
        self.tree = FenwickTree(len(nums))
        
        for i in range(len(nums)):
            self.tree.add(i + 1, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.tree.add(i+1, val - self.nums[i])
        self.nums[i] = val
        
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.tree.sums(j+1) - self.tree.sums(i)
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
