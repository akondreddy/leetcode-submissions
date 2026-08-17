class Solution(object):
    def findPeakElement(self, nums):
        length = len(nums)
        # Singular element
        if length == 1:
            return 0
        # Check leftmost and rightmost
        if nums[0] > nums[1]:
            return 0
        if nums[length - 1] > nums[length - 2]:
            return length - 1
        # Check rest of elements
        left = 1
        right = length - 2
        
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > nums[middle + 1] and nums[middle] > nums[middle - 1]:
                return middle
            elif nums[middle] < nums[middle + 1]:
                left = middle + 1
            elif nums[middle] < nums[middle - 1]:
                right = middle - 1
        return -1
 
       
        