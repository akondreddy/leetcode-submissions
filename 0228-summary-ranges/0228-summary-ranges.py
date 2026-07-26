class Solution(object):
    def summaryRanges(self, nums):
        ranges = []
        length = len(nums)
        if not nums:
            return ranges
        first = 0
        for i in range(length - 1):
            if nums[i + 1] == nums[i] + 1:
                continue
            else:
                if first == i:
                    ranges.append(str(nums[first]))
                else:
                    ranges.append(str(nums[first]) + "->" + str(nums[i]))
                first = i + 1
        if first == length - 1:
                ranges.append(str(nums[first]))
        else:
            ranges.append(str(nums[first]) + "->" + str(nums[-1]))
        return ranges
        