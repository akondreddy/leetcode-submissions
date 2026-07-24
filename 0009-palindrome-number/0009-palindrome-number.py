class Solution(object):
    def isPalindrome(self, x):
        # Idea: Build the number in reverse
        # then check if the numbers equal each other

        # Negative
        if x < 0: 
            return False

        original = x
        reverse = 0
        while original > 0:
            reverse = (reverse * 10) + (original % 10)
            original = original / 10
        return reverse == x
        