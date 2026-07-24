class Solution(object):
    def isPalindrome(self, x):
        # Idea: Build the number in reverse
        # then check if the numbers equal each other

        # Could also convert to string, might be faster

        original = x
        reverse = 0
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x = x / 10
        return reverse == original
        