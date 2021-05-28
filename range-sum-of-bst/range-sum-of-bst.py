# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        if root == None:
            return 0
        left_sum = self.rangeSumBST(root.left, low, high)
        right_sum = self.rangeSumBST(root.right, low, high)
        
        if root.val >= low and root.val <= high:
            return root.val + left_sum + right_sum
        
        return left_sum + right_sum
        