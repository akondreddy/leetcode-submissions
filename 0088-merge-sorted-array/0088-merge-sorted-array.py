class Solution(object):
    def merge(self, nums1, m, nums2, n):
        counter = 0
        for i in range(m, m + n):
            nums1[i] = nums2[counter]
            counter += 1
        nums1.sort()
        


        