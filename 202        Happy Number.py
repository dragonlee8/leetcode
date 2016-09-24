class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        from sets import Set
        nums = Set()

        while n not in nums:
            if n == 1:
                return True
            nums.add(n)
            s = str(n)
            n = 0
            for i in s:
                n += int(i) * int(i)
         
        
        return False
