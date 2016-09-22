class Solution(object):
    def search(self, nums, s, index):
        if index == len(nums):
            self.result.append(s)
            return
        
        self.search(nums, s, index + 1)
        self.search(nums, s + [nums[index]], index + 1)
        
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if not nums:
            return []
        
        self.result = []
        self.search(sorted(nums), [], 0)
        return self.result
