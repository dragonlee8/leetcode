# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def helper(self, head, visited):
        if not head:
            return  None
        
        if head in visited:
            return visited[head]
        
        newHead = RandomListNode(head.label)
        visited[head] = newHead
        newHead.next = self.helper(head.next, visited)
        if head.random != None:
            newHead.random = self.helper(head.random, visited)

        return newHead

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        visited = {}

        self.helper(head, visited)
        return visited[head]

