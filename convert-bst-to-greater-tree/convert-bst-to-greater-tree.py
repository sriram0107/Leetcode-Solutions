# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.convertTree(root, 0)
        return root
        
    def convertTree(self, root, p_sum):
        if root == None:
            return 0
        val = root.val
        right_sum = self.convertTree(root.right, p_sum)
        root.val += (right_sum + p_sum)
        left_sum = self.convertTree(root.left, root.val)
        return left_sum + val + right_sum
        
        
        
        
'''
1. sum of right subtree
2. for left nodes, sum of parent + sibling subtree
'''