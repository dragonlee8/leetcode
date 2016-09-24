# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def pushFullleft(root, stack):
            while root:
                stack.append(root)
                root = root.left
                
        stack = []
        pushFullleft(root, stack)
        
        node = None
        while stack and k > 0:
            node = stack.pop()
            k -= 1
            if node.right:
                pushFullleft(node.right, stack)
                
        return node.val
