# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        left_arr = self.preorderTraversal(root.left)
        right_arr = self.preorderTraversal(root.right)
        left_arr.extend(right_arr)
        traversal = []
        traversal.append(root.val)
        traversal.extend(left_arr)
        return traversal
        