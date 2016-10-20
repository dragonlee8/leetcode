class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # write your code here
        if not s and not p:
            return True
 
        idxs = idxp = 0
        star = None
        idxss = 0
        while idxs < len(s):
            #print idxs, idxp, star, idxss, len(p), p[idxp]
            if idxp < len(p):
                if p[idxp] == s[idxs] or p[idxp] == '?':
                    idxp += 1
                    idxs += 1
                    continue
                elif p[idxp] == '*':
                    star = idxp
                    idxp += 1
                    idxss = idxs
                    continue
            
            if star is not None:
                idxp = star + 1
                idxss += 1
                idxs = idxss
            else:
                return False
            
            
        for i in range(idxp, len(p)):
            if p[i] != '*':
                return False
                
        return True
