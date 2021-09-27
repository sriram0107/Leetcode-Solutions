from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''
undirected graph

1 - 2 - 5
|   |
3 - 4

(1)

app 1) recursive and take care of duplication
app 2) iterative -> bfs & store

[(3)]
(4)
{
    1: (1) [2,4]
    2: (2) [3,1]
    4: (4) [1,3]
    3: (3) [2,4]
    

}
'''
from collections import deque

class Solution:
    def getClone(self, val):
        clone = Node()
        clone.val = val
        clone.neighbors = []
        return clone
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        dq = deque()
        nodeMap = {}
        
        dq.append(node)
        
        while len(dq) != 0:
            newNode = dq.popleft()
            if newNode.val not in nodeMap.keys():
                clone = self.getClone(newNode.val)
                nodeMap[clone.val] = clone
            
            for nbr in newNode.neighbors:
                if nbr.val not in nodeMap.keys():
                    nbrClone = self.getClone(nbr.val)
                    nodeMap[nbrClone.val] = nbrClone
                    nodeMap[newNode.val].neighbors.append(nbrClone)
                    dq.append(nbr)       
                else:
                    nodeMap[newNode.val].neighbors.append(nodeMap[nbr.val])

        return nodeMap[node.val]
        
        
        
        
            
       