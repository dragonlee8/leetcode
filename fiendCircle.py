# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def findCircle(self, friends):
        if not friends:
            return 0

        n = len(friends)

        union = []
        for i in range(n):
            union.append(i)

        def findParent(i, union):
            while union[i] != i:
                i = union[i]

            return i

        for i in range(len(friends)):
            relation = friends[i]
            for j in range(i+1, len(relation)):
                if relation[j] == 'n':
                    continue
                rooti = findParent(i, union)
                rootj = findParent(j, union)

                union[rootj] = rooti

        print union
        from sets import Set
        circles = Set()
        for i in range(n):
            circles.add(findParent(i, union))

        return len(circles)


friends = ['ynyy',
           'nyyn',
           'yyyn',
           'ynny']

so = Solution()
print so.findCircle(friends)

