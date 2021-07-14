# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        
        node = head
        nextNode = head.next
        prev = None
        newHead = head.next
        while nextNode:
            if prev:
                prev.next = nextNode
            node.next = nextNode.next
            nextNode.next = node
            prev = node
            node = node.next
            if not node:
                break
            nextNode = node.next
        return newHead