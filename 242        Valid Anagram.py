class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        worddict = {}
        
        for x in s:
            if x in worddict:
                worddict[x] += 1
            else:
                worddict[x] = 1
            
        for x in t:
            if x not in worddict:
                return False
            
            worddict[x] -= 1
            if worddict[x] == 0:
                del worddict[x]
                
        return not any(worddict)
