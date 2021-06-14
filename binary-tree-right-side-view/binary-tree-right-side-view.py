from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        q = deque()
        q.append(root)
        rightView = []
        while len(q) != 0:
            count = len(q)
            while count > 0:
                node = q.popleft()
                if count == 1:
                    rightView.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                count -= 1
        return rightView
        