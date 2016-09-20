class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates:
            return []
        
        from sets import Set
        candidates = sorted(list(Set(candidates)))

        result = []

        def helper(cands, t, tmp):
            if t == 0:
                result.append(tmp)
                return

            if not cands:
                return

            n = cands[0]
            if n > t:
                return

            helper(cands, t - n, tmp + [n])
            helper(cands[1:], t, tmp)

        helper(candidates, target, [])
        return result
