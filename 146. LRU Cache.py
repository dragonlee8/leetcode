class Node:
    def __init__(self, key, val):
        self.value = val
        self.prev = None
        self.next = None
        self.key = key
        
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.kvMap = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.kvMap:
            return -1
        
        node = self.kvMap[key]
        self.moveToHead(node)
        return node.value
        
    def moveToHead(self, node: Node):
        if self.head.next == node:
            return
        
        self.removeNode(node)
        self.insertHead(node)
        
    def insertHead(self, node):
        if not node:
            return
        firstNode = self.head.next
        if firstNode:
            node.next = firstNode
            firstNode.prev = node
        self.head.next = node
        node.prev = self.head
        if not self.tail.next:
            self.tail.next = node

        self.kvMap[node.key] = node

    def removeNode(self, node: Node):
        if not node:
            return
        prevNode = node.prev
        nextNode = node.next

        if nextNode == None:
            self.tail.next = prevNode
        else:
            nextNode.prev = prevNode
        prevNode.next = nextNode
        del self.kvMap[node.key] 

    def put(self, key: int, value: int) -> None:
        if key in self.kvMap:
            node = self.kvMap[key]
            node.value = value
            self.moveToHead(node)
        else:
            node = Node(key, value)
            self.insertHead(node)
            
        if len(self.kvMap.keys()) > self.capacity:
            self.removeNode(self.tail.next)

                
                
                

            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
