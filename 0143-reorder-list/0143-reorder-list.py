# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        # Brute force solution, add all items to list first
        lst = []
        current = head
        while current:
            lst.append(current)
            current = current.next
        length = len(lst)
        
        # Now, we have a list of all the nodes
        # From here, use two pointers
        start = 1
        end = length - 1
        current = head
        while start <= end:
            current.next = lst[end]
            current = current.next
            if start != end:
                current.next = lst[start]
                current = current.next
            start += 1
            end -= 1
        current.next = None
        