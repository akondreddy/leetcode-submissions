class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # Iterate through every char in ransomNote.
        # .count(char) returns the amount of char in
        # the string. If the ransomNote contains more of one
        # character than magazine does, then it is not possible
        # for magazine to create ransomNote, returning False.
        for char in set(ransomNote):
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True
        
            
        