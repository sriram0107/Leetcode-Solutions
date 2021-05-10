from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        q = deque()
        q.append(root)
        count = 0
        while len(q)!=0:
            n = q.popleft()
            if n == None:
                break;
            count+=1
            q.append(n.left)
            q.append(n.right) 
        return count
            
        