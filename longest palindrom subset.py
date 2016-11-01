class Solution(object):
    def __init__(self):
        self.prevLookup = {}
        self.nextLookup = {}
        self.ret = []
    
    def initLookup(self, s):
        for c in s:
            if c not in self.prevLookup:
                self.prevLookup[c] = [0] * len(s)
                self.nextLookup[c] = [0] * len(s)

        for i in range(len(s)):
            for c in self.prevLookup:
                if s[i] == c:
                    self.prevLookup[c][i] = i
                else:
                    if i == 0:
                        self.prevLookup[c][i] = -1
                    else:
                        self.prevLookup[c][i] = self.prevLookup[c][i-1]  
                    
            
        for i in range(len(s)-1, -1, -1):
            for c in self.nextLookup:
                if s[i] == c:
                    self.nextLookup[c][i] = i
                else:
                    if i == len(s) -1:
                        self.nextLookup[c][i] = -1
                    else:
                        self.nextLookup[c][i] = self.nextLookup[c][i+1]  

    def helper(self, left, right, subset, s):
        if subset:
            self.ret.append(subset + ''.join(reversed(subset)))
    
        if left > right:
            return
    
        
        for c in self.prevLookup:
            leftIdx = self.nextLookup[c][left]
            rightIdx = self.nextLookup[c][right]
    
            if leftIdx >= 0 and leftIdx <= right: 
                self.ret.append(subset + c + ''.join(reversed(subset)))
                if leftIdx < rightIdx:
                    self.helper(leftIdx+1, rightIdx-1, subset+c, s)
            
                
    
    
    
    def findLongestPalin(self, s):
        self.initLookup(s)
        self.helper(0, len(s)-1, "", s)
        return self.ret


so = Solution()

print so.findLongestPalin("abcbabcba")
    

    
    
    



