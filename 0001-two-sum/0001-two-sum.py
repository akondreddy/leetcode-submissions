class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        hashtable = {}

        for i in range(length):
            hashtable[nums[i]] = i

        for i in range(length):
            leftover = target - nums[i]
            if leftover in hashtable and hashtable[leftover] != i:
                return [i, hashtable[leftover]]
        return []
            




        