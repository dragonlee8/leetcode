class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = {}
        cnt = 0            
        for i in nums:
            if i in s:
                s[i] += 1
                if k == 0 and s[i] == 2:
                    cnt += 1      
                continue
            if (i-k) in s:
                cnt += 1;
            if (i+k) in s:
                cnt += 1
            s[i] = 1
        
        return cnt
    
