# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
            
        arr = [str(root.val)]
        tmp = [root]
        d = deque(tmp)
        while d:
            node = d.popleft()
            if node.left:
                arr.append(str(node.left.val))
                d.append(node.left)
            else:
                arr.append('#')
            
            if node.right:
                arr.append(str(node.right.val))
                d.append(node.right)
            else:
                arr.append('#')
            
        i = len(arr) -1 
        #find last index not '#'
        for i in range(len(arr)-1, -1, -1):
            if arr[i] != '#':
                break
        
        return '[' + ','.join(arr[:i+1]) + ']'
            
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return None
        
        if not data[1:-1]:
            return None
        
        nodeArr = data[1:-1].split(',')
        tmp = []
        d = deque(tmp)
        isLeft = True
        root = TreeNode(nodeArr[0])
        d.append(root)
        idx = 0
        
        for x in nodeArr[1:]:
            root = d[idx]
            node = None
            if x != '#':
                node = TreeNode(x)
            if isLeft:
                root.left = node
                isLeft = False
            else:
                root.right = node
                idx += 1
                isLeft = True
            if node:
                d.append(node)
                
        return d[0]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
