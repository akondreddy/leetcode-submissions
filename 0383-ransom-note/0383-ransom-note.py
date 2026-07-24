class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        letters = {}
        # Parse through magazine and record letters
        for i in magazine:
            letters[i] = 1 + letters.get(i, 0)
        
        # Parse through ransomeNote, if letters contains
        # the letter, then decrement the count of that letter.
        # Otherwise, return False. If for loop terminates,
        # return True
        for i in ransomNote:
            if i not in letters or letters[i] <= 0:
                return False
            letters[i] = letters[i] - 1
        return True
        
            
        