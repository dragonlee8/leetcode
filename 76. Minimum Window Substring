class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        count = {}
        n = len(t)

        for x in t:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1

        match = 0
        start, end = 0, 0
        result = []
        tmp = dict.fromkeys(count, 0)
        for end in range(len(s)):
            if s[end] not in count:
                continue
            tmp[s[end]] += 1
            if tmp[s[end]] == count[s[end]]:
                match += 1
            while start < end:
                if s[start] not in count:
                    start += 1
                elif tmp[s[start]] > count[s[start]]:
                    tmp[s[start]] -= 1
                    start += 1
                else:
                    break
            
            if match == len(count.keys()):
                if not result:
                    result = [start, end]
                elif end - start < result[1] - result[0]:
                    result = [start, end]
            
        if not result:
            return ""
        else:
            return ''.join(s[result[0]:result[1]+1])
                    
