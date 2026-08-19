# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        # Standard method to reverse a linked list
        current = head
        previous = None
        while current:
            temp = current.next
            # The current node's next node will be the one before it
            current.next = previous
            # The previous node then becomes the current node
            previous = current
            # The current node becomes the next node, in order to recurse
            current = temp
        return previous

        