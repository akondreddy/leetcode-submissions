class Solution(object):
    def longestCommonPrefix(self, strs):
        sortedList = sorted(strs)
        first = sortedList[0]
        last = sortedList[-1]
        shortestLen = len(min(first, last))
        prefix = ""

        for i in range(shortestLen):
            if first[i] == last[i]:
                prefix = prefix + first[i]
            else:
                return prefix
        return prefix

        