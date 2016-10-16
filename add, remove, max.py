import sys
class ListNode(object):
    def __init__(self, key, val):
        self.val = val
        self.next = None
        self.key = key
        
class Solution(object):
    def __init__(self):
        self.mapping = {}
        self.head = ListNode('head', sys.maxint)
        self.tail = self.head
        
        
    def swap(self, node, prev):
        pprev = self.mapping[prev.key]
        pprev.next = node
        tmp = node.next
        node.next = prev
        prev.next = tmp
        
        if self.tail == node:
            self.tail = prev
        
        self.mapping[node.key] = pprev
        self.mapping[prev.key] = node
            
    def add(self, key):
        if key in self.mapping:
            prev = self.mapping[key]
            node = prev.next
            node.val += 1
            while node.val > prev.val:
                self.swap(node, prev)
                prev = self.mapping[node.key]
                
        else:
            node = ListNode(key, 1)
            self.mapping[key] = self.tail
            self.tail.next = node
            self.tail = node
            
            
    def remove(self, key):
        if key not in self.mapping:
            return 
        
        prev = self.mapping[key]
        node = prev.next
        node.val -= 1
        next = node.next
        while next and node.val < next.val:
            self.swap(next, node)
            next = node.next
        
        
    def max(self):
        return self.head.next.key
    
    
so = Solution()
so.add('a')
so.add('a')
so.add('b')
so.add('b')
print so.max()
so.remove('a')
so.add('c')
so.add('c')
print so.max()
so.add('c')
print so.max()
so.remove('c')
print so.max()
so.remove('c')
print so.max()
