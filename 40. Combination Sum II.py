class Solution(object):
    result = []
    def helper(self, candidates, target, tmp):
        if target == 0:
            self.result.append(tmp)
            
        if not candidates:
            return 
        elif candidates[0] > target:
            return
        
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            self.helper(candidates[i+1:], target - candidates[i], tmp + [candidates[i]])
            
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
            
        self.result = []
            
        candidates.sort()
        tmp = []
        self.helper(candidates, target, tmp)
        
        return self.result
