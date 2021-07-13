from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        q = deque()
        q.append(node)
        nodeMap = {}
        visited = []
        while len(q) != 0:
            nd = q.popleft()
            if nd.val not in nodeMap.keys():
                nodeMap[nd.val] = Node()
                nodeMap[nd.val].val = nd.val
            visited.append(nd.val)
            for nbr in nd.neighbors:
                if nbr.val not in nodeMap.keys():
                    q.append(nbr)
                    nodeMap[nbr.val] = Node()
                    nodeMap[nbr.val].val = nbr.val
                nodeMap[nd.val].neighbors.append(nodeMap[nbr.val])   
        return nodeMap[node.val]
            
        
        
        
        
            
       