class Solution(object):
    def isPalindrome(self, x):
        # Idea: Build the number in reverse
        # then check if the numbers equal each other

        original = x
        reverse = 0
        while original > 0:
            digit = original % 10
            reverse = reverse * 10 + digit
            original = original / 10
        if reverse == x:
            return True
        return False
        