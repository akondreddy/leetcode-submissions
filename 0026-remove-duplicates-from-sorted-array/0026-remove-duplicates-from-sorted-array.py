class Solution(object):
    def removeDuplicates(self, nums):
        length = len(nums)
        k = 1
        duplicatedNum = nums[0]
        for i in range(length):
            currentNum = nums[i]
            if currentNum != duplicatedNum:
                nums[k] = currentNum
                duplicatedNum = currentNum
                k += 1
        return k


        