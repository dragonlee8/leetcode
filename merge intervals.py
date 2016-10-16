# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        def cmp(a,b):
            return a.start - b.start
        
        intervals.sort(cmp)
        
        ret = []
        for interval in intervals:
            #print interval.start, interval.end
            if ret and ret[-1].end >= interval.start:
                ret[-1].end = max(ret[-1].end, interval.end)
            else:
                ret.append(interval)
            
        return ret
