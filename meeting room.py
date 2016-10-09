
# Definition for an interval.  
# class Interval(object):  
#     def __init__(self, s=0, e=0):  
#         self.start = s  
#         self.end = e  
import heapq


class Solution(object):
    def minMeetingRooms(self, intervals):
        def cmp(a,b):
            return a[0] < b[0]

        intervals.sort(cmp)
        count = 0
        stack = []
        import heapq
        heapq.heapify(stack)
        for start, end in intervals:
            while stack and stack[0] <= start:
                heapq.heappop(stack)
            heapq.heappush(stack, end)
            count = max(count, len(stack))

        return count

so = Solution()
print so.minMeetingRooms([[0, 30],[5, 15],[15, 20]])
