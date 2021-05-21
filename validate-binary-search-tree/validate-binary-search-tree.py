# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.check(root,[float("-inf"),float("inf")])
    
    def check(self,root,r_range):
        if root==None:
            return True
        elif root.val>=r_range[1] or root.val<=r_range[0]:
            return False
        else:
            return self.check(root.left,[r_range[0],root.val]) and self.check(root.right,[root.val,r_range[1]])
        
