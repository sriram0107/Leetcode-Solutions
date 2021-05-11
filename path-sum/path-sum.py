# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root == None:
            return False
        elif root.left == None and root.right == None and root.val == targetSum:
            return True
        
        left_path = False
        right_path = False
        if root.left:
            left_path = self.hasPathSum(root.left, targetSum - root.val)
        if root.right:
            right_path = self.hasPathSum(root.right, targetSum - root.val)
            
        return left_path or right_path
        