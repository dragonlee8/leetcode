import sys
class Solution(object):
    def __init__(self, arr):
        self.mapping = {}
        for i in range(len(arr)):
            word  = arr[i]
            if word not in self.mapping:
                self.mapping[word] = [i]
            else:
                self.mapping[word].append(i)


    def shortDist(self, word1, word2):
        if word1 not in self.mapping or word2 not in self.mapping:
            return -1
        
        pos1 = self.mapping[word1]
        pos2 = self.mapping[word2]

        idx1 = 0
        idx2 = 0
        ret = sys.maxint
        while idx1 < len(pos1) and idx2 < len(pos2):
            ret = min(ret, abs(pos1[idx1] - pos2[idx2]))
            if pos1[idx1] < pos2[idx2]:
                idx1 += 1
            else:
                idx2 += 1

        return ret

so = Solution(["practice", "makes", "perfect", "coding", "makes"])
print so.shortDist('makes', 'coding')

