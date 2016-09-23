# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def helper(self, node, visited):
        if node in visited:
            return visited[node]

        newNode = UndirectedGraphNode(node.label)
        visited[node] = newNode
        for neighbor in node.neighbors:
            newNode.neighbors.append(self.helper(neighbor, visited))

        return newNode

    def cloneGraph(self, node):
        visited = {}
        if not node:
            return None

        self.helper(node, visited)

        return visited[node]
