# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        # Recursive helper function.
        # In scenario of empty nums, left > right, 0 > -1,
        # so return None.
        def build(left, right):
            if left > right:
                return None
            
            # Get middle value of nums
            middle = (left + right) // 2
            root = TreeNode(nums[middle])

            # From middle, determine the left subtree by 
            # starting from left up until before middle
            root.left = build(left, middle - 1)
            # Determine the right subtree by starting from 
            # right after middle until the end of array
            root.right = build(middle + 1, right)

            return root
        
        return build(0, len(nums) - 1)

        
        

        