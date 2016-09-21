class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        mapping = {}
        
        for str in strs:
            key = ''.join(sorted(str))
            if key in mapping:
                mapping[key].append(str)
            else:
                mapping[key] = [str]
            
        for key, val in mapping.iteritems():
            result.append(val)
            
        return result
